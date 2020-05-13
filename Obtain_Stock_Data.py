
import requests,json
import csv
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
def retrieve_technical_indicator():
    base_url = "https://www.alphavantage.co/query?function=SMA&symbol=IBM&interval=daily&time_period=10&series_type=open&apikey="+alpha_vantage_api_key
    session = requests.session()
    request = session.get(base_url, timeout=5)
    technical_data = request.json()
    print(technical_data)
    base_url = "https://www.alphavantage.co/query?function=RSI&symbol=IBM&interval=daily&time_period=10&series_type=open&apikey="+alpha_vantage_api_key
    session = requests.session()
    request = session.get(base_url, timeout=5)
    rsi = request.json()
    print(rsi)

def Retrieve_Financial_Ratios():
    # base_url variable that stores the base url
    base_url = "https://financialmodelingprep.com/api/v3/financial-statement-growth/AAPL?period=Annual"

    session = requests.session()
    request = session.get(base_url, timeout=5)
    financial_ratio = request.json()

    print(financial_ratio)


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

def populate_MACD_graph(ticker):
    technical_url = 'https://www.alphavantage.co/query?function=MACD&symbol='+ ticker +\
                    '&interval=daily&series_type=open&apikey='+ alpha_vantage_api_key

    # main_url variable that stores complete url with API key
    req_ob = requests.get(technical_url)

    # result contains list of nested dictionaries
    result = req_ob.json()

    print(result)

populate_MACD_graph('AAPL')




