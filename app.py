from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, number, login_required, passValidate, lookup, company_officers, tickerHistory, displayDate, fundOwnership, institution_ownership

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///stock.db")

# Custom filter for displaying numbers
app.jinja_env.filters["number"] = number

# Custom filter for displaying date
app.jinja_env.filters["displayDate"] = displayDate


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("Must provide username", 400)

        regUser = request.form.get("username")
        dbUser = db.execute("Select * FROM users WHERE username = ?", regUser)

        # Search for duplicate usernames (dbUser) == 1 skips the error with empty lists returned from the db
        if len(dbUser) == 1 and (dbUser[0]["username"]) == regUser:
            return apology("Username taken", 400)

        # Ensure pasword was submitted
        if not request.form.get("password") or not request.form.get("confirmation"):
            return apology("Please provide password and/or confirmation", 400)

        # Ensure password and password confirmation match
        if request.form.get("password") != request.form.get("confirmation"):
            return apology("Passwords do not match", 400)

        # Validate password
        if passValidate(request.form.get("password")) is False:
            return apology("Password must have: Uppercase & lowercase letters, numbers, spercial characters and min 8 characters", 400)

       # If both username and password are validated register the user and update the db
        regPass = request.form.get("password")

        # Register user and password in the database
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", regUser, generate_password_hash(regPass))
        flash("Registered!")
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("Invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        flash("Logged in!")
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Get stock quote."""

    if request.method == "POST":

        # Standardize Symbol for Jinja use with upper
        symbol = request.form.get("symbol").upper()
        print("symbol: ", symbol)

        if symbol:
            ticker = lookup(symbol)

            # If lookup is not succesful return apology:
            if ticker is None:
                flash("The symbol does not exist! Please enter a valid symbol.")
                return redirect("/")
            else:
                compOfficers = company_officers(ticker, symbol).to_html(classes=["table", "text-start", "border-0", "table-hover"], index=False, justify="left")
                fOwnership = fundOwnership(ticker).to_html(classes=["table", "text-start", "border-0", "table-hover"], index=False, justify="left")
                iOwnership = institution_ownership(ticker).to_html(classes=["table", "text-start", "border-0", "table-hover"], index=False, justify="left")
                showTickerHistory = tickerHistory(ticker, symbol).to_html

                return render_template("stocks.html", data=ticker, symbol=symbol, officers=compOfficers, tickrHistory = showTickerHistory, fOwnership = fOwnership, iOwnership = iOwnership)
        else:

            # If empty symbol
            flash("Please Emter a symbol!")
            return redirect("/")
    else:
        return render_template("index.html")