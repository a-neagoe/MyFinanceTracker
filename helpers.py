import re
import yahooquery as yq
import pandas as pd
import plotly.graph_objs as go

from flask import redirect, render_template, request, session
from functools import wraps
from yahooquery import Ticker
from datetime import date, timedelta



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
    """Look up ticker."""

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

# return pd.DataFrame table for company officers
def company_officers(tick, symb):
    # Get the DataFrame
    df=pd.DataFrame(tick.asset_profile[symb]['companyOfficers'])

    # Rename table columns
    df.columns = ["Max Age", "Name", "Age", "Title", "Year Born", "Fiscal Year", "Total Pay", "Exercised Value", "Unexercised Value"]

    # Format column data and intialize column's list
    cols = ['Year Born', 'Fiscal Year', 'Total Pay']
    for col in cols:

        # Convert column's values to int or N/A if no value using an anonymous function (lambda x) anx
        if col == 'Year Born' or col == 'Fiscal Year':
            df[col] = df[col].apply(lambda x: int(x) if x == x else "N/A")

        # Convert values to millions with two digits float N/A if no value
        if col == 'Total Pay':
            df[col] = df[col].apply(lambda x: f'{x/1000000:.2f}M' if x == x else "N/A")

    # Drop columns
    data = df.drop(labels=["Max Age", "Age", "Exercised Value", "Unexercised Value"], axis=1)
    return data

def fundOwnership(tick):

    df = pd.DataFrame(tick.fund_ownership)

    # Prepare columns
    df.columns = ["Max Age", "Date Reported", "Holder", "% Held", "Shares", "Value", "Change"]
    cols = ["Max Age", "Date Reported", "Holder", "% Held", "Shares", "Value", "Change"]

    # Convert column's values to int or N/A if no value
    for col in cols:

        # Show %
        if col == '% Held':
            df[col] = df[col].apply(lambda x: f'{x * 100:.2f}%' if x == x else "N/A")

        # Format as , separated number
        if col == 'Shares' or col == 'Value':
            df[col] = df[col].apply(lambda x: f'{x:,.0f}' if x == x else "N/A")

    # # Drop columns
    data = df.drop(labels=["Max Age", "Change"], axis=1)
    return data


def institution_ownership(tick):
    df = pd.DataFrame(tick.institution_ownership)

    # Prepare columns
    df.columns = ["Max Age", "Date Reported", "Holder", "% Held", "Shares", "Value", "Change"]
    cols = ["Max Age", "Date Reported", "Holder", "% Held", "Shares", "Value", "Change"]

    # Convert column's values to int or N/A if no value
    for col in cols:
        if col == '% Held':
            df[col] = df[col].apply(lambda x: f'{x * 100:.2f}%' if x == x else "N/A")
        if col == 'Shares' or col == 'Value':
            df[col] = df[col].apply(lambda x: f'{x:,.0f}' if x == x else "N/A")

    # # Drop columns
    data = df.drop(labels=["Max Age", "Change"], axis=1)
    return data


 #  Create a Panda DataFrame from a list:
def tickerHistory(tick, symbol):

    # Get the approximate start date three years ago
    threeYears = (date.today() - timedelta(days=3*365)).strftime("%Y-%m-%d")

    # Format all values from the data frame in two decimals format using , as separator
    pd.options.display.float_format = '{:,.2f}'.format

    # Reset_index(inplace=True) and to_datetime needed for plotly graph in ("%Y-%m-%d") format
    df = tick.history(interval="1d", start=(threeYears), end=(date.today().strftime("%Y-%m-%d"))).reset_index()

    # Feed the ohlc data to plotly
    CandleStick = [go.Candlestick(x=df['date'],
    open=df['open'],
    high=df['high'],
    low=df['low'],
    close=df['close'],
    name='Stock Price')]

    # Set the name, theme and overlay the name inside the chart
    Layout = go.Layout(title= symbol + "Share Price",
                        title_x=0.5,
                        template='plotly_dark',
                        yaxis2=dict(title='Share Price'.title(), side='right', overlaying='y'))

    chart = go.Figure(data = CandleStick, layout = Layout)
    return chart

# register pasword validation
def passValidate(password):

    # Uppercase, lowercase, numbers, spercial characters and min lenght = 8
    if re.match(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", password):
        return True
    else:
        return False

def number(value):
    """Format value as a number."""
    return f"{value:,.0f}"


def displayDate(date):
    """Format date to a shorter format """
    date = date[0:10]
    return date