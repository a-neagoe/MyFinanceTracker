from yahooquery import Ticker

# another test!!!
try:
    t = Ticker('aapl')
    print(aapl.summary_profile['aapl']['longBusinessSummary'])
except (KeyError, ValueError):
    print("Invalid input or symbol not found.")

