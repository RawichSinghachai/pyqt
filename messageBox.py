from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QCoreApplication, Qt , QSize
from PyQt6.QtWidgets import QApplication, QWidget, QLabel,QPushButton, QVBoxLayout \
    ,QHBoxLayout,QGridLayout,QLineEdit,QMessageBox,QGroupBox,QSpacerItem


def showMessageBox(title,topic,mode='info'):
    
    if(mode == 'info'):
        icon = QMessageBox.Icon.Information
    elif(mode == 'warn'):
        icon = QMessageBox.Icon.Warning
    elif(mode == 'error'):
        icon = QMessageBox.Icon.Critical

    msgBox = QMessageBox()
    msgBox.setWindowTitle(title)
    msgBox.setText(topic)
    msgBox.setIcon(icon)
    msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
    msgBox.exec()

def showMessageDeleteDialog():
    msgBox = QMessageBox()
    msgBox.setWindowTitle('Delete Accout')
    msgBox.setText('Are you sure you want to delete this item?')
    msgBox.setStandardButtons(QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes)
    msgBox.setDefaultButton(QMessageBox.StandardButton.Yes)
    response = msgBox.exec()
    return response  
    