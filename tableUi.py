from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView
from database import Database


class TableUi(QWidget):
    def __init__(self, listUsers):
        super().__init__()

        # Root Layout
        vBox = QVBoxLayout()
        vBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(vBox)

        # Database
        self.db = Database()

        # Table
        self.listUsers = listUsers
        headers = ['FirstName', 'LastName', 'Gender', 'Department', 'Email', 'Birthday', 'Delete']
        self.table = QTableWidget(len(self.listUsers), len(headers))
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)  # Don't edit data in table

        # Set selection mode to single row selection only
        self.table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)

        # Don't expand cells
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

        # Connect the vertical header's sectionClicked signal to the slot
        self.table.verticalHeader().sectionClicked.connect(self.selectRow)

        self.iconDeleteDict = {}

        # Set Header Table
        for i, h in enumerate(headers):
            self.table.setHorizontalHeaderItem(i, QTableWidgetItem(h))

        # Fill out data in table
        for row_index, user in enumerate(self.listUsers):
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

            # Add delete icon
            iconDelete = QLabel()
            iconDelete.setPixmap(QPixmap('trash.png').scaled(20, 20, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
            iconDelete.setAlignment(Qt.AlignmentFlag.AlignCenter)
            iconDelete.setStyleSheet("""
                QLabel {
                    background-color: transparent;
                }
            """)

            self.table.setCellWidget(row_index, len(headers) - 1, iconDelete)
            self.iconDeleteDict[UserId] = iconDelete

        self.table.setStyleSheet("""
            QTableWidget {
                background-color: #f0f0f0;
                border: 1px solid #aaa;
                gridline-color: #dddddd;
            }
            QTableWidget::item {
                padding: 5px;
                border: 1px solid #dddddd;
            }
            QHeaderView::section {
                background-color: #505558;
                color: white;
                padding: 5px;
                border: 1px solid #2e3a42;
                font-weight: bold;
            }
            QTableWidget::item:selected {
                background-color: #a8d8d8;
                color: black;
            }
        """)
        vBox.addWidget(self.table)

        self.rowData = ''

    def selectRow(self, index):
        self.rowData = self.listUsers[index]

    def getRowData(self):
        return self.rowData
