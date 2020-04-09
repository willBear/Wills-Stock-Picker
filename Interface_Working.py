# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface_Workfile.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import requests,json




class Ui_MainWindow(object):
    # -------------------------------------------------------------------
    # Function Name: UpdateTime
    #
    # Description: This function is run every 1 second to update the date
    # and time labels on the top left of the main window.This function is
    # called from the QT timer expiry at the bottom of the setupUI
    # function.
    # -------------------------------------------------------------------
    def UpdateTime(self):
        current_time = datetime.now()
        # To Debug the current time
        # print(current_time.strftime("%H:%M:%S"))

        # Update the text label with current time, one for date and another for current time
        self.TimeNow_Label.setText(current_time.strftime("%H:%M:%S"))
        self.DateNow_Label.setText(current_time.strftime("%b %d %Y"))

    # -------------------------------------------------------------------
    # Function Name: UpdateBanner
    #
    # Description: This function is run every 30 seconds to update the
    # banner on the top of main window application that refreshes by
    # making a query to financialmodellingprep.com, multiple quotes.
    # When we receive a correct result from the website, we would update
    # the banners to have its information filled in.
    #
    # TODO:
    # Change colour based on the percentaged changed being + or -
    # Background colour flash for every update
    # Improve mass updating of banners to shave processing time
    # -------------------------------------------------------------------
    def UpdateBanner(self):
        # Fetch Real Time Data and Stores Previous Day Price
        # -------------------------------------------------------------------
        # ETFs Shown on Header:
        # SPY - SPDR S&P 500 ETF Trust -
        # QQQ - Invesco QQQ Trust
        # IWM - iShares Russell 2000 ETF
        # DIA - SPDR Dow Jones Industrial Average ETF Trust
        # ^VIX - CBOE Volatility Index
        # GLD - SPDR Gold Shares
        # SLV - iShares Silver Trust
        # -------------------------------------------------------------------
        banner_indices = ['SPY', 'QQQ', 'IWM', 'DIA', '^VIX', 'GLD', 'SLV']

        # Iterate through the array of tickers and add it to the quote string
        # We are requesting multiple quotes from
        quote_string = ','.join(banner_indices)

        # The URL that we will concatenate with quote_string, makes the request
        # and stores the result into closing_price_data
        url = "https://financialmodelingprep.com/api/v3/quote/" + quote_string
        session = requests.session()
        request = session.get(url, timeout=5)
        closing_price_data = request.json()

        # We would parse the data by looping through the nested dictionary and
        # insert the content of each dictionary into its rightful place
        for key in closing_price_data:
            if key['symbol'] == banner_indices[0]:
                self.Index_Symbol_0.setText(key['symbol'])
                self.Index_Price_0.setText(str(key['price']))
                # We take out the one word pre-fix to the ETF name
                self.Index_Name_0.setText(str(key['name']).split(' ', 1)[1])
                self.Index_Percentage_0.setText(str(key['changesPercentage']) + "%")
            elif key['symbol'] == banner_indices[1]:
                self.Index_Symbol_1.setText(key['symbol'])
                self.Index_Price_1.setText(str(key['price']))
                self.Index_Name_1.setText(str(key['name']).split(' ', 1)[1])
                self.Index_Percentage_1.setText(str(key['changesPercentage']) + "%")
            elif key['symbol'] == banner_indices[2]:
                self.Index_Symbol_2.setText(key['symbol'])
                self.Index_Price_2.setText(str(key['price']))
                self.Index_Name_2.setText(str(key['name']).split(' ', 1)[1])
                self.Index_Percentage_2.setText(str(key['changesPercentage']) + "%")
            elif key['symbol'] == banner_indices[3]:
                self.Index_Symbol_3.setText(key['symbol'])
                self.Index_Price_3.setText(str(key['price']))
                self.Index_Name_3.setText(str(key['name']).split(' ', 1)[1])
                self.Index_Percentage_3.setText(str(key['changesPercentage']) + "%")
            elif key['symbol'] == banner_indices[4]:
                self.Index_Symbol_4.setText(key['symbol'])
                self.Index_Price_4.setText(str(key['price']))
                self.Index_Name_4.setText(str(key['name']).split(' ', 1)[1])
                self.Index_Percentage_4.setText(str(key['changesPercentage']) + "%")
            elif key['symbol'] == banner_indices[5]:
                self.Index_Symbol_5.setText(key['symbol'])
                self.Index_Price_5.setText(str(key['price']))
                self.Index_Name_5.setText(str(key['name']).split(' ', 1)[1])
                self.Index_Percentage_5.setText(str(key['changesPercentage']) + "%")
            elif key['symbol'] == banner_indices[6]:
                self.Index_Symbol_6.setText(key['symbol'])
                self.Index_Price_6.setText(str(key['price']))
                self.Index_Name_6.setText(str(key['name']).split(' ', 1)[1])
                self.Index_Percentage_6.setText(str(key['changesPercentage']) + "%")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1024, 768)
        MainWindow.setMouseTracking(False)
        MainWindow.setAcceptDrops(False)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TimeNow_Label = QtWidgets.QLabel(self.centralwidget)
        self.TimeNow_Label.setGeometry(QtCore.QRect(10, 50, 140, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.TimeNow_Label.setFont(font)
        self.TimeNow_Label.setMouseTracking(False)
        self.TimeNow_Label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TimeNow_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.TimeNow_Label.setWordWrap(True)
        self.TimeNow_Label.setObjectName("TimeNow_Label")
        self.DateNow_Label = QtWidgets.QLabel(self.centralwidget)
        self.DateNow_Label.setGeometry(QtCore.QRect(0, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.DateNow_Label.setFont(font)
        self.DateNow_Label.setMouseTracking(False)
        self.DateNow_Label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DateNow_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.DateNow_Label.setWordWrap(True)
        self.DateNow_Label.setObjectName("DateNow_Label")
        self.Index_Symbol_0 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Symbol_0.setGeometry(QtCore.QRect(170, 10, 61, 20))
        self.Index_Symbol_0.setObjectName("Index_Symbol_0")
        self.Index_Percentage_0 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Percentage_0.setGeometry(QtCore.QRect(170, 50, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Index_Percentage_0.setFont(font)
        self.Index_Percentage_0.setObjectName("Index_Percentage_0")
        self.Index_Price_0 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Price_0.setGeometry(QtCore.QRect(230, 10, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.Index_Price_0.setFont(font)
        self.Index_Price_0.setObjectName("Index_Price_0")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(160, 10, 3, 61))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(290, 10, 3, 61))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.Index_Symbol_1 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Symbol_1.setGeometry(QtCore.QRect(300, 10, 61, 20))
        self.Index_Symbol_1.setObjectName("Index_Symbol_1")
        self.Index_Percentage_1 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Percentage_1.setGeometry(QtCore.QRect(300, 50, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Index_Percentage_1.setFont(font)
        self.Index_Percentage_1.setObjectName("Index_Percentage_1")
        self.Index_Price_1 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Price_1.setGeometry(QtCore.QRect(360, 10, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.Index_Price_1.setFont(font)
        self.Index_Price_1.setObjectName("Index_Price_1")
        self.Index_Percentage_2 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Percentage_2.setGeometry(QtCore.QRect(430, 50, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Index_Percentage_2.setFont(font)
        self.Index_Percentage_2.setObjectName("Index_Percentage_2")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(410, 10, 3, 61))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.Index_Symbol_2 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Symbol_2.setGeometry(QtCore.QRect(430, 10, 61, 20))
        self.Index_Symbol_2.setObjectName("Index_Symbol_2")
        self.Index_Price_2 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Price_2.setGeometry(QtCore.QRect(490, 10, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.Index_Price_2.setFont(font)
        self.Index_Price_2.setObjectName("Index_Price_2")
        self.Index_Percentage_3 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Percentage_3.setGeometry(QtCore.QRect(550, 50, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Index_Percentage_3.setFont(font)
        self.Index_Percentage_3.setObjectName("Index_Percentage_3")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(540, 10, 3, 61))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.Index_Symbol_3 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Symbol_3.setGeometry(QtCore.QRect(550, 10, 61, 20))
        self.Index_Symbol_3.setObjectName("Index_Symbol_3")
        self.Index_Price_3 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Price_3.setGeometry(QtCore.QRect(610, 10, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.Index_Price_3.setFont(font)
        self.Index_Price_3.setObjectName("Index_Price_3")
        self.Index_Percentage_4 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Percentage_4.setGeometry(QtCore.QRect(670, 50, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Index_Percentage_4.setFont(font)
        self.Index_Percentage_4.setObjectName("Index_Percentage_4")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(660, 10, 3, 61))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.Index_Symbol_4 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Symbol_4.setGeometry(QtCore.QRect(670, 10, 61, 20))
        self.Index_Symbol_4.setObjectName("Index_Symbol_4")
        self.Index_Price_4 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Price_4.setGeometry(QtCore.QRect(730, 10, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.Index_Price_4.setFont(font)
        self.Index_Price_4.setObjectName("Index_Price_4")
        self.Index_Percentage_5 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Percentage_5.setGeometry(QtCore.QRect(790, 50, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Index_Percentage_5.setFont(font)
        self.Index_Percentage_5.setObjectName("Index_Percentage_5")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(780, 10, 3, 61))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.Index_Symbol_5 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Symbol_5.setGeometry(QtCore.QRect(790, 10, 61, 20))
        self.Index_Symbol_5.setObjectName("Index_Symbol_5")
        self.Index_Price_5 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Price_5.setGeometry(QtCore.QRect(850, 10, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.Index_Price_5.setFont(font)
        self.Index_Price_5.setObjectName("Index_Price_5")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 70, 1024, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(900, 10, 3, 61))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.Index_Percentage_6 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Percentage_6.setGeometry(QtCore.QRect(910, 50, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Index_Percentage_6.setFont(font)
        self.Index_Percentage_6.setObjectName("Index_Percentage_6")
        self.Index_Symbol_6 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Symbol_6.setGeometry(QtCore.QRect(910, 10, 61, 20))
        self.Index_Symbol_6.setObjectName("Index_Symbol_6")
        self.Index_Price_6 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Price_6.setGeometry(QtCore.QRect(970, 10, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.Index_Price_6.setFont(font)
        self.Index_Price_6.setObjectName("Index_Price_6")
        self.Index_Name_0 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Name_0.setGeometry(QtCore.QRect(170, 32, 111, 21))
        self.Index_Name_0.setObjectName("Index_Name_0")
        self.Index_Name_1 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Name_1.setGeometry(QtCore.QRect(300, 32, 111, 21))
        self.Index_Name_1.setObjectName("Index_Name_1")
        self.Index_Name_2 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Name_2.setGeometry(QtCore.QRect(430, 32, 111, 21))
        self.Index_Name_2.setObjectName("Index_Name_2")
        self.Index_Name_3 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Name_3.setGeometry(QtCore.QRect(550, 32, 111, 21))
        self.Index_Name_3.setObjectName("Index_Name_3")
        self.Index_Name_4 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Name_4.setGeometry(QtCore.QRect(670, 32, 111, 21))
        self.Index_Name_4.setObjectName("Index_Name_4")
        self.Index_Name_5 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Name_5.setGeometry(QtCore.QRect(790, 32, 111, 21))
        self.Index_Name_5.setObjectName("Index_Name_5")
        self.Index_Name_6 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Name_6.setGeometry(QtCore.QRect(910, 32, 111, 21))
        self.Index_Name_6.setObjectName("Index_Name_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.timer_painter = QtCore.QTimer()
        self.timer_painter.timeout.connect(self.UpdateTime)
        self.timer_painter.start(1000)

        self.UpdateBanner()

        self.stock_update_timer = QtCore.QTimer()
        self.stock_update_timer.timeout.connect(self.UpdateBanner)
        self.stock_update_timer.start(10000)



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Will\'s Stock Screener"))
        self.TimeNow_Label.setText(_translate("MainWindow", "TimeNow_Label"))
        self.DateNow_Label.setText(_translate("MainWindow", "Datenow_Label"))
        self.Index_Symbol_0.setText(_translate("MainWindow", "Index0"))
        self.Index_Percentage_0.setText(_translate("MainWindow", "Index_%"))
        self.Index_Price_0.setText(_translate("MainWindow", "Index_P_0"))
        self.Index_Symbol_1.setText(_translate("MainWindow", "Index1"))
        self.Index_Percentage_1.setText(_translate("MainWindow", "Index_%"))
        self.Index_Price_1.setText(_translate("MainWindow", "Index_P"))
        self.Index_Percentage_2.setText(_translate("MainWindow", "Index_%"))
        self.Index_Symbol_2.setText(_translate("MainWindow", "Index2"))
        self.Index_Price_2.setText(_translate("MainWindow", "Index_P"))
        self.Index_Percentage_3.setText(_translate("MainWindow", "Index_%"))
        self.Index_Symbol_3.setText(_translate("MainWindow", "Index3"))
        self.Index_Price_3.setText(_translate("MainWindow", "Index_P"))
        self.Index_Percentage_4.setText(_translate("MainWindow", "Index_%"))
        self.Index_Symbol_4.setText(_translate("MainWindow", "Index4"))
        self.Index_Price_4.setText(_translate("MainWindow", "Index_P"))
        self.Index_Percentage_5.setText(_translate("MainWindow", "Index_%"))
        self.Index_Symbol_5.setText(_translate("MainWindow", "Index5"))
        self.Index_Price_5.setText(_translate("MainWindow", "Index_P"))
        self.Index_Percentage_6.setText(_translate("MainWindow", "Index_%"))
        self.Index_Symbol_6.setText(_translate("MainWindow", "Index6"))
        self.Index_Price_6.setText(_translate("MainWindow", "Index_P"))
        self.Index_Name_0.setText(_translate("MainWindow", "Index_Name_0"))
        self.Index_Name_1.setText(_translate("MainWindow", "Index_Name_1"))
        self.Index_Name_2.setText(_translate("MainWindow", "Index_Name_2"))
        self.Index_Name_3.setText(_translate("MainWindow", "Index_Name_3"))
        self.Index_Name_4.setText(_translate("MainWindow", "Index_Name_4"))
        self.Index_Name_5.setText(_translate("MainWindow", "Index_Name_5"))
        self.Index_Name_6.setText(_translate("MainWindow", "Index_Name_6"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
