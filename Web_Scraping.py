###########################
# Created on May 6th 2020
# @ Author: WillBear
###########################



import requests
from bs4 import BeautifulSoup
import investpy
from selenium import webdriver
from

def find_stock_price():
    url = 'https://finance.yahoo.com/quote/FB?p=FB'
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    # print(soup)
    # The price is pulled from
    price = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text

    print(price)

def find_analyst_target(symbol):
    url = 'https://finance.yahoo.com/quote/'+symbol+'?p=' + symbol
    response = requests.get(url)

    # Call the response and convert it into a lxml format
    soup = BeautifulSoup(response.text,'lxml')
    # print(soup)
    data_table = soup.find_all('table', {'class':'W(100%) M(0) Bdcl(c)'})
    print(data_table)

    target_price = data_table[0].find('td', {'class':'Ta(end) Fw(600) Lh(14px)','data-test':'ONE_YEAR_TARGET_PRICE-value'})
    print(target_price)
    print(target_price.text)

def find_technical_details(symbol):
    # Using the investpy module, we would get investing.com website url for the company
    # TODO:
    # Add functionality for Canadian and Stocks that are from other parts of the world
    company_profile = investpy.get_stock_company_profile(stock=symbol,
                                                        country='United States')
    # print(company_profile)

    company_profile_url = company_profile['url']
    technical_url = company_profile_url[:-15] + 'technical'

    response = requests.get(technical_url, headers={'User-Agent': 'Mozilla/5.0'})

    soup = BeautifulSoup(response.text,'lxml')
    # print(soup)
    data_table = soup.find_all('div', {'id':'techinalContent'})
    # print(data_table)
    cols = [td.text for td in data_table[0].select('td')]
    # print(cols)

    # We initializa a empty list
    parsed_list=[]

    # Parse data that we receive from web scraping into array
    for text in cols:
        parsed_list.append(text.strip())

    # Now we initialize a dictionary that contains information in regards to the data we want, as well as how
    # many number of  elements are contained in the array
    technical_indicators = {'Classic': 7, 'RSI(14)': 1, 'MACD(12,26)': 2, 'MA10': 1, 'MA20': 1, 'MA100': 1, }

    # We have to populate an empty array with the correct rows and columns,
    row = len(technical_indicators)
    column = max(technical_indicators.values())
    print('row: ' + str(row) + ' column: ' + str(column))

    # Declare an empty array with corresponding rows and columns
    # technical_values = [] * column
    technical_values = [[None] * column] * row
    print(technical_values)
    found_data = False
    row_index = 0
    # We process the following data into a two dimensional array
    for text in parsed_list:
        if found_data and (control_index < terminating_index):
            print('Row: ' + str(row_index) +' Column: ' +str(control_index) + ' Text is:' + text)
            # print('the type for text is:'+ str(type(text)))
            # technical_values[row_index][control_index] = text
            control_index = control_index + 1
        else:
            found_data = False

        if text in technical_indicators:
            # row_index = list(technical_indicators).index(text)
            technical_values[row_index].append(text)
            row_index = row_index + 1
            print('Title Found: ' + str(text) + ' ' + str(row_index))
            terminating_index = technical_indicators[text]
            found_data = True
            control_index = 0

    print(technical_values)


find_technical_details('IBM')