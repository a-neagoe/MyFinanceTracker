import re
import yahooquery as yq
import pandas as pd

from flask import redirect, render_template, request, session
from functools import wraps
from yahooquery import Ticker


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

#  lookup a single symbol using ticker object from yahooquery
def lookup(symbol):
    """Look up quote for symbol."""

    try:
        # validate using keyword arguments
        t = Ticker(symbol, validate=True)

        # handle a single symbol (if more are added later the code should be changed)
        if t.invalid_symbols:
            return None
        else:
            return t
    except (KeyError, ValueError, AttributeError):
        print("Invalid input or symbol not found.")
        return None


# def usd(value):
#     """Format value as USD."""
#     return f"${value:,.2f}"


# register pasword validation
def passValidate(password):

    # Uppercase, lowercase, numbers, spercial characters and min lenght = 8
    if re.match(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", password):
        return True
    else:
        return False