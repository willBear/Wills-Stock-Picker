import requests, json
# -------------------------------------------------------------------
# Function Name: Populate_Stock_List
#
# Description: This function is used to pull data from Financial
# Modelling Prep, it contains a list of stock data that this
# website contains and stores it into a database file
#
# -------------------------------------------------------------------

def Populate_Stock_List():
    # Set up the JSON url that we need to use from financial modelling prep
    # Note: This URL may change in the future, please visit website for
    # further information
    url = "https://financialmodelingprep.com/api/v3/company/stock/list"
    session = requests.session()
    request = session.get(url, timeout=5)
    stock_list = request.json()

    # Now we have the data that we need from financial modelling prep
    # we need to store the useful data into a server
    # The dictionary returned from the website is a nested dictionary
    # therefore we travelse through this dictionary and save it all
    print(len(stock_list['symbolsList']))
    hi = 0
    for key in stock_list['symbolsList']:
        print(stock_list['symbolsList'][hi])
        hi = hi + 1



Populate_Stock_List()
