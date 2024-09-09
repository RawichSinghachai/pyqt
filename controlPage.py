from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QCoreApplication, Qt , QSize,QTimer, QDateTime
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QWidget, QLabel,QPushButton, QVBoxLayout \
    ,QHBoxLayout,QGridLayout,QLineEdit,QMessageBox,QGroupBox,QSpacerItem,QTableWidget\
    ,QTableWidgetItem,QHeaderView


from database import Database
from tableUi import TableUi
from leftControlUi import LeftControlUi
from seachBar import SeachBar
from excelButton import ExcelButton
# from editPage import EditPage




class ControlPage(QWidget):
    def __init__(self,stackedWidget):
        super().__init__()

        self.stackedWidget = stackedWidget
        # self.editPage = EditPage(self.stackedWidget)
        # self.stackedWidget.addWidget(self.editPage)

        # Database ------------------------------------------------------------------------------------
        self.db = Database()
        # print(self.db.getAllUser())

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
        vBoxRight.addWidget(self.searchBar)

        # Table
        self.tableUi = TableUi()
        vBoxRight.addWidget(self.tableUi)


        # Excel
        self.excelButton = ExcelButton()
        vBoxRight.addWidget(self.excelButton)
      
        # Get instance
        self.leftControlUi.getEditBtn().clicked.connect(self.openEditPage)



    # Logic ---------------------------------------------------------------------------------------
        self.rowData = ''


    def openEditPage(self):
        print(self.rowData)
        edit_page = self.stackedWidget.widget(3)
        edit_page.populateForm(self.tableUi.getRowData())
        self.stackedWidget.setCurrentWidget(self.stackedWidget.widget(3))

    
   


# app = QCoreApplication.instance()
# if app is None: app = QApplication([])


# window = ControlPage()
# window.show()
# app.exec()