from yahooquery import Ticker

# another test!!!
try:
    aapl = Ticker('1111')
    print(aapl.summary_profile['aapl']['longBusinessSummary'])
except (KeyError, ValueError):
    print("Invalid input or symbol not found.")

