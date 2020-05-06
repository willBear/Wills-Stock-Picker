###########################
# Created on May 6th 2020
# @ Author: WillBear
###########################



import requests
from bs4 import BeautifulSoup

def find_stock_price():
    url = 'https://finance.yahoo.com/quote/FB?p=FB'
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    # print(soup)
    # The price is pulled from
    price = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text

    print(price)

def find_analyst_target(symbol):
    url = 'https://www.tradingview.com/symbols/NYSE-BA/technicals/'