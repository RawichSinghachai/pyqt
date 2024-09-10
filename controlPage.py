from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QCoreApplication, Qt , QSize,QTimer, QDateTime
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QWidget, QLabel,QPushButton, QVBoxLayout \
    ,QHBoxLayout,QGridLayout,QLineEdit,QMessageBox,QGroupBox,QSpacerItem,QTableWidget\
    ,QTableWidgetItem,QHeaderView
from PyQt6.QtGui import QMouseEvent


from database import Database
from tableUi import TableUi
from leftControlUi import LeftControlUi
from seachBar import SeachBar
from excelButton import ExcelButton
from messageBox import showMessageBox,showMessageDeleteDialog  




class ControlPage(QWidget):
    def __init__(self,stackedWidget):
        super().__init__()

        self.stackedWidget = stackedWidget
        # self.editPage = EditPage(self.stackedWidget)
        # self.stackedWidget.addWidget(self.editPage)

        # Database ------------------------------------------------------------------------------------
        self.db = Database()
        self.listUsers = self.db.getAllUser()

        # Title Window
        self.setWindowTitle("Table")

        # self.setFixedSize(QSize(800,500))
        self.setStyleSheet("background-color: #B4B4B4;")
        
        hBox = QHBoxLayout()
        hBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(hBox)
        
        # Left ----------------------------------------------------------------------------------------------------
        self.leftControlUi = LeftControlUi()
        hBox.addWidget(self.leftControlUi)
        

# ---------------------------------------------------------------------------------------------------------------------------------------------
        # Right
        vBoxRight = QVBoxLayout()
        vBoxRight.setAlignment(Qt.AlignmentFlag.AlignTop)
        hBox.addLayout(vBoxRight)

        #  SeachBar 
        self.searchBar = SeachBar()
        self.searchBar.setPlaceholderText("Search...")
        self.searchBar.textChanged.connect(self.filterTable)
        vBoxRight.addWidget(self.searchBar)

        # Table
        self.tableUi = TableUi(self.listUsers)
        vBoxRight.addWidget(self.tableUi)


        # Excel
        self.excelButton = ExcelButton()
        vBoxRight.addWidget(self.excelButton)
      
        # Get instance
        self.leftControlUi.getEditBtn().clicked.connect(self.openEditPage)
        # self.tableUi.getIconDelete().mousePressEvent = self.deleteRow



    # Logic ---------------------------------------------------------------------------------------

        for user_id, iconDelete in self.tableUi.iconDeleteDict.items():  # Fix here by accessing the dictionary
            iconDelete.mousePressEvent = lambda event, uid=user_id: self.deleteRow(event, uid)


    def openEditPage(self):
        edit_page = self.stackedWidget.widget(3)
        edit_page.populateForm(self.tableUi.getRowData())
        self.stackedWidget.setCurrentWidget(self.stackedWidget.widget(3))

    # Delete Account
    def deleteRow(self, event: QMouseEvent, user_id):
        if event.button() == Qt.MouseButton.LeftButton:

            response = showMessageDeleteDialog()
            if response == QMessageBox.StandardButton.Yes:
                print(f'Delete clicked for UserId: {user_id}')
                if self.db.deleteUser(user_id):
                    showMessageBox('Delete','User  deleted successfully.')
                    # Refresh Control Page
                    self.refreshControlPage()

            
                else:
                    showMessageBox('Delete','Failed to delete user',mode=('error'))
            else:
                print('User canceled the deletion.')


    # Refresh Control Page
    def refreshControlPage(self):
        self.stackedWidget.removeWidget(self)
        refreshed_page = ControlPage(self.stackedWidget)
        self.stackedWidget.addWidget(refreshed_page)
        self.stackedWidget.setCurrentWidget(refreshed_page)



   


# app = QCoreApplication.instance()
# if app is None: app = QApplication([])


# window = ControlPage()
# window.show()
# app.exec()