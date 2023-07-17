# MyFinanceTracker

#### Description:

Stock Research is a flask app made for looking up information about Stocks, Mutual Funds and ETFs.

## Requirements

```bash
cs50
Flask
Flask-Session
requests
pandas
yahooquery (versions below v2.3.2 are broken)
plotly.graph_objs
```

## Use and purpose:

This web app was designed Primarily for self learning about the Stock Market. In the long run I want to add notes and info about financial indicators displayed in the app and provide advanced charts displayed in a separate page.

Example:

> Bid size represents the quantity of a security that investors are willing to purchase at a specified bid price. Bid size is stated in board lots representing 100 shares each. Therefore, a bid size of four represents 400 shares. Bid sizes are important because they reflect the demand and liquidity of a security.

## What's inside:

Flask app with app.py, helpers.py, database and two folders for the templates and the static files.

## Functions Description

The main functions are lookup and lookupETF and they provide data objects for stocks and mutual funds/etfs. Each function uses a different template/route as the information displayed for ETFs is less comprehensive than the one used for stocks.

The other functions are used in support and they return dataframes used for the tables (made with pandas), filters used for jinja, the chart with the OHLC data for the past three years or the password validation used for the registration module.

## To Do

Store the data in variables to reduce the number of querries and increasae load times.
