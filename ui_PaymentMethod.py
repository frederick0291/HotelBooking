# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'paymentJsjysx.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_PaymentMethod(object):
    def setupUi(self, PaymentMethod):
        if PaymentMethod.objectName():
            PaymentMethod.setObjectName(u"PaymentMethod")
        PaymentMethod.resize(686, 301)
        self.label_15 = QLabel(PaymentMethod)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(0, 0, 1011, 61))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_15.setPalette(palette)
        self.label_15.setAutoFillBackground(True)
        self.label_9 = QLabel(PaymentMethod)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(-120, 0, 521, 41))
        palette1 = QPalette()
        brush2 = QBrush(QColor(255, 255, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush)
        brush3 = QBrush(QColor(255, 255, 191, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(127, 127, 63, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(170, 170, 84, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 128))
        brush7.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
        brush8 = QBrush(QColor(0, 0, 0, 128))
        brush8.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        brush9 = QBrush(QColor(0, 0, 0, 128))
        brush9.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.label_9.setPalette(palette1)
        font = QFont()
        font.setFamily(u"Century Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setToolTipDuration(-4)
        self.label_9.setAutoFillBackground(False)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(PaymentMethod)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(60, 30, 171, 20))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush10 = QBrush(QColor(120, 120, 120, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        self.label_11.setPalette(palette2)
        font1 = QFont()
        font1.setPointSize(7)
        self.label_11.setFont(font1)
        self.label_10 = QLabel(PaymentMethod)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, -20, 91, 101))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        self.label_10.setPalette(palette3)
        font2 = QFont()
        font2.setFamily(u"Century Gothic")
        font2.setPointSize(28)
        font2.setBold(False)
        font2.setWeight(50)
        self.label_10.setFont(font2)
        self.label_10.setAutoFillBackground(False)
        self.label_2 = QLabel(PaymentMethod)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 10, 521, 41))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette4.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        brush11 = QBrush(QColor(0, 0, 0, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
        brush12 = QBrush(QColor(0, 0, 0, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        brush13 = QBrush(QColor(0, 0, 0, 128))
        brush13.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        self.label_2.setPalette(palette4)
        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_2.setFont(font3)
        self.label_2.setToolTipDuration(-4)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.line_4 = QFrame(PaymentMethod)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(650, 10, 21, 16))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_5 = QFrame(PaymentMethod)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(650, 20, 21, 16))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.line_6 = QFrame(PaymentMethod)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(650, 30, 21, 16))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.label_7 = QLabel(PaymentMethod)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 60, 751, 441))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Base, brush)
        brush14 = QBrush(QColor(159, 103, 18, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush14)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush14)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        self.label_7.setPalette(palette5)
        self.label_7.setAutoFillBackground(True)
        self.rbEwallet = QRadioButton(PaymentMethod)
        self.rbEwallet.setObjectName(u"rbEwallet")
        self.rbEwallet.setGeometry(QRect(40, 170, 341, 17))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        self.rbEwallet.setPalette(palette6)
        font4 = QFont()
        font4.setFamily(u"Century Gothic")
        font4.setPointSize(14)
        self.rbEwallet.setFont(font4)
        self.rbCard = QRadioButton(PaymentMethod)
        self.rbCard.setObjectName(u"rbCard")
        self.rbCard.setGeometry(QRect(40, 110, 391, 31))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        self.rbCard.setPalette(palette7)
        self.rbCard.setFont(font4)
        self.rbCash = QRadioButton(PaymentMethod)
        self.rbCash.setObjectName(u"rbCash")
        self.rbCash.setGeometry(QRect(40, 220, 351, 17))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        self.rbCash.setPalette(palette8)
        self.rbCash.setFont(font4)
        self.btnContinue = QPushButton(PaymentMethod)
        self.btnContinue.setObjectName(u"btnContinue")
        self.btnContinue.setGeometry(QRect(440, 250, 91, 31))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.Button, brush14)
        brush15 = QBrush(QColor(158, 103, 18, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush15)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush15)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        self.btnContinue.setPalette(palette9)
        font5 = QFont()
        font5.setFamily(u"Century Gothic")
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setWeight(75)
        self.btnContinue.setFont(font5)
        self.btnExit = QPushButton(PaymentMethod)
        self.btnExit.setObjectName(u"btnExit")
        self.btnExit.setGeometry(QRect(540, 250, 91, 31))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.Button, brush14)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush15)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush15)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        self.btnExit.setPalette(palette10)
        self.btnExit.setFont(font5)

        self.retranslateUi(PaymentMethod)

        QMetaObject.connectSlotsByName(PaymentMethod)
    # setupUi

    def retranslateUi(self, PaymentMethod):
        PaymentMethod.setWindowTitle(QCoreApplication.translate("PaymentMethod", u"PaymentMethod", None))
        self.label_15.setText("")
        self.label_9.setText(QCoreApplication.translate("PaymentMethod", u"H O T E L   D E L   L U N A ", None))
        self.label_11.setText(QCoreApplication.translate("PaymentMethod", u"A   P L A C E   L I K E    H O M E", None))
        self.label_10.setText(QCoreApplication.translate("PaymentMethod", u"O", None))
        self.label_2.setText(QCoreApplication.translate("PaymentMethod", u"M o d e   o f   P a y m e n t", None))
        self.label_7.setText("")
        self.rbEwallet.setText(QCoreApplication.translate("PaymentMethod", u"E-Wallet (GCash/Paymaya)", None))
        self.rbCard.setText(QCoreApplication.translate("PaymentMethod", u"Bank Transfer (Debit Card / Credit Card)", None))
        self.rbCash.setText(QCoreApplication.translate("PaymentMethod", u"Cash Over the Counter", None))
        self.btnContinue.setText(QCoreApplication.translate("PaymentMethod", u"Continue", None))
        self.btnExit.setText(QCoreApplication.translate("PaymentMethod", u"Exit", None))
    # retranslateUi
