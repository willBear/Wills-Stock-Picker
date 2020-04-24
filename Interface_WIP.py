# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface_Workfile.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import requests, json
import urllib
alpha_vantage_api_key = "4NE2ALTFPGT83V3S"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1024, 768)
        MainWindow.setMouseTracking(False)
        MainWindow.setAcceptDrops(False)
        MainWindow.setAccessibleName("")
        MainWindow.setAccessibleDescription("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TimeNow_Label = QtWidgets.QLabel(self.centralwidget)
        self.TimeNow_Label.setGeometry(QtCore.QRect(5, 32, 90, 21))
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
        self.DateNow_Label.setGeometry(QtCore.QRect(5, 10, 90, 21))
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
        self.Index_Symbol_0.setGeometry(QtCore.QRect(100, 10, 40, 20))
        self.Index_Symbol_0.setObjectName("Index_Symbol_0")
        self.Index_Percentage_0 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Percentage_0.setGeometry(QtCore.QRect(100, 55, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Index_Percentage_0.setFont(font)
        self.Index_Percentage_0.setObjectName("Index_Percentage_0")
        self.Index_Price_0 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Price_0.setGeometry(QtCore.QRect(185, 10, 45, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.Index_Price_0.setFont(font)
        self.Index_Price_0.setObjectName("Index_Price_0")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(95, 10, 3, 61))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(230, 10, 3, 61))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.Index_Symbol_1 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Symbol_1.setGeometry(QtCore.QRect(235, 10, 40, 20))
        self.Index_Symbol_1.setObjectName("Index_Symbol_1")
        self.Index_Percentage_1 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Percentage_1.setGeometry(QtCore.QRect(235, 55, 50, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Index_Percentage_1.setFont(font)
        self.Index_Percentage_1.setObjectName("Index_Percentage_1")
        self.Index_Price_1 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Price_1.setGeometry(QtCore.QRect(320, 10, 45, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.Index_Price_1.setFont(font)
        self.Index_Price_1.setObjectName("Index_Price_1")
        self.Index_Percentage_2 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Percentage_2.setGeometry(QtCore.QRect(370, 55, 50, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Index_Percentage_2.setFont(font)
        self.Index_Percentage_2.setObjectName("Index_Percentage_2")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(365, 10, 3, 61))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.Index_Symbol_2 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Symbol_2.setGeometry(QtCore.QRect(370, 10, 40, 20))
        self.Index_Symbol_2.setObjectName("Index_Symbol_2")
        self.Index_Price_2 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Price_2.setGeometry(QtCore.QRect(450, 10, 45, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.Index_Price_2.setFont(font)
        self.Index_Price_2.setObjectName("Index_Price_2")
        self.Index_Percentage_3 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Percentage_3.setGeometry(QtCore.QRect(505, 55, 50, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Index_Percentage_3.setFont(font)
        self.Index_Percentage_3.setObjectName("Index_Percentage_3")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(500, 10, 3, 61))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.Index_Symbol_3 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Symbol_3.setGeometry(QtCore.QRect(505, 10, 40, 20))
        self.Index_Symbol_3.setObjectName("Index_Symbol_3")
        self.Index_Price_3 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Price_3.setGeometry(QtCore.QRect(590, 10, 45, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.Index_Price_3.setFont(font)
        self.Index_Price_3.setObjectName("Index_Price_3")
        self.Index_Percentage_4 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Percentage_4.setGeometry(QtCore.QRect(640, 55, 50, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Index_Percentage_4.setFont(font)
        self.Index_Percentage_4.setObjectName("Index_Percentage_4")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(635, 10, 3, 61))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.Index_Symbol_4 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Symbol_4.setGeometry(QtCore.QRect(640, 10, 40, 20))
        self.Index_Symbol_4.setObjectName("Index_Symbol_4")
        self.Index_Price_4 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Price_4.setGeometry(QtCore.QRect(725, 10, 45, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.Index_Price_4.setFont(font)
        self.Index_Price_4.setObjectName("Index_Price_4")
        self.Index_Percentage_5 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Percentage_5.setGeometry(QtCore.QRect(775, 55, 50, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Index_Percentage_5.setFont(font)
        self.Index_Percentage_5.setObjectName("Index_Percentage_5")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(770, 10, 3, 61))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.Index_Symbol_5 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Symbol_5.setGeometry(QtCore.QRect(775, 10, 40, 20))
        self.Index_Symbol_5.setObjectName("Index_Symbol_5")
        self.Index_Price_5 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Price_5.setGeometry(QtCore.QRect(860, 10, 45, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.Index_Price_5.setFont(font)
        self.Index_Price_5.setObjectName("Index_Price_5")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 75, 1024, 5))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(905, 10, 3, 61))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.Index_Percentage_6 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Percentage_6.setGeometry(QtCore.QRect(910, 55, 50, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Index_Percentage_6.setFont(font)
        self.Index_Percentage_6.setObjectName("Index_Percentage_6")
        self.Index_Symbol_6 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Symbol_6.setGeometry(QtCore.QRect(910, 10, 40, 20))
        self.Index_Symbol_6.setObjectName("Index_Symbol_6")
        self.Index_Price_6 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Price_6.setGeometry(QtCore.QRect(980, 10, 45, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.Index_Price_6.setFont(font)
        self.Index_Price_6.setObjectName("Index_Price_6")
        self.Index_Name_0 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Name_0.setGeometry(QtCore.QRect(100, 32, 130, 21))
        self.Index_Name_0.setObjectName("Index_Name_0")
        self.Index_Name_1 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Name_1.setGeometry(QtCore.QRect(235, 32, 130, 21))
        self.Index_Name_1.setObjectName("Index_Name_1")
        self.Index_Name_2 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Name_2.setGeometry(QtCore.QRect(370, 32, 130, 21))
        self.Index_Name_2.setObjectName("Index_Name_2")
        self.Index_Name_3 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Name_3.setGeometry(QtCore.QRect(505, 32, 130, 21))
        self.Index_Name_3.setObjectName("Index_Name_3")
        self.Index_Name_4 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Name_4.setGeometry(QtCore.QRect(640, 32, 130, 21))
        self.Index_Name_4.setObjectName("Index_Name_4")
        self.Index_Name_5 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Name_5.setGeometry(QtCore.QRect(775, 32, 130, 21))
        self.Index_Name_5.setObjectName("Index_Name_5")
        self.Index_Name_6 = QtWidgets.QLabel(self.centralwidget)
        self.Index_Name_6.setGeometry(QtCore.QRect(910, 32, 130, 21))
        self.Index_Name_6.setObjectName("Index_Name_6")
        self.Sector_Name_0 = QtWidgets.QLabel(self.centralwidget)
        self.Sector_Name_0.setGeometry(QtCore.QRect(14, 710, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Sector_Name_0.setFont(font)
        self.Sector_Name_0.setObjectName("Sector_Name_0")
        self.Sector_Percentage_0 = QtWidgets.QLabel(self.centralwidget)
        self.Sector_Percentage_0.setGeometry(QtCore.QRect(154, 710, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Sector_Percentage_0.setFont(font)
        self.Sector_Percentage_0.setObjectName("Sector_Percentage_0")
        self.Sector_Percentage_1 = QtWidgets.QLabel(self.centralwidget)
        self.Sector_Percentage_1.setGeometry(QtCore.QRect(154, 740, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Sector_Percentage_1.setFont(font)
        self.Sector_Percentage_1.setObjectName("Sector_Percentage_1")
        self.Sector_Name_1 = QtWidgets.QLabel(self.centralwidget)
        self.Sector_Name_1.setGeometry(QtCore.QRect(14, 740, 39, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Sector_Name_1.setFont(font)
        self.Sector_Name_1.setObjectName("Sector_Name_1")
        self.Sector_Percentage_2 = QtWidgets.QLabel(self.centralwidget)
        self.Sector_Percentage_2.setGeometry(QtCore.QRect(364, 710, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Sector_Percentage_2.setFont(font)
        self.Sector_Percentage_2.setObjectName("Sector_Percentage_2")
        self.Sector_Name_2 = QtWidgets.QLabel(self.centralwidget)
        self.Sector_Name_2.setGeometry(QtCore.QRect(214, 710, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Sector_Name_2.setFont(font)
        self.Sector_Name_2.setObjectName("Sector_Name_2")
        self.Sector_Percentage_3 = QtWidgets.QLabel(self.centralwidget)
        self.Sector_Percentage_3.setGeometry(QtCore.QRect(364, 740, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Sector_Percentage_3.setFont(font)
        self.Sector_Percentage_3.setObjectName("Sector_Percentage_3")
        self.Sector_Name_3 = QtWidgets.QLabel(self.centralwidget)
        self.Sector_Name_3.setGeometry(QtCore.QRect(214, 740, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Sector_Name_3.setFont(font)
        self.Sector_Name_3.setObjectName("Sector_Name_3")
        self.Sector_Percentage_4 = QtWidgets.QLabel(self.centralwidget)
        self.Sector_Percentage_4.setGeometry(QtCore.QRect(564, 710, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Sector_Percentage_4.setFont(font)
        self.Sector_Percentage_4.setObjectName("Sector_Percentage_4")
        self.Sector_Name_4 = QtWidgets.QLabel(self.centralwidget)
        self.Sector_Name_4.setGeometry(QtCore.QRect(424, 710, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Sector_Name_4.setFont(font)
        self.Sector_Name_4.setObjectName("Sector_Name_4")
        self.Sector_Percentage_5 = QtWidgets.QLabel(self.centralwidget)
        self.Sector_Percentage_5.setGeometry(QtCore.QRect(564, 740, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Sector_Percentage_5.setFont(font)
        self.Sector_Percentage_5.setObjectName("Sector_Percentage_5")
        self.Sector_Name_5 = QtWidgets.QLabel(self.centralwidget)
        self.Sector_Name_5.setGeometry(QtCore.QRect(424, 740, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Sector_Name_5.setFont(font)
        self.Sector_Name_5.setObjectName("Sector_Name_5")
        self.Sector_Percentage_6 = QtWidgets.QLabel(self.centralwidget)
        self.Sector_Percentage_6.setGeometry(QtCore.QRect(764, 710, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Sector_Percentage_6.setFont(font)
        self.Sector_Percentage_6.setObjectName("Sector_Percentage_6")
        self.Sector_Name_6 = QtWidgets.QLabel(self.centralwidget)
        self.Sector_Name_6.setGeometry(QtCore.QRect(624, 710, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Sector_Name_6.setFont(font)
        self.Sector_Name_6.setObjectName("Sector_Name_6")
        self.Sector_Percentage_7 = QtWidgets.QLabel(self.centralwidget)
        self.Sector_Percentage_7.setGeometry(QtCore.QRect(764, 740, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Sector_Percentage_7.setFont(font)
        self.Sector_Percentage_7.setObjectName("Sector_Percentage_7")
        self.Sector_Name_7 = QtWidgets.QLabel(self.centralwidget)
        self.Sector_Name_7.setGeometry(QtCore.QRect(624, 740, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Sector_Name_7.setFont(font)
        self.Sector_Name_7.setObjectName("Sector_Name_7")
        self.Sector_Name_9 = QtWidgets.QLabel(self.centralwidget)
        self.Sector_Name_9.setGeometry(QtCore.QRect(824, 740, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Sector_Name_9.setFont(font)
        self.Sector_Name_9.setObjectName("Sector_Name_9")
        self.Sector_Percentage_9 = QtWidgets.QLabel(self.centralwidget)
        self.Sector_Percentage_9.setGeometry(QtCore.QRect(964, 740, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Sector_Percentage_9.setFont(font)
        self.Sector_Percentage_9.setObjectName("Sector_Percentage_9")
        self.Sector_Name_8 = QtWidgets.QLabel(self.centralwidget)
        self.Sector_Name_8.setGeometry(QtCore.QRect(824, 710, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Sector_Name_8.setFont(font)
        self.Sector_Name_8.setObjectName("Sector_Name_8")
        self.Sector_Percentage_8 = QtWidgets.QLabel(self.centralwidget)
        self.Sector_Percentage_8.setGeometry(QtCore.QRect(964, 710, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Sector_Percentage_8.setFont(font)
        self.Sector_Percentage_8.setObjectName("Sector_Percentage_8")
        self.Sector_Performance_Title = QtWidgets.QComboBox(self.centralwidget)
        self.Sector_Performance_Title.setGeometry(QtCore.QRect(780, 680, 231, 30))
        self.Sector_Performance_Title.setObjectName("Sector_Performance_Title")
        self.Sector_Performance_Title.addItem("")
        self.Sector_Performance_Title.addItem("")
        self.Sector_Performance_Title.addItem("")
        self.Sector_Performance_Title.addItem("")
        self.Sector_Performance_Title.addItem("")
        self.Sector_Performance_Title.addItem("")
        self.Sector_Performance_Title.addItem("")
        self.Sector_Performance_Title.addItem("")
        self.Sector_Performance_Title.addItem("")
        self.Sector_Performance_Title.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 680, 1024, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(5, 55, 90, 15))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.Search_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Search_Button.setGeometry(QtCore.QRect(105, 85, 25, 21))
        self.Search_Button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Search_Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Search_Button.setIcon(icon)
        self.Search_Button.setIconSize(QtCore.QSize(21, 21))
        self.Search_Button.setObjectName("Search_Button")
        self.Search_Bar = QtWidgets.QLineEdit(self.centralwidget)
        self.Search_Bar.setGeometry(QtCore.QRect(5, 85, 100, 21))
        self.Search_Bar.setObjectName("Search_Bar")
        self.Stock_Symbol = QtWidgets.QLabel(self.centralwidget)
        self.Stock_Symbol.setGeometry(QtCore.QRect(140, 85, 50, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Stock_Symbol.setFont(font)
        self.Stock_Symbol.setObjectName("Stock_Symbol")
        self.Description_Header = QtWidgets.QLabel(self.centralwidget)
        self.Description_Header.setGeometry(QtCore.QRect(140, 140, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Description_Header.setFont(font)
        self.Description_Header.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Description_Header.setObjectName("Description_Header")
        self.Description_Label = QtWidgets.QLabel(self.centralwidget)
        self.Description_Label.setGeometry(QtCore.QRect(140, 160, 371, 101))
        self.Description_Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Description_Label.setWordWrap(True)
        self.Description_Label.setObjectName("Description_Label")
        self.Company_Image = QtWidgets.QLabel(self.centralwidget)
        self.Company_Image.setGeometry(QtCore.QRect(5, 140, 100, 100))
        self.Company_Image.setScaledContents(True)
        self.Company_Image.setAlignment(QtCore.Qt.AlignCenter)
        self.Company_Image.setObjectName("Company_Image")
        self.Industry_Title = QtWidgets.QLabel(self.centralwidget)
        self.Industry_Title.setGeometry(QtCore.QRect(525, 160, 70, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Industry_Title.setFont(font)
        self.Industry_Title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Industry_Title.setObjectName("Industry_Title")
        self.Exchange_Title = QtWidgets.QLabel(self.centralwidget)
        self.Exchange_Title.setGeometry(QtCore.QRect(525, 180, 70, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Exchange_Title.setFont(font)
        self.Exchange_Title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Exchange_Title.setOpenExternalLinks(False)
        self.Exchange_Title.setObjectName("Exchange_Title")
        self.Industry_Label = QtWidgets.QLabel(self.centralwidget)
        self.Industry_Label.setGeometry(QtCore.QRect(600, 160, 200, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Industry_Label.setFont(font)
        self.Industry_Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Industry_Label.setObjectName("Industry_Label")
        self.Exchange_Label = QtWidgets.QLabel(self.centralwidget)
        self.Exchange_Label.setGeometry(QtCore.QRect(600, 180, 200, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Exchange_Label.setFont(font)
        self.Exchange_Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Exchange_Label.setObjectName("Exchange_Label")
        self.Stock_Price = QtWidgets.QLabel(self.centralwidget)
        self.Stock_Price.setGeometry(QtCore.QRect(215, 85, 50, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Stock_Price.setFont(font)
        self.Stock_Price.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Stock_Price.setObjectName("Stock_Price")
        self.Stock_Percentage_Change = QtWidgets.QLabel(self.centralwidget)
        self.Stock_Percentage_Change.setGeometry(QtCore.QRect(275, 85, 50, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Stock_Percentage_Change.setFont(font)
        self.Stock_Percentage_Change.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Stock_Percentage_Change.setObjectName("Stock_Percentage_Change")
        self.Stock_Volume = QtWidgets.QLabel(self.centralwidget)
        self.Stock_Volume.setGeometry(QtCore.QRect(670, 85, 125, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Stock_Volume.setFont(font)
        self.Stock_Volume.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Stock_Volume.setObjectName("Stock_Volume")
        self.Stock_Line_1 = QtWidgets.QFrame(self.centralwidget)
        self.Stock_Line_1.setGeometry(QtCore.QRect(0, 105, 1024, 5))
        self.Stock_Line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.Stock_Line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Stock_Line_1.setObjectName("Stock_Line_1")
        self.Stock_Line_2 = QtWidgets.QFrame(self.centralwidget)
        self.Stock_Line_2.setGeometry(QtCore.QRect(0, 130, 1024, 5))
        self.Stock_Line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.Stock_Line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Stock_Line_2.setObjectName("Stock_Line_2")
        self.Stock_Name = QtWidgets.QLabel(self.centralwidget)
        self.Stock_Name.setGeometry(QtCore.QRect(0, 110, 220, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Stock_Name.setFont(font)
        self.Stock_Name.setObjectName("Stock_Name")
        self.Stock_Name_Filler = QtWidgets.QLabel(self.centralwidget)
        self.Stock_Name_Filler.setGeometry(QtCore.QRect(220, 110, 804, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Stock_Name_Filler.setFont(font)
        self.Stock_Name_Filler.setText("")
        self.Stock_Name_Filler.setObjectName("Stock_Name_Filler")
        self.Stock_Market_Capitalization = QtWidgets.QLabel(self.centralwidget)
        self.Stock_Market_Capitalization.setGeometry(QtCore.QRect(800, 85, 140, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Stock_Market_Capitalization.setFont(font)
        self.Stock_Market_Capitalization.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Stock_Market_Capitalization.setObjectName("Stock_Market_Capitalization")
        self.Stock_Beta = QtWidgets.QLabel(self.centralwidget)
        self.Stock_Beta.setGeometry(QtCore.QRect(940, 85, 80, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Stock_Beta.setFont(font)
        self.Stock_Beta.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Stock_Beta.setObjectName("Stock_Beta")
        self.Stock_Open = QtWidgets.QLabel(self.centralwidget)
        self.Stock_Open.setGeometry(QtCore.QRect(340, 85, 100, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Stock_Open.setFont(font)
        self.Stock_Open.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Stock_Open.setObjectName("Stock_Open")
        self.Stock_High = QtWidgets.QLabel(self.centralwidget)
        self.Stock_High.setGeometry(QtCore.QRect(440, 85, 100, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Stock_High.setFont(font)
        self.Stock_High.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Stock_High.setObjectName("Stock_High")
        self.Stock_Low = QtWidgets.QLabel(self.centralwidget)
        self.Stock_Low.setGeometry(QtCore.QRect(540, 85, 100, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Stock_Low.setFont(font)
        self.Stock_Low.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Stock_Low.setObjectName("Stock_Low")
        self.label.raise_()
        self.TimeNow_Label.raise_()
        self.DateNow_Label.raise_()
        self.Index_Symbol_0.raise_()
        self.Index_Percentage_0.raise_()
        self.Index_Price_0.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.Index_Symbol_1.raise_()
        self.Index_Percentage_1.raise_()
        self.Index_Price_1.raise_()
        self.Index_Percentage_2.raise_()
        self.line_4.raise_()
        self.Index_Symbol_2.raise_()
        self.Index_Price_2.raise_()
        self.Index_Percentage_3.raise_()
        self.line_5.raise_()
        self.Index_Symbol_3.raise_()
        self.Index_Price_3.raise_()
        self.Index_Percentage_4.raise_()
        self.line_6.raise_()
        self.Index_Symbol_4.raise_()
        self.Index_Price_4.raise_()
        self.Index_Percentage_5.raise_()
        self.line_7.raise_()
        self.Index_Symbol_5.raise_()
        self.Index_Price_5.raise_()
        self.line.raise_()
        self.line_8.raise_()
        self.Index_Percentage_6.raise_()
        self.Index_Symbol_6.raise_()
        self.Index_Price_6.raise_()
        self.Index_Name_0.raise_()
        self.Index_Name_1.raise_()
        self.Index_Name_2.raise_()
        self.Index_Name_3.raise_()
        self.Index_Name_4.raise_()
        self.Index_Name_5.raise_()
        self.Index_Name_6.raise_()
        self.Sector_Name_0.raise_()
        self.Sector_Percentage_0.raise_()
        self.Sector_Percentage_1.raise_()
        self.Sector_Name_1.raise_()
        self.Sector_Percentage_2.raise_()
        self.Sector_Name_2.raise_()
        self.Sector_Percentage_3.raise_()
        self.Sector_Name_3.raise_()
        self.Sector_Percentage_4.raise_()
        self.Sector_Name_4.raise_()
        self.Sector_Percentage_5.raise_()
        self.Sector_Name_5.raise_()
        self.Sector_Percentage_6.raise_()
        self.Sector_Name_6.raise_()
        self.Sector_Percentage_7.raise_()
        self.Sector_Name_7.raise_()
        self.Sector_Name_9.raise_()
        self.Sector_Percentage_9.raise_()
        self.Sector_Name_8.raise_()
        self.Sector_Percentage_8.raise_()
        self.Sector_Performance_Title.raise_()
        self.label_2.raise_()
        self.Search_Button.raise_()
        self.Search_Bar.raise_()
        self.Stock_Symbol.raise_()
        self.Description_Header.raise_()
        self.Description_Label.raise_()
        self.Company_Image.raise_()
        self.Industry_Title.raise_()
        self.Exchange_Title.raise_()
        self.Industry_Label.raise_()
        self.Exchange_Label.raise_()
        self.Stock_Price.raise_()
        self.Stock_Percentage_Change.raise_()
        self.Stock_Volume.raise_()
        self.Stock_Line_1.raise_()
        self.Stock_Line_2.raise_()
        self.Stock_Name.raise_()
        self.Stock_Name_Filler.raise_()
        self.Stock_Market_Capitalization.raise_()
        self.Stock_Beta.raise_()
        self.Stock_Open.raise_()
        self.Stock_High.raise_()
        self.Stock_Low.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        # Set the visibility of the widgets to 0 when we initialize
        Stock_Widgets = [self.Company_Image, self.Stock_Symbol,self.Stock_Name,self.Stock_Price,self.Stock_Percentage_Change,
                         self.Stock_Open,self.Stock_High,self.Stock_Low,self.Stock_Volume,self.Stock_Market_Capitalization,
                         self.Stock_Beta,self.Company_Image,self.Stock_Line_1,self.Stock_Line_2,self.Description_Label,
                         self.Description_Header,self.Industry_Label,self.Industry_Title,self.Exchange_Label,self.Exchange_Title]

        for widget in Stock_Widgets:
            widget.setVisible(False)

        # Whenever the search button is pressed, we would run the search stocks function
        self.Search_Button.clicked.connect(self.Search_Stocks)

        # We have a timer that updates every second and updates the current time of the clock
        self.timer_painter = QtCore.QTimer()
        self.timer_painter.timeout.connect(self.UpdateTime)
        self.timer_painter.start(1000)

        # Set up another timer that updates all the banner indices
        self.stock_update_timer = QtCore.QTimer()
        self.stock_update_timer.timeout.connect(self.UpdateBanner)
        self.stock_update_timer.start(10000)

        # Singleshot Timers that sets up a timer and populates all formation, timed loop updates are then followed
        QtCore.QTimer.singleShot(1000, self.UpdateBanner)
        QtCore.QTimer.singleShot(1000, self.PopulateSectorPerformances)

        # Whenever the index of the performance title is changed, we would run populate Sector Performances Function
        self.Sector_Performance_Title.currentIndexChanged.connect(self.PopulateSectorPerformances)
        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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

    def Search_Stocks(self):

        # Get rid of white spaces if there are any
        ticker_string = self.Search_Bar.text()
        ticker_string = ticker_string.strip()

        # Group the widgets together in an array so we can group set its visibility status
        Stock_Widgets = [self.Company_Image, self.Stock_Symbol,self.Stock_Name,self.Stock_Price,self.Stock_Percentage_Change,
                         self.Stock_Open,self.Stock_High,self.Stock_Low,self.Stock_Volume,self.Stock_Market_Capitalization,
                         self.Stock_Beta,self.Company_Image,self.Stock_Line_1,self.Stock_Line_2,self.Description_Label,
                         self.Description_Header,self.Industry_Label,self.Industry_Title,self.Exchange_Label,self.Exchange_Title]

        url = "https://financialmodelingprep.com/api/v3/company/profile/" + ticker_string
        session = requests.session()
        request = session.get(url, timeout=5)
        company_data = request.json()

        quote_url = "https://financialmodelingprep.com/api/v3/quote/" + ticker_string
        session = requests.session()
        request = session.get(quote_url, timeout=5)
        quote_data = request.json()
        # We now need to test the integrity of the data that we have received. We check for the amount of dictionary
        # pairs in the returned message, if it has less than 2 key-value pairs, we would throw message
        print(company_data)
        print('\n')
        print(quote_data)
        print(len(quote_data))
        print(quote_data[0]['dayLow'])

        if len(company_data) < 2:
            return

        # We do some parsing of the company data
        company_profile = company_data['profile']
        self.Stock_Name.setText('  ' + str(company_profile['companyName']))
        self.Stock_Symbol.setText(company_data['symbol'])
        self.Description_Label.setText(company_profile['description'])

        # Take the Image URL from information passed down from Financial Modelling Prep
        image_url = company_profile['image']

        # We would use the URL module and read the image file, convert it to byte
        data = urllib.request.urlopen(image_url).read()
        image = QtGui.QImage()
        image.loadFromData(data)

        # We set the company image to have the converted image
        self.Company_Image.setPixmap(QtGui.QPixmap(image))

        self.Stock_Price.setText(str(company_profile['price']))

        percentage_change = company_profile['changesPercentage']
        percentage_change = percentage_change[1:-1]
        self.Stock_Percentage_Change.setText(percentage_change)

        self.Stock_Volume.setText('Vol: '+ company_profile['volAvg'])
        self.Stock_Low.setText('L: ' + str(quote_data[0]['dayLow']))
        self.Stock_High.setText('H: ' + str(quote_data[0]['dayHigh']))
        self.Stock_Open.setText('O: ' + str(quote_data[0]['open']))
        beta = company_profile['beta']
        beta = beta[0:4]

        self.Stock_Beta.setText('Beta: '+ beta)
        print(type(company_profile['mktCap']))
        self.Stock_Market_Capitalization.setText(company_profile['mktCap'])
        self.Exchange_Label.setText(company_profile['exchange'])
        self.Industry_Label.setText(company_profile['industry'])


        # Now since all the data has been loaded, we would set the visibility of all widgets to be visible
        for widget in Stock_Widgets:
            widget.show()

        self.Stock_Name.setStyleSheet('Background:BROWN;Color:WHITE')
        self.Stock_Name_Filler.setStyleSheet('Background:GREEN')

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
        # WTI - Crude Oil Index
        # -------------------------------------------------------------------
        banner_indices = ['SPY', 'QQQ', 'IWM', 'DIA', '^VIX', 'GLD', 'WTI']

        # Iterate through the array of tickers and add it to the quote string
        # We are requesting multiple quotes from
        quote_string = ','.join(banner_indices)

        # The URL that we will concatenate with quote_string, makes the request
        # and stores the result into closing_price_data
        url = "https://financialmodelingprep.com/api/v3/quote/" + quote_string
        session = requests.session()
        request = session.get(url, timeout=5)
        closing_price_data = request.json()

        # Add the all widgets into an array t=
        colour_change_widgets = [self.Index_Percentage_0, self.Index_Percentage_1, self.Index_Percentage_2,
                                 self.Index_Percentage_3,
                                 self.Index_Percentage_4, self.Index_Percentage_5, self.Index_Percentage_6]

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

        # Go through every single percentage changed that needs colour adjusted and make red for losses
        # and green for anything that's above 0.00%
        for w in colour_change_widgets:
            if '-' in w.text():
                w.setStyleSheet("color:red")
            else:
                w.setStyleSheet("color:green")

    # -------------------------------------------------------------------
    # Function Name: PopulateSectorPerformances
    #
    # Description: This function is called to populate the performances of
    #              each sector performance in real time
    #
    # TODO:
    # Change colour based on the percentaged changed being + or -
    # Background colour flash for every update
    # Improve mass updating of banners to shave processing time
    # -------------------------------------------------------------------

    def PopulateSectorPerformances(self):
        # Fetch Real Time Data and Stores Previous Day Price
        # -------------------------------------------------------------------
        # Sectors Interested:
        # Slot 0 - Consumer Discretionary
        # Slot 1 - Energy
        # Slot 2 - Communication Services
        # Slot 3 - Information Technology
        # Slot 4 - Consumer Staples
        # Slot 5 - Health Care
        # Slot 6 - Materials
        # Slot 7 - Utilities
        # Slot 8 - Industrials
        # Slot 9 - Financials
        # Based on the selected index of the performance, we would update the
        # titles and data associated with the sector performance
        # -------------------------------------------------------------------
        print("The index changed is: " + str(self.Sector_Performance_Title.currentIndex()))

        sector_indices = ['Consumer Discretionary', 'Energy', 'Communication Services', 'Information Technology',
                          'Consumer Staples', 'Health Care', 'Materials', 'Utilities', 'Industrials', 'Financials']

        # This index maps the timeline to the dictionary passed by the json requests by alpha vantage
        timeline_indice = ['Rank A: Real-Time Performance', 'Rank B: 1 Day Performance', 'Rank C: 5 Day Performance',
                           'Rank D: 1 Month Performance', 'Rank E: 3 Month Performance',
                           'Rank F: Year-to-Date (YTD) Performance',
                           'Rank G: 1 Year Performance', 'Rank H: 3 Year Performance', 'Rank I: 5 Year Performance',
                           'Rank J: 10 Year Performance']

        colour_change_widgets = [self.Sector_Percentage_0, self.Sector_Percentage_1, self.Sector_Percentage_2,
                                 self.Sector_Percentage_3,
                                 self.Sector_Percentage_4, self.Sector_Percentage_5, self.Sector_Percentage_6,
                                 self.Sector_Percentage_7,
                                 self.Sector_Percentage_8, self.Sector_Percentage_9]

        # base_url variable that stores the base url
        base_url = "https://www.alphavantage.co/query?function=SECTOR"

        # main_url variable that stores complete url with API key
        main_url = base_url + "&apikey=" + alpha_vantage_api_key

        # get method of requests module
        # return response object
        req_ob = requests.get(main_url)

        # result contains list of nested dictionaries
        result = req_ob.json()

        parsed_dictionary = result[timeline_indice[self.Sector_Performance_Title.currentIndex()]]

        for key in parsed_dictionary:
            if key == sector_indices[0]:
                self.Sector_Name_0.setText(key)
                self.Sector_Percentage_0.setText(parsed_dictionary[key])
            elif key == sector_indices[1]:
                self.Sector_Name_1.setText(key)
                self.Sector_Percentage_1.setText(parsed_dictionary[key])
            elif key == sector_indices[2]:
                self.Sector_Name_2.setText(key)
                self.Sector_Percentage_2.setText(parsed_dictionary[key])
            elif key == sector_indices[3]:
                self.Sector_Name_3.setText(key)
                self.Sector_Percentage_3.setText(parsed_dictionary[key])
            elif key == sector_indices[4]:
                self.Sector_Name_4.setText(key)
                self.Sector_Percentage_4.setText(parsed_dictionary[key])
            elif key == sector_indices[5]:
                self.Sector_Name_5.setText(key)
                self.Sector_Percentage_5.setText(parsed_dictionary[key])
            elif key == sector_indices[6]:
                self.Sector_Name_6.setText(key)
                self.Sector_Percentage_6.setText(parsed_dictionary[key])
            elif key == sector_indices[7]:
                self.Sector_Name_7.setText(key)
                self.Sector_Percentage_7.setText(parsed_dictionary[key])
            elif key == sector_indices[8]:
                self.Sector_Name_8.setText(key)
                self.Sector_Percentage_8.setText(parsed_dictionary[key])
            elif key == sector_indices[9]:
                self.Sector_Name_9.setText(key)
                self.Sector_Percentage_9.setText(parsed_dictionary[key])

        for w in colour_change_widgets:
            if '-' in w.text():
                w.setStyleSheet("color:red")
            else:
                w.setStyleSheet("color:green")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Will\'s Stock Screener"))
        self.TimeNow_Label.setText(_translate("MainWindow", "00:00:00"))
        self.DateNow_Label.setText(_translate("MainWindow", "Apr 14 2020"))
        self.Index_Symbol_0.setText(_translate("MainWindow", "SPY"))
        self.Index_Percentage_0.setText(_translate("MainWindow", "-0.00%"))
        self.Index_Price_0.setText(_translate("MainWindow", "100.00"))
        self.Index_Symbol_1.setText(_translate("MainWindow", "QQQ"))
        self.Index_Percentage_1.setText(_translate("MainWindow", "-0.00%"))
        self.Index_Price_1.setText(_translate("MainWindow", "100.00"))
        self.Index_Percentage_2.setText(_translate("MainWindow", "-0.00%"))
        self.Index_Symbol_2.setText(_translate("MainWindow", "IWM"))
        self.Index_Price_2.setText(_translate("MainWindow", "100.00"))
        self.Index_Percentage_3.setText(_translate("MainWindow", "-0.00%"))
        self.Index_Symbol_3.setText(_translate("MainWindow", "DIA"))
        self.Index_Price_3.setText(_translate("MainWindow", "100.00"))
        self.Index_Percentage_4.setText(_translate("MainWindow", "-0.00%"))
        self.Index_Symbol_4.setText(_translate("MainWindow", "^VIX"))
        self.Index_Price_4.setText(_translate("MainWindow", "100.00"))
        self.Index_Percentage_5.setText(_translate("MainWindow", "-0.00%"))
        self.Index_Symbol_5.setText(_translate("MainWindow", "GLD"))
        self.Index_Price_5.setText(_translate("MainWindow", "100.00"))
        self.Index_Percentage_6.setText(_translate("MainWindow", "-0.00%"))
        self.Index_Symbol_6.setText(_translate("MainWindow", "WTI"))
        self.Index_Price_6.setText(_translate("MainWindow", "100.00"))
        self.Index_Name_0.setText(_translate("MainWindow", "S&P 500 ETF Trust"))
        self.Index_Name_1.setText(_translate("MainWindow", "QQQ Trust"))
        self.Index_Name_2.setText(_translate("MainWindow", "Russell 2000 ETF"))
        self.Index_Name_3.setText(_translate("MainWindow", "Dow Jones Industrial"))
        self.Index_Name_4.setText(_translate("MainWindow", "Volatility Index"))
        self.Index_Name_5.setText(_translate("MainWindow", "Gold Shares"))
        self.Index_Name_6.setText(_translate("MainWindow", "Offshore, Inc."))
        self.Sector_Name_0.setText(_translate("MainWindow", "Consumer Discretionary"))
        self.Sector_Percentage_0.setText(_translate("MainWindow", "-0.00%"))
        self.Sector_Percentage_1.setText(_translate("MainWindow", "-0.00%"))
        self.Sector_Name_1.setText(_translate("MainWindow", "Energy"))
        self.Sector_Percentage_2.setText(_translate("MainWindow", "-0.00%"))
        self.Sector_Name_2.setText(_translate("MainWindow", "Communication Services"))
        self.Sector_Percentage_3.setText(_translate("MainWindow", "-0.00%"))
        self.Sector_Name_3.setText(_translate("MainWindow", "Information Technology"))
        self.Sector_Percentage_4.setText(_translate("MainWindow", "-0.00%"))
        self.Sector_Name_4.setText(_translate("MainWindow", "Consumer Staples"))
        self.Sector_Percentage_5.setText(_translate("MainWindow", "-0.00%"))
        self.Sector_Name_5.setText(_translate("MainWindow", "Health Care"))
        self.Sector_Percentage_6.setText(_translate("MainWindow", "-0.00%"))
        self.Sector_Name_6.setText(_translate("MainWindow", "Materials"))
        self.Sector_Percentage_7.setText(_translate("MainWindow", "-0.00%"))
        self.Sector_Name_7.setText(_translate("MainWindow", "Utilities"))
        self.Sector_Name_9.setText(_translate("MainWindow", "Financials"))
        self.Sector_Percentage_9.setText(_translate("MainWindow", "-0.00%"))
        self.Sector_Name_8.setText(_translate("MainWindow", "Industrials"))
        self.Sector_Percentage_8.setText(_translate("MainWindow", "-0.00%"))
        self.Sector_Performance_Title.setItemText(0, _translate("MainWindow", "Real-Time Performance"))
        self.Sector_Performance_Title.setItemText(1, _translate("MainWindow", "1 Day Performance"))
        self.Sector_Performance_Title.setItemText(2, _translate("MainWindow", "5 Day Performance"))
        self.Sector_Performance_Title.setItemText(3, _translate("MainWindow", "1 Month Performance"))
        self.Sector_Performance_Title.setItemText(4, _translate("MainWindow", "3 Month Performance"))
        self.Sector_Performance_Title.setItemText(5, _translate("MainWindow", "Year-to-Date (YTD) Performance"))
        self.Sector_Performance_Title.setItemText(6, _translate("MainWindow", "1 Year Performance"))
        self.Sector_Performance_Title.setItemText(7, _translate("MainWindow", "3 Year Performance"))
        self.Sector_Performance_Title.setItemText(8, _translate("MainWindow", "5 Year Performance"))
        self.Sector_Performance_Title.setItemText(9, _translate("MainWindow", "10 Year Performance"))
        self.label.setText(_translate("MainWindow", "Sector Performance"))
        self.label_2.setText(_translate("MainWindow", "Open"))
        self.Search_Bar.setPlaceholderText(_translate("MainWindow", "Tickers..."))
        self.Stock_Symbol.setText(_translate("MainWindow", "AAPL"))
        self.Description_Header.setText(_translate("MainWindow", "Description:"))
        self.Description_Label.setText(_translate("MainWindow", "Apple Inc is designs, manufactures and markets mobile communication and media devices and personal computers, and sells a variety of related software, services, accessories, networking solutions and third-party digital content and applications."))
        self.Company_Image.setText(_translate("MainWindow", "[img]"))
        self.Industry_Title.setText(_translate("MainWindow", "Industry:"))
        self.Exchange_Title.setText(_translate("MainWindow", "Exchange:"))
        self.Industry_Label.setText(_translate("MainWindow", "Online Media"))
        self.Exchange_Label.setText(_translate("MainWindow", "NASDAQ"))
        self.Stock_Price.setText(_translate("MainWindow", "69.00"))
        self.Stock_Percentage_Change.setText(_translate("MainWindow", "+0.15"))
        self.Stock_Volume.setText(_translate("MainWindow", "Vol: "))
        self.Stock_Name.setText(_translate("MainWindow", "AAPL"))
        self.Stock_Market_Capitalization.setText(_translate("MainWindow", "Mkt Cap: "))
        self.Stock_Beta.setText(_translate("MainWindow", "Beta:"))
        self.Stock_Open.setText(_translate("MainWindow", "Open:"))
        self.Stock_High.setText(_translate("MainWindow", "H:"))
        self.Stock_Low.setText(_translate("MainWindow", "L:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
