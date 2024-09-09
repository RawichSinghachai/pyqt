from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QCoreApplication, Qt , QSize,QTimer, QDateTime
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QWidget, QLabel,QPushButton, QVBoxLayout \
    ,QHBoxLayout,QGridLayout,QLineEdit,QMessageBox,QGroupBox,QSpacerItem,QTableWidget\
    ,QTableWidgetItem,QHeaderView

class LeftControlUi(QWidget):
    def __init__(self):
        super().__init__()

        vBoxLeft = QVBoxLayout()
        vBoxLeft.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(vBoxLeft)

        # Profile Image
        img = QPixmap('profile.png')
        img = img.scaled(150 , 150, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        lableImage = QLabel()
        lableImage.setPixmap(img)
        vBoxLeft.addWidget(lableImage)

        # Edit Button
        self.editBtn = QPushButton('Edit Profile')
        self.editBtn.setStyleSheet('''
            QPushButton {
                background-color:#000000;
                color:white;
                padding:10px;
                font-size:16px;
                font-weight: bold;
            }
            QPushButton::hover {
                background-color:#444444                
            }                 
            ''')
        vBoxLeft.addWidget(self.editBtn) 


        # Add User Button
        addUserBtn = QPushButton('Add User')
        addUserBtn.setStyleSheet('''
            QPushButton {
                background-color:#000000;
                color:white;
                padding:10px;
                font-size:16px;
                font-weight: bold;
            }
            QPushButton::hover {
                background-color:#444444                
            }                 
            ''')
        vBoxLeft.addWidget(addUserBtn) 

        # Testing Button
        testBtn = QPushButton('Test History') 
        testBtn.setStyleSheet('''
            QPushButton {
                background-color:#000000;
                color:white;
                padding:10px;
                font-size:16px;
                font-weight: bold;
            }
            QPushButton::hover {
                background-color:#444444                
            }                 
            ''')
        vBoxLeft.addWidget(testBtn) 

        # Start Button
        startBtn = QPushButton('Start Tetsing') 
        startBtn.setStyleSheet('''
            QPushButton {
                background-color:#6af21c;
                color:white;
                padding:10px;
                font-size:16px;
                font-weight: bold;
            }
            QPushButton::hover {
                background-color:#90f259              
            }                 
            ''')
        vBoxLeft.addWidget(startBtn) 

        # Exit Button
        exitbtn = QPushButton('Exit Program') 
        exitbtn.setStyleSheet('''
            QPushButton {
                background-color:#ff0000;
                color:white;
                padding:10px;
                font-size:16px;
                font-weight: bold;
            }
            QPushButton::hover {
                background-color:#fa4343             
            }                 
            ''')
        vBoxLeft.addWidget(exitbtn) 

        # lable timer
        self.dateLable = QLabel()
        self.dateLable.setStyleSheet("font-size: 8px;")  # Optional styling
        vBoxLeft.addWidget(self.dateLable)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.start(1000)  # Update every 1000 milliseconds (1 second)
        self.updateDateTime()

    # funtion timer
    def updateDateTime(self):
        # Get the current date and time
        current_date_time = QDateTime.currentDateTime()
        # Format it to display as needed
        formatted_date_time = current_date_time.toString("dddd, MMMM d, yyyy hh:mm:ss AP")
        # Update the QLabel with the current date and time
        self.dateLable.setText(formatted_date_time)      


    def getEditBtn(self):
        return self.editBtn