
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
from ui_AdminSignIn import Ui_AdminSignIn

## ==> EDIT INVENTORY
from ui_EditInventory import Ui_EditInventory

## ==> EDIT ROOM INFO
from ui_EditRoomInfo import Ui_EditRoomInfo

## Set options for Laptops or other monitors that need high DPI scaling
## Source: https://stackoverflow.com/questions/57527705/qt-designer-using-high-resolution-need-low-resolution-version
## Or just disable the custom scaling in windows setting.

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


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
    
    ## MOUSE PRESS EVENT - MOVING WINDOWS BY DRAGGING 
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
    
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

    ## MOUSE PRESS EVENT - MOVING WINDOWS BY DRAGGING 
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
        

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

    ## MOUSE PRESS EVENT - MOVING WINDOWS BY DRAGGING 
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


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
        
    ## MOUSE PRESS EVENT - MOVING WINDOWS BY DRAGGING 
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

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

    ## MOUSE PRESS EVENT - MOVING WINDOWS BY DRAGGING 
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

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
        
    ## MOUSE PRESS EVENT - MOVING WINDOWS BY DRAGGING 
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

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
        
        # Access the parent's UI to get the name of the customer in the line edit
        # The parent's UI is still accessible since we only used hide() not close() to the hotelbooking object
        # self.parent is the HotelBooking() we created on line 124 
        customer_name = self.parent.ui.txtName.text()
        date_in = self.parent.ui.deIn.date()
        # convert the pyqt date to normal python date then convert the python date to string
        date_in = date_in.toPyDate()
        date_in = str(date_in)
        # get the time in from the parent UI
        time_in = self.parent.ui.teIn.time()
        # convert the pyqt time to normal string
        time_in = time_in.toString()
        
        print(date_in + " " + time_in)
        # set the customer name and the time and date on the reservation record UI      
        self.ui.customerName.setText(customer_name)
        self.ui.timeAndDate.setText(date_in + " " + time_in)
    
    def reject(self):
        self.main = MainWindow()
        self.main.show()
        self.close()

    ## MOUSE PRESS EVENT - MOVING WINDOWS BY DRAGGING 
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

        
class RoomInfo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent):
        QMainWindow.__init__(self)
        self.ui = Ui_RoomInfo()
        self.ui.setupUi(self)
        self.parent = parent
        
        ## READ THE INCLUSIONS OF EACH ROOM BASED ON TEXT FILE
        with open("Room_A.txt", "r") as RoomADetails:
            RoomA = RoomADetails.readlines()
        with open("Room_B.txt", "r") as RoomBDetails:
            RoomB = RoomBDetails.readlines()        
        with open("Room_C.txt", "r") as RoomCDetails:
            RoomC = RoomCDetails.readlines()
        with open("Room_D.txt", "r") as RoomDDetails:
            RoomD = RoomDDetails.readlines()
        
        ## SET THE INCLUSIONS OF EACH ROOM TO THE LIST WIDGET
        for inclusion in RoomA:
            self.ui.roomAText.append(inclusion)
        
        for inclusion in RoomB:
            self.ui.roomBText.append(inclusion)
            
        for inclusion in RoomC:
            self.ui.roomCText.append(inclusion)        
        
        for inclusion in RoomD:
            self.ui.roomDText.append(inclusion)        
        
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.buttonBox.rejected.connect(self.closeInfo)

    def closeInfo(self):
        # re-show the parent Ui_MainWindow then close the Roominfo GUI 
        self.parent.show()
        self.close()  
    
    ## MOUSE PRESS EVENT - MOVING WINDOWS BY DRAGGING 
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    
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
        # Check if username and password are correct before allowing user to enter as admin
        # Echomode for txtPass was set to Password to hide the password as we type
        if self.ui.txtUser.text() == "Admin" and self.ui.txtPass.text() == "AdminLuna":
            self.EditInventory = EditInventory()
            self.EditInventory.show()
            self.parent.close()
            self.close()
        else:
            pass
    
    ## MOUSE PRESS EVENT - MOVING WINDOWS BY DRAGGING 
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    
class EditInventory(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_EditInventory()
        self.ui.setupUi(self)
        
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        # Button presses
        self.ui.btnBack.clicked.connect(self.back)
        self.ui.btnEditRoomInfo.clicked.connect(self.gotoEditRoomInfo)
    
    # Button Functions
    def back(self):
        # if we click back go and open up the main window again
        self.main = MainWindow()
        self.main.show()
        self.close()
    
    def gotoEditRoomInfo(self):
        self.EditRoomInfo = EditRoomInfo(parent=self)
        self.EditRoomInfo.show()
        self.hide()
    
    ## MOUSE PRESS EVENT - MOVING WINDOWS BY DRAGGING 
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

class EditRoomInfo(QMainWindow, Ui_EditInventory):
    def __init__(self, parent):
        QMainWindow.__init__(self)
        self.ui = Ui_EditRoomInfo()
        self.ui.setupUi(self)
        self.parent = parent
        
        ## READ THE INCLUSIONS OF EACH ROOM BASED ON TEXT FILE
        with open("Room_A.txt", "r") as RoomADetails:
            RoomA = RoomADetails.readlines()
        with open("Room_B.txt", "r") as RoomBDetails:
            RoomB = RoomBDetails.readlines()        
        with open("Room_C.txt", "r") as RoomCDetails:
            RoomC = RoomCDetails.readlines()
        with open("Room_D.txt", "r") as RoomDDetails:
            RoomD = RoomDDetails.readlines()
        
        ## SET THE INCLUSIONS OF EACH ROOM TO THE LIST WIDGET
        for inclusion in RoomA:
            self.ui.roomAText.append(inclusion)
        
        for inclusion in RoomB:
            self.ui.roomBText.append(inclusion)
            
        for inclusion in RoomC:
            self.ui.roomCText.append(inclusion)        
        
        for inclusion in RoomD:
            self.ui.roomDText.append(inclusion)        
        
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.buttonBox.rejected.connect(self.closeInfo)
        self.ui.buttonBox.accepted.connect(self.saveInfo)

    def closeInfo(self):
        self.parent.show()
        self.close()  
    
    def saveInfo(self):
        # NOTE: OVERWRITE TEXT FILE HERE
        self.parent.show()
        self.close()
        
    ## MOUSE PRESS EVENT - MOVING WINDOWS BY DRAGGING 
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())