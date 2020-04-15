import requests,json
from functools import reduce
import pandas as pd
from datetime import date
from pandas.tseries.offsets import BDay

alpha_vantage_api_key = "4NE2ALTFPGT83V3S"

def Populate_Sector_Performances():

    # base_url variable that stores the base url
    base_url = "https://www.alphavantage.co/query?function=SECTOR"

    # main_url variable that stores complete url with API key
    main_url = base_url + "&apikey=" + alpha_vantage_api_key

    # Debug the main_url
    print(main_url)

    # get method of requests module
    # return response object
    req_ob = requests.get(main_url)

    # json method return json format
    # data into python dictionary data type.

    # result contains list of nested dictionaries
    result = req_ob.json()

    print(type(result))
    print(result)
    #parsed_dictionary = result['Rank A: Real-Time Performance']





def Populate_Intraday_Price():
    major_indices = ["SPX","IXCO","RUT","RUT"]

    # base_url variable that stores the base url
    base_url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE"

    # main_url variable that stores complete url with API key
    main_url = base_url + "&symbol=^GSPC&apikey=" + alpha_vantage_api_key
    req_ob = requests.get(main_url)

    # json method return json format
    # data into python dictionary data type.

    # result contains list of nested dictionaries
    result = req_ob.json()

    print(type(result))
    print(result)
    """
    print(result["Global Quote"]['10. change percent'])
    changed_percent = result["Global Quote"]['10. change percent']
    changed_percent = changed_percent[:-1]
    changed_percent_float = float(changed_percent)

    if (changed_percent_float < 0):
        print("RED")
    else:
        print("GREEN")
    """
"""
url = "https://financialmodelingprep.com/api/v3/majors-indexes"
session = requests.session()
request = session.get(url, timeout=5)
stock_data = request.json()
print(stock_data)


for key in stock_data['majorIndexesList']:
    print(str(key['ticker']) + ' ' + str(key['changes']) + ' ' +str(key['price']) + ' ' + str(key['indexName']))
"""
banner_indices = ['SPY','QQQ','IWM','DIA','^VIX','GLD']


# This def is used for finding the previous day's closing price of multiple selected stock/index
def find_closing_price_multiple(tickers):
    # Iterate through the array of tickers and add it to the quote string
    quote_string = ','.join(tickers)

    url = "https://financialmodelingprep.com/api/v3/quote/" + quote_string
    session = requests.session()
    request = session.get(url, timeout=5)
    closing_price_data = request.json()


Populate_Sector_Performances()




