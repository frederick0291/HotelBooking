
import sys
import platform
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
# from PyQt5.uic import uiparser

## ==> MAIN WINDOW
from ui_MainWindow import Ui_MainWindow

## ==> TERMS AND CONDITIONS
from ui_TandC import Ui_TandC

## ==> HOTEL BOOKING
from ui_HotelBooking import Ui_HotelBooking

## ==> ARE YOU SURE?
from ui_AreYouSure import Ui_AreYouSure

## ==> CANCEL: YES | NO
from ui_CancelYesNo import Ui_YesNo

## ==> PAYMENT METHOD
from ui_PaymentMethod import Ui_PaymentMethod

## ==> RESERVATION RECORD
from ui_ReservationRecord import Ui_ReservationRecord

## ==> ROOM INFO
from ui_RoomInfo import Ui_RoomInfo

## ==> SIGN IN
from ui_user import Ui_AdminSignIn

## ==> EDIT INVENTORY
from ui_EditInventory import Ui_EditInventory

## Set options for Laptops or other monitors that need high DPI scaling
# if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
#     PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

# if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
#     PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

## ==> GLOBALS

# YOUR MAIN APPLICATION
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        ## Button Clicks
        self.ui.btnExit.clicked.connect(self.exitButton)
        self.ui.btnBooking.clicked.connect(self.TandC)
        self.ui.btnRoom.clicked.connect(self.RoomInfo)
        self.ui.btnAdmin.clicked.connect(self.SignIn)
        
        ## Show Window
        self.show()
        
    def exitButton(self):
        self.close()
        
    def TandC(self):
        self.TandC = TandC(parent=self)
        self.TandC.show()
        self.hide()
    
    def RoomInfo(self):
        self.RoomInfo = RoomInfo(parent=self)
        self.RoomInfo.show()
        self.hide()
    
    def SignIn(self):
        self.AdminSignIn = AdminSignIn(parent=self)
        self.AdminSignIn.show()
        
    
# TERMS AND CONDITIONS
class TandC(QMainWindow, Ui_MainWindow):
    def __init__(self,parent):
        QMainWindow.__init__(self)
        self.ui = Ui_TandC()
        self.ui.setupUi(self)
        self.parent = parent

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        ## BUTTON CLICKS
        ########################################################################
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def accept(self):
        self.HotelBooking = HotelBooking()
        self.HotelBooking.show()
        self.close()
        
    def reject(self):
        self.parent.show()
        self.close()
        

class HotelBooking(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_HotelBooking()
        self.ui.setupUi(self)
        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)    
        
        ## BUTTON CLICKS
        ########################################################################
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)
        ## ==> END ##        

    ## ==> APP FUNCTIONS
    ########################################################################
    # YES
    def accept(self):
        # TODO Start working here
        self.AreYouSure = AreYouSure(parent=self)
        self.AreYouSure.show()
    
    # NO
    def reject(self):
        self.CancelYesNo = CancelYesNo(parent=self)
        self.CancelYesNo.show()
        # self.close()

class AreYouSure(QMainWindow, Ui_HotelBooking):
    def __init__(self, parent):
        QMainWindow.__init__(self)
        self.ui = Ui_AreYouSure()
        self.ui.setupUi(self)
        self.parent = parent
        
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)    
        
        ## BUTTON CLICKS
        ########################################################################
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

    def accept(self):
        # Hide the parent since we need the data from there
        self.parent.hide()
        self.PaymentMethod = PaymentMethod(parent=self.parent)
        self.PaymentMethod.show()
        # OPEN Payment here
        self.close()
        
    def reject(self):
        self.close()

class CancelYesNo(QMainWindow, Ui_HotelBooking):
    def __init__(self, parent):
        QMainWindow.__init__(self)
        self.ui = Ui_YesNo()
        self.ui.setupUi(self)
        self.parent = parent
        
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)    
        
        ## BUTTON CLICKS
        ########################################################################
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)
    
    def accept(self):
        self.main = MainWindow()
        self.main.show()
        self.parent.close()
        self.close()
        
    def reject(self):
        self.close()

class PaymentMethod(QMainWindow, Ui_HotelBooking):
    def __init__(self,parent):
        QMainWindow.__init__(self)
        self.ui = Ui_PaymentMethod()
        self.ui.setupUi(self)
        self.parent = parent
        
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)    
        
        ## BUTTON CLICKS
        ########################################################################
        self.ui.btnContinue.clicked.connect(self.cont)
        self.ui.btnExit.clicked.connect(self.exit)
        
    def cont(self):
        self.ReservationRecord = ReservationRecord(parent=self.parent)
        self.ReservationRecord.show()
        self.hide()
    
    def exit(self):
        self.CancelYesNo = CancelYesNo(parent=self)
        self.CancelYesNo.show()

class ReservationRecord(QMainWindow, Ui_HotelBooking):
    def __init__(self,parent):
        QMainWindow.__init__(self)
        self.ui = Ui_ReservationRecord()
        self.ui.setupUi(self)
        self.parent = parent
        
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)    

        ## BUTTON CLICKS
        ########################################################################        
        # self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)
    
    def reject(self):
        self.main = MainWindow()
        self.main.show()
        self.close()
        
class RoomInfo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent):
        QMainWindow.__init__(self)
        self.ui = Ui_RoomInfo()
        self.ui.setupUi(self)
        self.parent = parent
        
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.buttonBox.rejected.connect(self.closeInfo)

    def closeInfo(self):
        self.parent.show()
        self.close()  
        
class AdminSignIn(QMainWindow, Ui_MainWindow):
    def __init__(self, parent):
        QMainWindow.__init__(self)
        self.ui = Ui_AdminSignIn()
        self.ui.setupUi(self)
        self.parent=parent
        
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        ## BUTTON CLICKS
        self.ui.btnLogin.clicked.connect(self.login)
        
    def login(self):
        self.EditInventory = EditInventory()
        self.EditInventory.show()
        self.parent.close()
        self.close()
        
class EditInventory(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_EditInventory()
        self.ui.setupUi(self)
        
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # self.ui.buttonBox.rejected.connect(self.closeInfo)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())