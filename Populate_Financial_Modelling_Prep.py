import requests, json
import sqlite3
from sqlite3 import Error

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
    return(stock_list['symbolsList'])

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_table(db_file):
    """ Try connection to the SQLite database  if not exist then we make a table
        The table format are as of follows, please refer to dict.txt for more
        information
    """

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        parsed_dictionary = Populate_Stock_List()
        c = conn.cursor()
        c.execute("DROP TABLE stocksList")
        c.execute("CREATE TABLE IF NOT EXISTS stocksList( symbol TEXT, name TEXT, exchange TEXT);")
        for key in parsed_dictionary:
            print(key)
            symbol = key['symbol']
            if 'name' in key:
                name = key['name']
            else:
                name = ''
            if 'exchange' in key:
                exchange = key['exchange']
            else:
                exchange = ''
            insert_statement = 'INSERT INTO stocksList(symbol, name, exchange) VALUES("' + symbol +'","' + name + '","' + exchange + '");'
            print(insert_statement)
            c.execute(insert_statement)

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    database = r"/Users/weixiong/Documents/GitHub/Fundamental_Analysis/StockList.db"
    create_table(r"/Users/weixiong/Documents/GitHub/Fundamental_Analysis/StockList.db")