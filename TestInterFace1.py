# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface_Workfile.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import threading
import time
from datetime import datetime

class Ui_MainWindow(object):

    def UpdateTime(self):
        current_time = datetime.now()
        # To Debug the current time
        # print(current_time.strftime("%H:%M:%S"))

        # Update the text label with current time
        self.TimeNow_Label.setText(current_time.strftime("%b %d %Y %H:%M:%S"))

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
        self.TimeNow_Label.setGeometry(QtCore.QRect(0, 0, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(15)

        self.TimeNow_Label.setFont(font)
        self.TimeNow_Label.setMouseTracking(False)
        self.TimeNow_Label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TimeNow_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.TimeNow_Label.setWordWrap(True)
        self.TimeNow_Label.setObjectName("TimeNow_Label")

        MainWindow.setCentralWidget(self.centralwidget)

        self.timer_painter = QtCore.QTimer()
        self.timer_painter.timeout.connect(self.UpdateTime)
        self.timer_painter.start(1000)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Will\'s Stock Screener"))
        self.TimeNow_Label.setText(_translate("MainWindow", "TimeNow_Label"))
        self.Test_Label.setText(_translate("MainWindow", "TextLabel"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

