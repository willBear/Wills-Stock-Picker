import matplotlib.pyplot as plt
import requests,json
import numpy as np
import sys
import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

alpha_vantage_api_key = "4NE2ALTFPGT83V3S"

import sys
import random
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.setCentralWidget(self.canvas)

        n_data = 50
        self.xdata = list(range(n_data))
        self.ydata = [random.randint(0, 10) for i in range(n_data)]
        self.update_plot()

        self.show()

        # Setup a timer to trigger the redraw by calling update_plot.
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        # Drop off the first y element, append a new one.
        self.ydata = self.ydata[1:] + [random.randint(0, 10)]
        self.canvas.axes.cla()  # Clear the canvas.
        self.canvas.axes.plot(self.xdata, self.ydata, 'r')
        # Trigger the canvas to update and redraw.
        self.canvas.draw()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()


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
    macd_hist_array = []
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
            macd_hist_array.append(float(macd_data[data]['MACD_Hist']))
            index = index + 1
        else:
            break
    date_array.reverse()
    macd_array.reverse()
    macd_signal_array.reverse()
    macd_hist_array.reverse()

    plt.yticks(np.arange(min(macd_array), max(macd_array), step=(max(macd_array) - min(macd_array))/10))
    plt.xticks(rotation=45)
    plt.plot(date_array, macd_array, linestyle='-', color = 'blue')
    plt.plot(date_array, macd_signal_array, linestyle='-', color = 'orange')
    plt.bar(date_array,macd_hist_array)
    # plt.grid(True)
    plt.show()


