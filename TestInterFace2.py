# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface_Workfile.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import requests,json

alpha_vantage_api_key = "4NE2ALTFPGT83V3S"

class Ui_MainWindow(object):

    def UpdateTime(self):
        current_time = datetime.now()
        # To Debug the current time
        # print(current_time.strftime("%H:%M:%S"))

        # Update the text label with current time
        self.TimeNow_Label.setText(current_time.strftime("%H:%M:%S"))
        self.DateNow_Label.setText(current_time.strftime("%b %d %Y"))

    def UpdateIndces(self):
        url = "https://financialmodelingprep.com/api/v3/majors-indexes"
        session = requests.session()
        request = session.get(url, timeout=15)
        result = request.json()

        # Populate index 0 for symbols
        self.Index_Symbol_0.setText(result["Global Quote"]['01. symbol'])
        # Populate percentage changed for closing price
        self.Index_Percentage_0.setText(result["Global Quote"]['10. change percent'])
        # Populate price of current quote
        self.Index_Price_0.setText(result["Global Quote"]['05. price'])

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1024, 768)
        MainWindow.setMouseTracking(False)
        MainWindow.setAcceptDrops(False)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 1024, 50))
        self.line.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.line.setAutoFillBackground(False)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
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
        self.DateNow_Label.setGeometry(QtCore.QRect(0, 10, 161, 31))
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
        self.Index_Percentage_0.setGeometry(QtCore.QRect(170, 40, 100, 31))
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.timer_painter = QtCore.QTimer()
        self.timer_painter.timeout.connect(self.UpdateTime)
        self.timer_painter.start(1000)

        self.stock_update_timer = QtCore.QTimer()
        self.stock_update_timer.timeout.connect(self.UpdateIndces)
        self.stock_update_timer.start(30000)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.UpdateIndces()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Will\'s Stock Screener"))
        self.TimeNow_Label.setText(_translate("MainWindow", "TimeNow_Label"))
        self.DateNow_Label.setText(_translate("MainWindow", "Datenow_Label"))
        self.Index_Symbol_0.setText(_translate("MainWindow", "Index1"))
        self.Index_Percentage_0.setText(_translate("MainWindow", "Index_%"))
        self.Index_Price_0.setText(_translate("MainWindow", "Index_P"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())