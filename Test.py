import matplotlib.pyplot as plt
import requests,json
import numpy as np

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
    macd_signal_array = []
    print('The type of data of macd_data is:' + str(type(macd_data)))
    print(macd_data)

    index = 0
    # # Go through this loop and store everything into an array later for plotting
    for data in macd_data:
        if index < 200:
            print(data)
            date_array.append(data)
            macd_array.append(float(macd_data[data]['MACD']))
            macd_signal_array.append(float(macd_data[data]['MACD_Signal']))
            index = index + 1
        else:
            break
    date_array.reverse()
    macd_array.reverse()
    macd_signal_array.reverse()

    plt.yticks(np.arange(min(macd_array), max(macd_array), step=(max(macd_array) - min(macd_array))/10))
    plt.xticks(rotation=45)
    plt.plot(date_array, macd_array, marker='o', linestyle='-', color = 'blue')
    plt.plot(date_array, macd_signal_array, marker='o', linestyle='-', color = 'orange')
    plt.grid(True)
    plt.show()


pull_stock_macd_data('aapl')