from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QCoreApplication, Qt , QSize,QTimer, QDateTime,QDate
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QWidget, QLabel,QPushButton, QVBoxLayout \
    ,QHBoxLayout,QGridLayout,QLineEdit,QMessageBox,QGroupBox,QSpacerItem,QTableWidget\
    ,QTableWidgetItem,QHeaderView,QDateEdit,QComboBox

class EditUserUi(QWidget):
    def __init__(self):
        super().__init__()
        
        vBox = QVBoxLayout()
        vBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(vBox)

        # Group Row One ----------------------------------------------------------------------------------------
        hBoxRowOne = QHBoxLayout()
        vBox.addLayout(hBoxRowOne)

        # Group FirstName
        vBoxGroupUserName = QVBoxLayout()
        hBoxRowOne.addLayout(vBoxGroupUserName)

        # UserName Lable Input
        self.firstNameLableInput = QLabel('FirstName')
        self.firstNameLableInput.setStyleSheet(
            """
                font-size: 16px;
                font-weight: bold;
            """
        )
        vBoxGroupUserName.addWidget(self.firstNameLableInput)

        # FirstName Input
        self.firstNameInput = QLineEdit()
        self.firstNameInput.setPlaceholderText('Fill UserName')
        self.firstNameInput.setFixedSize(QSize(200,40))
        self.firstNameInput.setStyleSheet(
            """
                background-color: white;
                border: 2px solid black;
                border-radius: 5px;
                padding: 5px;
                font-size : 15px;
            """
        )
        vBoxGroupUserName.addWidget(self.firstNameInput)

        # Group LastName
        vBoxGroupLastName = QVBoxLayout()
        hBoxRowOne.addLayout(vBoxGroupLastName)

        # LastName Lable Input
        self.lastNameLableInput = QLabel('LastName')
        self.lastNameLableInput.setStyleSheet(
            """
                font-size: 16px;
                font-weight: bold;
            """
        )
        vBoxGroupLastName.addWidget(self.lastNameLableInput)

        # LastName Input
        self.lastNameInput = QLineEdit()
        self.lastNameInput.setPlaceholderText('Fill LastName')
        self.lastNameInput.setFixedSize(QSize(200,40))
        self.lastNameInput.setStyleSheet(
            """
                background-color: white;
                border: 2px solid black;
                border-radius: 5px;
                padding: 5px;
                font-size : 15px;
            """
        )
        vBoxGroupLastName.addWidget(self.lastNameInput)


        # Group Row Two ----------------------------------------------------------------------------------------
        hBoxRowTwo = QHBoxLayout()
        vBox.addLayout(hBoxRowTwo)

        # Group Email
        vBoxGroupEmail = QVBoxLayout()
        hBoxRowTwo.addLayout(vBoxGroupEmail)

        # Email Lable Input
        self.emailLableInput = QLabel('Email')
        self.emailLableInput.setStyleSheet(
            """
                font-size: 16px;
                font-weight: bold;
            """
        )
        vBoxGroupEmail.addWidget(self.emailLableInput)

        # Email Input
        self.emailInput = QLineEdit()
        self.emailInput.setPlaceholderText('Fill Email')
        self.emailInput.setFixedSize(QSize(200,40))
        self.emailInput.setStyleSheet(
            """
                background-color: white;
                border: 2px solid black;
                border-radius: 5px;
                padding: 5px;
                font-size : 15px;
            """
        )
        vBoxGroupEmail.addWidget(self.emailInput)

        # Group Role
        vBoxGroupRole = QVBoxLayout()
        hBoxRowTwo.addLayout(vBoxGroupRole)

        # Department Lable Input
        self.departmentLableInput = QLabel('Department')
        self.departmentLableInput.setStyleSheet(
            """
                font-size: 16px;
                font-weight: bold;
            """
        )
        vBoxGroupRole.addWidget(self.departmentLableInput)

        # Department Input
        self.departmentInput = QLineEdit()
        self.departmentInput.setPlaceholderText('Fill Department')
        self.departmentInput.setStyleSheet(
            """
                background-color: white;
                border: 2px solid black;
                border-radius: 5px;
                padding: 5px;
                font-size : 15px;
            """
        )
        self.departmentInput.setFixedSize(QSize(200,40))
        vBoxGroupRole.addWidget(self.departmentInput)


        # Group Row Three ----------------------------------------------------------------------------------------
        hBoxRowThree = QHBoxLayout()
        vBox.addLayout(hBoxRowThree)

        # Group Gender
        vBoxGroupGender = QVBoxLayout()
        hBoxRowThree.addLayout(vBoxGroupGender)

        # Gender Lable Input
        self.genderLableInput = QLabel('Gender')
        self.genderLableInput.setStyleSheet(
            """
                font-size: 16px;
                font-weight: bold;
            """
        )
        vBoxGroupGender.addWidget(self.genderLableInput)

        # Gender Input
        self.genderInput = QComboBox()
        self.genderInput.addItems(["Select Gender", "Male", "Female", "Other"])
        self.genderInput.setCurrentIndex(0)
        self.genderInput.setFixedSize(QSize(200,40))
        self.genderInput.setStyleSheet("""
            QComboBox {
                background-color: #F0F0F0;
                border: 2px solid #000000;
                border-radius: 5px;
                padding: 5px;
                font: 14px Arial;
            }
            QComboBox::drop-down {
                border-left: 2px solid #000000;
                width: 25px;
            }
            QComboBox::down-arrow {
                image: url(caret-down.png); /* Custom arrow icon */
                width: 20px;
                height: 20px;
            }
            QComboBox QAbstractItemView {
                background-color: #F0F0F0;
                border: 2px solid #000000;
                selection-background-color: #5A9;
                selection-color: #000000;
            }
            QComboBox QAbstractItemView::item:selected {
                background-color: #000000; /* Background color of selected item */
                color: #F0F0F0; /* Text color of selected item */
            }
        """)
        vBoxGroupGender.addWidget(self.genderInput)


        # Group Birth Date
        vBoxGroupBirthDate = QVBoxLayout()
        hBoxRowThree.addLayout(vBoxGroupBirthDate)

        # Birth Date Lable Input
        self.birthDateLableInput = QLabel('Birth Date')
        self.birthDateLableInput.setStyleSheet(
            """
                font-size: 16px;
                font-weight: bold;
            """
        )
        vBoxGroupBirthDate.addWidget(self.birthDateLableInput)

        # Birth Date Input
        self.birthDateInput = QDateEdit()
        self.birthDateInput.setCalendarPopup(True)
        self.birthDateInput.setDate(QDate.currentDate())
        self.birthDateInput.setDisplayFormat("dd/MM/yyyy")
        self.birthDateInput.setFixedSize(QSize(200,40))
        self.birthDateInput.setStyleSheet("""
            QDateEdit {
                background-color: #F0F0F0;
                border: 2px solid #000000;
                border-radius: 5px;
                padding: 5px;
                font: 14px Arial;
            }
            QDateEdit::drop-down {
                border-left: 2px solid #000000;
                width: 20px;
            }
            QDateEdit::down-arrow {
                image: url(caret-down.png); /* Custom arrow icon */
                width: 20px;
                height: 20px;
            }
            QCalendarWidget QWidget {
                background-color: #F0F0F0;
            }
            QCalendarWidget QToolButton {
                background-color: #F0F0F0;
                color: #000000;
            }

            QCalendarWidget QAbstractItemView {
                font: 14px Arial;
                background-color: #E1E0B1;
                border: 1px solid #000000;
            }
            QCalendarWidget QTableView::item:selected {
                background-color: #D3A3A3; /* Background color for selected date */
                color: #000000; /* Text color for selected date */
            }                              
        """)
        vBoxGroupBirthDate.addWidget(self.birthDateInput)


        # Button Control
        hBoxButtonControl = QHBoxLayout()
        vBox.addLayout(hBoxButtonControl)

        self.cancelBtn = QPushButton('Cancel')
        self.cancelBtn.setStyleSheet('''
            QPushButton {
                background-color:#f75a6c;
                color:white;
                padding:10px;
                font-size:16px;
                font-weight: bold;
            }
            QPushButton::hover {
                background-color:#f50722                
            }                 
            ''')
        hBoxButtonControl.addWidget(self.cancelBtn)


        self.submitBtn = QPushButton('Submit')
        self.submitBtn.setStyleSheet('''
            QPushButton {
                background-color:#f75a6c;
                color:white;
                padding:10px;
                font-size:16px;
                font-weight: bold;
            }
            QPushButton::hover {
                background-color:#f50722                
            }                 
            ''')
        hBoxButtonControl.addWidget(self.submitBtn)


    # Export parameter -------------------------------------------------------------------------

    def getFirstNameInput(self):
        return self.firstNameInput
    
    def getLastNameInput(self):
        return self.lastNameInput
    
    def getEmailInput(self):
        return self.emailInput
    
    def getDepartmentInput(self):
        return self.departmentInput
    
    def getGenderInput(self):
        return self.genderInput
    
    def getBirthDateInput(self):
        return self.birthDateInput
    
    def getCancelButton(self):
        return self.cancelBtn
    
    def getSubmitButton(self):
        return self.submitBtn
    

    