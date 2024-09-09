from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QCoreApplication, Qt , QSize,QTimer, QDateTime
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QWidget, QLabel,QPushButton, QVBoxLayout \
    ,QHBoxLayout,QGridLayout,QLineEdit,QMessageBox,QGroupBox,QSpacerItem,QTableWidget\
    ,QTableWidgetItem,QHeaderView

from database import Database


class TableUi(QWidget):
    def __init__(self,listUsers=[]):
        super().__init__()

        # Root Layout
        vBox = QVBoxLayout()
        vBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(vBox)

        # Database ------------------------------------------------------------------------------------
        self.db = Database()
        # print(self.db.getAllUser())
        self.listUsers = self.db.getAllUser()

        # Table 
        # self.listUsers = self.showdata()

        # demo_data = [
        # ['John', 'Doe', 'Male', 'HR', 'John@gmail', '1990-01-01'],  # False means not deleted
        # ['Jane', 'Smith', 'Female', 'IT', 'Jane@gmail', '1992-02-02'],
        # ['Alice', 'Johnson', 'Female', 'EN', 'Alice@gmail', '1993-03-03']
        #     ]
        headers = [ 'FirstName', 'LastName','Gender' ,'Department', 'Email','Birthday', 'Delete']
        self.table = QTableWidget(len(self.listUsers),len(headers)) 
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers) # Don't edit data in table
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents) # Don't expand Column Cell
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents) # Don't expand Row Cell

        # Connect the vertical header's sectionClicked signal to the slot
        self.table.verticalHeader().sectionClicked.connect(self.selectRow)



        
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
            for column_index, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
                self.table.setItem(row_index, column_index, item)

                # add delete icon
                # Icon delete
                iconDelete = QLabel()
                iconDelete.setPixmap(QPixmap('trash.png').scaled(20, 20, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
                iconDelete.setAlignment(Qt.AlignmentFlag.AlignCenter)
                iconDelete.setStyleSheet("""
                    QLabel {
                        background-color: transparent; /* Background color of the icon */
                    }
                """)
                self.table.setCellWidget(row_index,len(self.listUsers[0])-1,iconDelete)


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

    def getTable(self):
        return self.table
    

    def showdata(self):
        return self.db.getAllUser()


    
    # def updateTable(self, users):
    #     self.setRowCount(len(users))
    #     for row_index, user in enumerate(users):
    #         self.setItem(row_index, 0, QTableWidgetItem(user['FirstName']))
    #         self.setItem(row_index, 1, QTableWidgetItem(user['LastName']))
    #         self.setItem(row_index, 2, QTableWidgetItem(user['Gender']))
    #         self.setItem(row_index, 3, QTableWidgetItem(user['Department']))
    #         self.setItem(row_index, 4, QTableWidgetItem(user['Email']))
    #         self.setItem(row_index, 5, QTableWidgetItem(user['BirthDate']))