# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import numpy
import requests
from datetime import datetime,timedelta
from time import mktime

alpha_vantage_api_key = "4NE2ALTFPGT83V3S"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(10, 410, 781, 131))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pushButton = QtWidgets.QPushButton(self.splitter)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_2.setObjectName("pushButton_2")

        date_axis = TimeAxisItem(orientation='bottom')
        self.graphicsView = pg.PlotWidget(self.centralwidget, axisItems={'bottom':date_axis})
        self.graphicsView.setBackground('w')

        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 781, 391))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(lambda:self.pull_stock_macd_data())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Draw"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))

    def pull_stock_macd_data(self):
        technical_url = 'https://www.alphavantage.co/query?function=MACD&symbol=' + 'aapl' + \
                        '&interval=daily&series_type=open&apikey=' + alpha_vantage_api_key

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

        index = 0
        # # Go through this loop and store everything into an array later for plotting
        for data in macd_data:
            if index < 50:
                #print(type(data))
                date = datetime.strptime(data,'%Y-%m-%d')
                print('The type of data is: ' + str(type(date))+ ' and the value is:' + str(date))
                date_array.append(date)
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

        for i in range(2):
            if i == 0:
                y_data = macd_array
                line_symbol = 'o'
            elif i == 1:
                y_data = macd_signal_array
                line_symbol = 't'

            self.graphicsView.plot(x=[x.timestamp() for x in date_array], y=y_data, pen=(i,2), symbol=line_symbol)

            # self.graphicsView.BarGraphitem(x=[x.timestamp() for x in date_array],height = macd_hist_array,brush = 'b')


class TimeAxisItem(pg.AxisItem):
    def tickStrings(self, values, scale, spacing):
        return [datetime.fromtimestamp(value) for value in values]

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
