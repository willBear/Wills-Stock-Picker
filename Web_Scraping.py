###########################
# Created on May 6th 2020
# @ Author: WillBear
###########################



import requests
from bs4 import BeautifulSoup
import investpy

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
    company_profile = investpy.get_stock_company_profile(stock=symbol,
                                                        country='United States')
    print(company_profile)
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

    array_index_row = 0
    row = len(technical_indicators)
    column = max(technical_indicators.values())
    print('row: ' + str(row) + ' column: ' + str(column))
    parsed_array = [[0] * column] * row
    found_data = False
    # We process the following data into a two dimensional array
    for text in parsed_list:
        if found_data and (control_index < terminating_index):
            parsed_array[row_index].insert(text)
            control_index = control_index + 1
        else:
            found_data = False

        if text in technical_indicators:
            parsed_array.insert(array_index_row,text)
            row_index = list(technical_indicators).index(text)
            print('Text Found: ' + str(text) + ' ' + str(row_index))
            terminating_index = technical_indicators[text]
            found_data = True
            control_index = 0



find_technical_details('IBM')