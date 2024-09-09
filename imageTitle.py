from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QCoreApplication, Qt , QSize
from PyQt6.QtWidgets import QApplication, QWidget, QLabel,QPushButton, QVBoxLayout \
    ,QHBoxLayout,QGridLayout,QLineEdit,QMessageBox,QGroupBox,QSizePolicy,QSpacerItem
from PyQt6.QtGui import QMouseEvent

class ImageTitle(QWidget):
    def __init__(self):
        super().__init__()
        
        vBoxForm = QVBoxLayout()
        self.setLayout(vBoxForm)

        img = QPixmap('qoogle.png')
        img = img.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        lableImage = QLabel()
        lableImage.setPixmap(img)
        vBoxForm.addWidget(lableImage)








