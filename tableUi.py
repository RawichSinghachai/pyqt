from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QCoreApplication, Qt , QSize,QTimer, QDateTime
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QWidget, QLabel,QPushButton, QVBoxLayout \
    ,QHBoxLayout,QGridLayout,QLineEdit,QMessageBox,QGroupBox,QSpacerItem,QTableWidget\
    ,QTableWidgetItem,QHeaderView
from PyQt6.QtGui import QMouseEvent

from database import Database



class TableUi(QWidget):
    def __init__(self,listUsers):
        super().__init__()

        # Root Layout
        vBox = QVBoxLayout()
        vBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(vBox)

        # Database ------------------------------------------------------------------------------------
        self.db = Database()

        

        # Table 
        self.listUsers = listUsers

        headers = [ 'FirstName', 'LastName','Gender' ,'Department', 'Email','Birthday', 'Delete']
        self.table = QTableWidget(len(self.listUsers),len(headers)) 
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers) # Don't edit data in table
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents) # Don't expand Column Cell
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents) # Don't expand Row Cell

        # Connect the vertical header's sectionClicked signal to the slot
        self.table.verticalHeader().sectionClicked.connect(self.selectRow)

        self.iconDeleteDict = {}

        
        # Set Header Table
        for i ,h in enumerate(headers):
            self.table.setHorizontalHeaderItem(i,QTableWidgetItem(h))

        # fill out Data in table
        for row_index, user  in enumerate(self.listUsers):
            row_data = [
                user['FirstName'],
                user['LastName'],
                user['Gender'],
                user['Department'],
                user['Email'],
                user['BirthDate']
                ]
            UserId = user['UserId']
            for column_index, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
                self.table.setItem(row_index, column_index, item)

                # add delete icon
                # Icon delete
                self.iconDelete = QLabel()
                self.iconDelete.setPixmap(QPixmap('trash.png').scaled(20, 20, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
                self.iconDelete.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.iconDelete.setStyleSheet("""
                    QLabel {
                        background-color: transparent; /* Background color of the icon */
                    }
                """)
                # self.iconDelete.mousePressEvent = self.deleteRow
                
                self.table.setCellWidget(row_index,len(self.listUsers[0])-1,self.iconDelete)

                self.iconDeleteDict[UserId] = self.iconDelete
           



        self.table.setStyleSheet("""
            QTableWidget {
                background-color: #f0f0f0;  /* Background color of the table */
                border: 1px solid #aaa;     /* Border around the table */
                gridline-color: #dddddd;       /* Color of the grid lines */
            }
            QTableWidget::item {
                padding: 5px;               /* Padding inside each cell */
                border: 1px solid #dddddd;     /* Border around each cell */
            }
            QHeaderView::section {
                background-color: #505558;  /* Background color of header sections */
                color: white;               /* Text color of header sections */
                padding: 5px;               /* Padding inside header sections */
                border: 1px solid #2e3a42;  /* Border around header sections */
                font-weight: bold;
            }
            QTableWidget::item:selected {
                background-color: #a8d8d8;  /* Background color of selected items */
                color: black;               /* Text color of selected items */
            }
        """)
        vBox.addWidget(self.table)

        self.rowData = ''

    def selectRow(self,index):
        self.rowData = self.listUsers[index]
        print('select row')
        print(f'selct row data :  {self.rowData}')
        # print(f"Selected Row {index}: {self.rowData}")

    def getRowData(self):
        return self.rowData


    


    
    # def deleteRow(self,event: QMouseEvent):
    #     if event.button() == Qt.MouseButton.LeftButton:
    #         self.db.deleteUser(self.iconDelete.property('UserId'))
    #         print('deleteClick')


