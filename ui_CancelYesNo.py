# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CANCEL-YES-OR-NOZFdamp.ui'
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


class Ui_YesNo(object):
    def setupUi(self, YesNo):
        if YesNo.objectName():
            YesNo.setObjectName(u"YesNo")
        YesNo.resize(400, 180)
        self.buttonBox = QDialogButtonBox(YesNo)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(-60, 120, 341, 32))
        palette = QPalette()
        brush = QBrush(QColor(159, 103, 18, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        brush2 = QBrush(QColor(157, 102, 18, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.buttonBox.setPalette(palette)
        font = QFont()
        font.setFamily(u"Century Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.buttonBox.setFont(font)
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.No|QDialogButtonBox.Yes)
        self.label = QLabel(YesNo)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 401, 301))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.label.setPalette(palette1)
        self.label.setAutoFillBackground(True)
        self.label_3 = QLabel(YesNo)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 361, 161))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.label_3.setPalette(palette2)
        self.label_3.setAutoFillBackground(True)
        self.label_5 = QLabel(YesNo)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 30, 311, 91))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        brush5 = QBrush(QColor(255, 255, 127, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush1)
        brush6 = QBrush(QColor(255, 255, 191, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush6)
        brush7 = QBrush(QColor(127, 127, 63, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush7)
        brush8 = QBrush(QColor(170, 170, 84, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush8)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush4)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush6)
        brush9 = QBrush(QColor(255, 255, 220, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush4)
        brush10 = QBrush(QColor(0, 0, 0, 128))
        brush10.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush4)
        brush11 = QBrush(QColor(0, 0, 0, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush4)
        brush12 = QBrush(QColor(0, 0, 0, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.label_5.setPalette(palette3)
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_5.setFont(font1)
        self.label_5.setToolTipDuration(-4)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label.raise_()
        self.label_3.raise_()
        self.buttonBox.raise_()
        self.label_5.raise_()

        self.retranslateUi(YesNo)
        # self.buttonBox.accepted.connect(YesNo.accept)
        # self.buttonBox.rejected.connect(YesNo.reject)

        QMetaObject.connectSlotsByName(YesNo)
    # setupUi

    def retranslateUi(self, YesNo):
        YesNo.setWindowTitle(QCoreApplication.translate("YesNo", u"YesNo", None))
        self.label.setText("")
        self.label_3.setText("")
        self.label_5.setText(QCoreApplication.translate("YesNo", u"Are you sure you want to CANCEL RESERVATION?", None))
    # retranslateUi

