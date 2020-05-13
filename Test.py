import mplfinance
import requests,json
import pandas as pd

alpha_vantage_api_key = "4NE2ALTFPGT83V3S"

def pull_stock_macd_data(ticker):
    technical_url = 'https://www.alphavantage.co/query?function=MACD&symbol='+ ticker +\
                    '&interval=daily&series_type=open&apikey='+ alpha_vantage_api_key

    req_ob = requests.get(technical_url)

    # result contains list of nested dictionaries
    result = req_ob.json()

    last_refresh_date = result['Meta Data']['3: Last Refreshed']
    print("Last Refresh Date is:" + last_refresh_date)

    interval = result['Meta Data']['4: Interval']
    print("The interval of refresh is :" + last_refresh_date)

    macd_data = result['Technical Analysis: MACD']

    # Declare Four Variables that we need to plot into the graph
    date_array = []
    macd_array = []

    # Go through this loop and store everything into an array later for plotting
    for date in macd_data:
        date_array.append(date)
        macd_array.append(date['MACD'])
    mplfinance.plot()

    # print(result)

pull_stock_macd_data('aapl')