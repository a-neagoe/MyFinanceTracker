# Stock Research
#### Video Demo:  <URL HERE>
#### Description:

Stock Research is a flask app made for looking up information about Stocks, Mutual Funds and ETF.

## Requirements

```bash
cs50
Flask
Flask-Session
requests
pandas
yahooquery
plotly.graph_objs
```

## Use and purpose:
Primarily for self learning about Stock Market. In the long run I want to add notes and info about data found in the app and advanced charts displayed in a separate page.

Example:
> Bid size represents the quantity of a security that investors are willing to purchase at a specified bid price. Bid size is stated in board lots representing 100 shares each. Therefore, a bid size of four represents 400 shares. Bid sizes are important because they reflect the demand and liquidity of a security.


## What's inside:

Flask app with app.py, helpers.py, database and two folders for the templates and the static files.

## Functions Description

The main functions are lookup and lookupETF and they provide data objects for stocks and mutual funds/etfs. Each function uses a different template/route as the information displayed for ETFs is less comprehensive and different than the one used for stocks.

The other functions are used in support and they return dataframes used for the tables (made with pandas), filters used for jinja, the chart with the OHLC data for the past three years or the password validation used for the registration module.

## Some design considerations: Why I did or did not do some things

The web app is far from finished and it's main flaw is the loading time for the stocks. Because the API had data  for the Yahoo Finance tabs in multiple modules, I had to compromise and made queries for each row displayed in some tabs as the info displayed with loops and dictionaries would not have the same usability. This got worse as the all tabs displayed in the main page are loaded upfront. The queries also needed empty data verification deployed directly in jinja in order to prevent the app's crash, if the filters used for usability would be applied on empty data objects.

The loading time could be mitigated if each tab would be rendered in a separate template, preserving the main page's layout and  making the request less taxing, as there would be less overhead when making the querries. I could also try to prepare and serve the data better in the helpers functions.



## Roadmap

Although the app replicates Yahoo Finance, it's main functionality will shift to displaying advanced charts that could display price trends, oscillators and candlestick patterns from OHLCV datasets. The whole project was a test for better understanding the pandas dataframes and to actually be able to render a plotly graph inside of an html's div. The use of the database and a better API (maybe a payed one with an API key) is considered.
