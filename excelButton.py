from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QCoreApplication, Qt , QSize,QTimer, QDateTime
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QWidget, QLabel,QPushButton, QVBoxLayout \
    ,QHBoxLayout,QGridLayout,QLineEdit,QMessageBox,QGroupBox,QSpacerItem,QTableWidget\
    ,QTableWidgetItem,QHeaderView

class ExcelButton(QWidget):
    def __init__(self):
        super().__init__()

        hBoxExcel = QHBoxLayout()
        self.setLayout(hBoxExcel)

        # Import Excel Button
        importExcelBtn = QPushButton('Import Excel')
        importExcelBtn.setFixedWidth(250)
        importExcelBtn.setStyleSheet('''
            QPushButton {
                background-color:#0086ff;
                color:white;
                padding:10px;
                font-size:16px;
                font-weight: bold;
            }
            QPushButton::hover {
                background-color:#72b9fa                
            }                 
            ''')
        hBoxExcel.addWidget(importExcelBtn)


        # Export Excel Button
        exportExcelBtn = QPushButton('Import Excel')
        exportExcelBtn.setFixedWidth(250)
        exportExcelBtn.setStyleSheet('''
            QPushButton {
                background-color:#0086ff;
                color:white;
                padding:10px;
                font-size:16px;
                font-weight: bold;
            }
            QPushButton::hover {
                background-color:#72b9fa                
            }                 
            ''')
        hBoxExcel.addWidget(exportExcelBtn)