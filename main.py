import sys
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                          QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                         QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

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


# YOUR MAIN APPLICATION
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        ## REMOVE TITLE BAR
        ## Source: https://stackoverflow.com/questions/7021502/pyqt-remove-the-programs-title-bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        ## Button Clicks
        ## Source: https://stackoverflow.com/questions/53225320/open-a-new-window-when-the-button-is-clicked-pyqt5
        self.ui.btnExit.clicked.connect(self.exitButton)
        self.ui.btnBooking.clicked.connect(self.TandC)
        self.ui.btnRoom.clicked.connect(self.RoomInfo)
        self.ui.btnAdmin.clicked.connect(self.SignIn)
        
        ## Show Window
        self.show()
        
    def exitButton(self):
        self.close()
        
    def TandC(self):
        # NOTE: Setting parent and child windows. 
        # Source: https://stackoverflow.com/questions/52493439/access-data-from-the-parent-window-in-a-child-window-in-pyqt
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
    # SOURCE: https://stackoverflow.com/questions/37718329/pyqt5-draggable-frameless-window
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
    
# TERMS AND CONDITIONS
# NOTE: Setting parent and child windows. 
# Source: https://stackoverflow.com/questions/52493439/access-data-from-the-parent-window-in-a-child-window-in-pyqt
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
        ## Add choices to combo boxes
        ## First we read the text files to get the choices
        with open("Available_Room_A.txt", "r") as RoomADetails:
            RoomA = RoomADetails.readlines()
        with open("Available_Room_B.txt", "r") as RoomBDetails:
            RoomB = RoomBDetails.readlines()
        with open("Available_Room_C.txt", "r") as RoomCDetails:
            RoomC = RoomCDetails.readlines()
        with open("Available_Room_D.txt", "r") as RoomDDetails:
            RoomD = RoomDDetails.readlines()        
            
        ## SET THE AVAILABLE ROOMS TO EACH COMBO BOX
        ## Source: https://stackoverflow.com/questions/35142276/how-can-i-add-item-data-to-qcombobox-from-qt-designer-ui-file
        ## For Loop the room variables
        for room in RoomA:
            # remove the \n character in the "room" string to avoid display issues in the combo box
            # source: https://www.kite.com/python/answers/how-to-remove-all-line-breaks-from-a-string-in-python
            room = room.replace("\n", "")
            self.ui.cmbA.addItem(room)
        for room in RoomB:
            room = room.replace("\n", "")
            self.ui.cmbB.addItem(room)
        for room in RoomC:
            room = room.replace("\n", "")
            self.ui.cmbC.addItem(room)    
        for room in RoomD:
            room = room.replace("\n", "")
            self.ui.cmbD.addItem(room)      
        

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)    
        
        ## BUTTON CLICKS
        ########################################################################
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)
        self.ui.AddRoomBtn.clicked.connect(self.addRoom)
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
        
    # RESERVE MORE THAN ONE ROOM
    def addRoom(self):
        # Get the customer name
        Name = self.ui.txtName.text()
        
        # PART 1: Get the  rooms that the user wants
        if self.ui.rbA.isChecked():
            # get the room name from the combobox
            # Source: https://stackoverflow.com/questions/2056915/how-can-i-get-the-selected-value-out-of-a-qcombobox
            room = self.ui.cmbA.currentText()
            # delete the room in the text file
            with open("Available_Room_A.txt", "r") as RoomADetails:
                # use splitlines to remove \n from each line as it will cause an error in the index searching
                # source: https://stackoverflow.com/questions/15233340/getting-rid-of-n-when-using-readlines
                RoomA = RoomADetails.read().splitlines()
            # get the index/line number from the RoomA so we could replace it
            # source: https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
            index = RoomA.index(room)
            # remove that index from the list of rooms
            # Source: https://stackoverflow.com/questions/627435/how-to-remove-an-element-from-a-list-by-index
            RoomA.pop(index)
            
            # we now have a list of rooms WITHOUT the reserved room
            # we will write it back to the text file 
            # Source: https://stackoverflow.com/questions/4719438/editing-specific-line-in-text-file-in-python
            with open("Available_Room_A.txt", "w") as RoomADetails:
                # write back the rooms into a new line for each room
                # we use .join to join the strings and add a \n after each item
                # Source: https://stackoverflow.com/questions/13730107/writelines-writes-lines-without-newline-just-fills-the-file/42757094
                RoomADetails.write("\n".join(RoomA))
                
            # Store the rooms to reserve here first before we send it to the table 
            with open("Reserved_Rooms.txt", "a") as ReservedRooms:
                ReservedRooms.write(Name + "," + room + "," + "A" + "\n")
            
        if self.ui.rbB.isChecked():
            room = self.ui.cmbB.currentText()
            with open("Available_Room_B.txt", "r") as RoomBDetails:
                RoomB = RoomBDetails.read().splitlines()
            index = RoomB.index(room)
            RoomB.pop(index)
            
            with open("Available_Room_B.txt", "w") as RoomBDetails:
                RoomBDetails.write("\n".join(RoomB))
                        
            with open("Reserved_Rooms.txt", "a") as ReservedRooms:
                ReservedRooms.write(Name + "," + room + "," + "B" + "\n")
                
        if self.ui.rbC.isChecked():
            room = self.ui.cmbC.currentText()
            with open("Available_Room_C.txt", "r") as RoomCDetails:
                RoomC = RoomCDetails.read().splitlines()
            index = RoomC.index(room)
            RoomC.pop(index)
            
            with open("Available_Room_C.txt", "w") as RoomCDetails:
                RoomCDetails.write("\n".join(RoomC))
                
            with open("Reserved_Rooms.txt", "a") as ReservedRooms:
                ReservedRooms.write(Name + "," + room + "," + "C" + "\n")
            
        if self.ui.rbD.isChecked():
            room = self.ui.cmbD.currentText()
            with open("Available_Room_D.txt", "r") as RoomDDetails:
                RoomD = RoomDDetails.read().splitlines()
            index = RoomD.index(room)
            RoomD.pop(index)
            
            with open("Available_Room_D.txt", "w") as RoomDDetails:
                RoomDDetails.write("\n".join(RoomD)) 
          
            with open("Reserved_Rooms.txt", "a") as ReservedRooms:
                ReservedRooms.write(Name + "," + room + "," + "D" + "\n")
            
        
        # PART 2: Remove those rooms from the choices by reading the text file again
        with open("Available_Room_A.txt", "r") as RoomADetails:
            RoomA = RoomADetails.readlines()
        with open("Available_Room_B.txt", "r") as RoomBDetails:
            RoomB = RoomBDetails.readlines()
        with open("Available_Room_C.txt", "r") as RoomCDetails:
            RoomC = RoomCDetails.readlines()
        with open("Available_Room_D.txt", "r") as RoomDDetails:
            RoomD = RoomDDetails.readlines()        
        
        # CLEAN UP THE COMBO BOXES BEFORE WE ADD THE CHOICES AGAIN:
        self.ui.cmbA.clear()
        self.ui.cmbB.clear()
        self.ui.cmbC.clear()
        self.ui.cmbD.clear()
        
        ## SET THE AVAILABLE ROOMS TO EACH COMBO BOX
        ## Source: https://stackoverflow.com/questions/35142276/how-can-i-add-item-data-to-qcombobox-from-qt-designer-ui-file
        ## For Loop the room variables
        for room in RoomA:
            # remove the \n character in the "room" string to avoid display issues in the combo box
            # source: https://www.kite.com/python/answers/how-to-remove-all-line-breaks-from-a-string-in-python
            room = room.replace("\n", "")
            self.ui.cmbA.addItem(room)
        for room in RoomB:
            room = room.replace("\n", "")
            self.ui.cmbB.addItem(room)
        for room in RoomC:
            room = room.replace("\n", "")
            self.ui.cmbC.addItem(room)    
        for room in RoomD:
            room = room.replace("\n", "")
            self.ui.cmbD.addItem(room)     
            
        # UNCHECK THE ROOM SELECTION CHECK BOXES 
        # SOURCE: https://www.geeksforgeeks.org/pyqt5-setchecked-method-for-check-box/
        self.ui.rbA.setChecked(False)
        self.ui.rbB.setChecked(False)
        self.ui.rbC.setChecked(False)
        self.ui.rbD.setChecked(False)
        

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

        # OPEN Payment here
        self.PaymentMethod = PaymentMethod(parent=self.parent)
        self.PaymentMethod.show()
        
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
        
        # RESERVE THE ROOM AND REMOVE IT FROM THE CHOICES
        # First we check which radio button was checked
        # Source: https://www.geeksforgeeks.org/pyqt5-find-if-radio-button-is-checked/
        if self.parent.ui.rbA.isChecked():
            # get the room name from the combobox
            # Source: https://stackoverflow.com/questions/2056915/how-can-i-get-the-selected-value-out-of-a-qcombobox
            room = self.parent.ui.cmbA.currentText()
            # delete the room in the text file
            with open("Available_Room_A.txt", "r") as RoomADetails:
                # use splitlines to remove \n from each line as it will cause an error in the index searching
                # source: https://stackoverflow.com/questions/15233340/getting-rid-of-n-when-using-readlines
                RoomA = RoomADetails.read().splitlines()
            # get the index/line number from the RoomA so we could replace it
            # source: https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
            index = RoomA.index(room)
            # remove that index from the list of rooms
            # Source: https://stackoverflow.com/questions/627435/how-to-remove-an-element-from-a-list-by-index
            RoomA.pop(index)
            
            # we now have a list of rooms WITHOUT the reserved room
            # we will write it back to the text file 
            # Source: https://stackoverflow.com/questions/4719438/editing-specific-line-in-text-file-in-python
            with open("Available_Room_A.txt", "w") as RoomADetails:
                # write back the rooms into a new line for each room
                # we use .join to join the strings and add a \n after each item
                # Source: https://stackoverflow.com/questions/13730107/writelines-writes-lines-without-newline-just-fills-the-file/42757094
                RoomADetails.write("\n".join(RoomA))
                
        if self.parent.ui.rbB.isChecked():
            room = self.parent.ui.cmbB.currentText()
            with open("Available_Room_B.txt", "r") as RoomBDetails:
                RoomB = RoomBDetails.read().splitlines()
            index = RoomB.index(room)
            RoomB.pop(index)
            
            with open("Available_Room_B.txt", "w") as RoomBDetails:
                RoomBDetails.write("\n".join(RoomB))
                
        if self.parent.ui.rbC.isChecked():
            room = self.parent.ui.cmbC.currentText()
            with open("Available_Room_C.txt", "r") as RoomCDetails:
                RoomC = RoomCDetails.read().splitlines()
            index = RoomC.index(room)
            RoomC.pop(index)
            
            with open("Available_Room_C.txt", "w") as RoomCDetails:
                RoomCDetails.write("\n".join(RoomC))

        if self.parent.ui.rbD.isChecked():
            room = self.parent.ui.cmbD.currentText()
            with open("Available_Room_D.txt", "r") as RoomDDetails:
                RoomD = RoomDDetails.read().splitlines()
            index = RoomD.index(room)
            RoomD.pop(index)
            
            with open("Available_Room_D.txt", "w") as RoomDDetails:
                RoomDDetails.write("\n".join(RoomD)) 
                       
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
        ## SOURCE: https://www.pythonforbeginners.com/files/with-statement-in-python
        with open("Room_A.txt", "r") as RoomADetails:
            RoomA = RoomADetails.readlines()
        with open("Room_B.txt", "r") as RoomBDetails:
            RoomB = RoomBDetails.readlines()        
        with open("Room_C.txt", "r") as RoomCDetails:
            RoomC = RoomCDetails.readlines()
        with open("Room_D.txt", "r") as RoomDDetails:
            RoomD = RoomDDetails.readlines()
        
        ## SET THE INCLUSIONS OF EACH ROOM TO THE TEXT BROWSER
        ## Source: https://stackoverflow.com/questions/7771164/add-more-than-one-line-to-a-qtextedit-pyqt
        ## For Loop
        for inclusion in RoomA:
            # replace the \n characters at the end of the inclusion string to display them properly
            # source: https://www.kite.com/python/answers/how-to-remove-all-line-breaks-from-a-string-in-python
            inclusion = inclusion.replace("\n", "")
            self.ui.roomAText.append(inclusion)
        
        for inclusion in RoomB:
            inclusion = inclusion.replace("\n", "")
            self.ui.roomBText.append(inclusion)
            
        for inclusion in RoomC:
            inclusion = inclusion.replace("\n", "")
            self.ui.roomCText.append(inclusion)        
        
        for inclusion in RoomD:
            inclusion = inclusion.replace("\n", "")
            self.ui.roomDText.append(inclusion)        
        
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        ## BUTTON CLICKS
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
        
        # ## REMOVE TITLE BAR
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
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
        self.ui.tblCustomer.verticalHeader().setVisible(False)
        self.ui.tblCustomer.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.updateCustomerTable()
        
        
        
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        # Button presses
        self.ui.btnBack.clicked.connect(self.back)
        self.ui.btnEditRoomInfo.clicked.connect(self.gotoEditRoomInfo)
        self.ui.btnDelete.clicked.connect(self.delete)
        self.ui.btnSave.clicked.connect(self.save)
        self.ui.btnProfile.clicked.connect(self.viewProfile)
        self.ui.btnUpdate.clicked.connect(self.update)
        self.ui.btnSearch.clicked.connect(self.search)
        self.ui.btnView.clicked.connect(self.viewAll)
    
    # update the customer table widget
    # SOURCE: https://stackoverflow.com/questions/32506464/how-to-add-text-to-a-cell-of-a-tablewidget
    def updateCustomerTable(self):
        self.ui.tblCustomer.setColumnCount(4)
        # Add headers to the columns
        # SOURCE: https://stackoverflow.com/questions/37222081/pyqt-qtableview-set-horizontal-vertical-header-labels/37223212
        self.ui.tblCustomer.setHorizontalHeaderLabels(["Customer ID", "Name", "Room #", "Room Type"])
        # read reserved rooms text file to get the data to add to the table
        with open("Reserved_Rooms.txt", "r") as reservedRooms:
            rooms = reservedRooms.readlines()
        
        # each line of room has the details like the customer name room # and room type
        for room in rooms:
            room = room.replace("\n","")
            # split each string line to each of the items (Customer Name, Room #, Room Type)
            # split by the comma
            # SOURCE: https://www.w3schools.com/python/ref_string_split.asp
            room = room.split(",")
            print(room)
            # add a new row using the room details 
            # SOURCE: https://stackoverflow.com/questions/24044421/how-to-add-a-row-in-a-tablewidget-pyqt
            rowCount = self.ui.tblCustomer.rowCount()
            custID = str(rowCount + 1)
            name = room[0]
            roomNum = room[1]
            roomType = room[2]
            self.ui.tblCustomer.insertRow(rowCount)
            self.ui.tblCustomer.setItem(rowCount , 0, QTableWidgetItem(custID))
            self.ui.tblCustomer.setItem(rowCount , 1, QTableWidgetItem(name))
            self.ui.tblCustomer.setItem(rowCount , 2, QTableWidgetItem(roomNum))
            self.ui.tblCustomer.setItem(rowCount , 3, QTableWidgetItem(roomType))
    
    # Button Functions
    def search(self):
        # Hide all rows
        numRows = self.ui.tblCustomer.rowCount()
        for row in range(numRows):
            self.ui.tblCustomer.hideRow(row)
            
        # Unhide only rows that are going to match the filter
        # Source: https://www.qtcentre.org/threads/43313-How-to-set-filter-option-in-QTableWidget
        name = self.ui.txtSearch.text()
        filterList = self.ui.tblCustomer.findItems(name, Qt.MatchContains)
        for item in filterList:
            self.ui.tblCustomer.showRow(item.row())
            
    def viewAll(self):
        # Unhide all rows
        numRows = self.ui.tblCustomer.rowCount()
        for row in range(numRows):
            self.ui.tblCustomer.showRow(row)
            
        # clean up the GUI
        self.ui.txtSearch.setText("")
            
    def update(self):
        # get our index from the viewProfile function
        index = self.indexToEdit
        
        # get the data from the GUI
        custID = self.ui.txtNo.text()
        name = self.ui.txtNameP.text()
        roomNum = self.ui.txtAddressP.text()
        roomType = self.ui.txtContactP.text()
        
        # update the table row
        self.ui.tblCustomer.setItem(index , 0, QTableWidgetItem(custID))
        self.ui.tblCustomer.setItem(index , 1, QTableWidgetItem(name))
        self.ui.tblCustomer.setItem(index , 2, QTableWidgetItem(roomNum))
        self.ui.tblCustomer.setItem(index , 3, QTableWidgetItem(roomType))
        
        # clean up the update profie box
        self.ui.txtNo.setText("")
        self.ui.txtNameP.setText("")
        self.ui.txtAddressP.setText("")
        self.ui.txtContactP.setText("")
    
    def viewProfile(self):
        # get the index of the item first
        index = self.ui.tblCustomer.selectionModel().selectedRows()
        index = index[0].row()

        # gather the details
        custID = str(index + 1)
        custName = self.ui.tblCustomer.item(index, 1).text()
        roomNum = self.ui.tblCustomer.item(index, 2).text()
        roomType = self.ui.tblCustomer.item(index, 3).text()
        
        # update the GUI with the above details
        self.ui.txtNo.setText(custID)
        self.ui.txtNameP.setText(custName)
        self.ui.txtAddressP.setText(roomNum)
        self.ui.txtContactP.setText(roomType)
        
        # create a variable that will store our index since we need to access this when we click update
        self.indexToEdit = index 
        
    def save(self):
        # get the data first
        rowCount = self.ui.tblCustomer.rowCount()
        custID = str(rowCount + 1)
        name = self.ui.txtIname.text()
        roomNum = self.ui.txtIadd.text()
        roomType = self.ui.txtIcp.text()
        
        # add new row then add the details
        self.ui.tblCustomer.insertRow(rowCount)
        self.ui.tblCustomer.setItem(rowCount , 0, QTableWidgetItem(custID))
        self.ui.tblCustomer.setItem(rowCount , 1, QTableWidgetItem(name))
        self.ui.tblCustomer.setItem(rowCount , 2, QTableWidgetItem(roomNum))
        self.ui.tblCustomer.setItem(rowCount , 3, QTableWidgetItem(roomType))

        # clean up the line edits 
        self.ui.txtIname.setText("")
        self.ui.txtIadd.setText("")
        self.ui.txtIcp.setText("")
        
    def delete(self):
        index = self.ui.tblCustomer.selectionModel().selectedRows()
        index = index[0].row()
        # get the index of the selected item 
        # Source: https://doc.qt.io/qt-5/qmodelindex.html
        # then delete the row
        # Source: https://stackoverflow.com/questions/48121393/how-to-delete-multiple-rows-in-a-qtableview-widget
        roomNum = self.ui.tblCustomer.item(index, 2).text()
        if roomNum.startswith("Room A"):
            with open("Available_Room_A.txt", "a") as roomtext:
                roomtext.write("\n" + roomNum)
        if roomNum.startswith("Room B"):
            with open("Available_Room_B.txt", "a") as roomtext:
                roomtext.write("\n" + roomNum)                
        if roomNum.startswith("Room C"):
            with open("Available_Room_C.txt", "a") as roomtext:
                roomtext.write("\n" + roomNum)
        if roomNum.startswith("Room D"):
            with open("Available_Room_D.txt", "a") as roomtext:
                roomtext.write("\n" + roomNum)                            
        self.ui.tblCustomer.removeRow(index)
    
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
            inclusion = inclusion.replace("\n", "")
            self.ui.roomAText.append(inclusion)
        
        for inclusion in RoomB:
            inclusion = inclusion.replace("\n", "")
            self.ui.roomBText.append(inclusion)
            
        for inclusion in RoomC:
            inclusion = inclusion.replace("\n", "")
            self.ui.roomCText.append(inclusion)        
        
        for inclusion in RoomD:
            inclusion = inclusion.replace("\n", "")
            self.ui.roomDText.append(inclusion)        
        
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        ## BUTTON CLICKS
        self.ui.buttonBox.rejected.connect(self.closeInfo)
        self.ui.buttonBox.accepted.connect(self.saveInfo)

    def closeInfo(self):
        self.parent.show()
        self.close()  
    
    def saveInfo(self):
        # Source: https://stackoverflow.com/questions/2424000/read-and-overwrite-a-file-in-python
        # Get the text from the text boxes
        # Source: https://stackoverflow.com/questions/24035660/how-to-read-from-qtextedit-in-python
        roomADetails = self.ui.roomAText.toPlainText()
        roomBDetails = self.ui.roomBText.toPlainText()
        roomCDetails = self.ui.roomCText.toPlainText()
        roomDDetails = self.ui.roomDText.toPlainText()
        # Then save the text to the text files so the contents will change the next time it loads the GUI
        # The variables look similar but they are not due to capitalization
        # RoomADetails is the open file 
        # roomADetails is the string variable
        with open("Room_A.txt", "w") as RoomADetails:
            RoomADetails.writelines(roomADetails)
        with open("Room_B.txt", "w") as RoomBDetails:
            RoomBDetails.writelines(roomBDetails)     
        with open("Room_C.txt", "w") as RoomCDetails:
            RoomCDetails.writelines(roomCDetails)
        with open("Room_D.txt", "w") as RoomDDetails:
            RoomDDetails.writelines(roomDDetails)
        
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
