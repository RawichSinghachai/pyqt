from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QCoreApplication, Qt , QSize,QTimer, QDateTime,QDate
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QWidget, QLabel,QPushButton, QVBoxLayout \
    ,QHBoxLayout,QGridLayout,QLineEdit,QMessageBox,QGroupBox,QSpacerItem,QTableWidget\
    ,QTableWidgetItem,QHeaderView,QDateEdit,QComboBox

from editUserUi import EditUserUi
from database import Database
from messageBox import showMessageBox
from controlPage import ControlPage

class EditPage(QWidget):
    def __init__(self,stackedWidget):
        super().__init__()

        self.stackedWidget = stackedWidget

        self.setWindowTitle("Create User")

        self.setStyleSheet("background-color: #B4B4B4;")
        
        vBox = QVBoxLayout()
        vBox.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(vBox)


        self.title = QLabel('Edit Profile')
        self.title.setStyleSheet(
            """
                font-size: 30px;
                font-weight: bold;
            """
        )
        vBox.addWidget(self.title,alignment=Qt.AlignmentFlag.AlignCenter)

        # Form Login
        self.formEditUi =  EditUserUi()
        vBox.addWidget(self.formEditUi)

        # Database ------------------------------------------------------------------------------------
        self.db = Database()

        # Get instance
        self.formEditUi.getFirstNameInput().textChanged.connect(self.onChangeFirstNameInput)
        self.formEditUi.getLastNameInput().textChanged.connect(self.onChangeLastNameInput)
        self.formEditUi.getEmailInput().textChanged.connect(self.onChangeEmailInput)
        self.formEditUi.getDepartmentInput().textChanged.connect(self.onChangeDepartmentInput)
        self.formEditUi.getGenderInput().currentIndexChanged.connect(self.onChangeGenderInput)
        self.formEditUi.getBirthDateInput().dateChanged.connect(self.onChangeBirthDateInput)

        self.formEditUi.getSubmitButton().clicked.connect(self.submitUserDetail)
        self.formEditUi.getCancelButton().clicked.connect(self.closeEditPage)

        

    # Logic ------------------------------------------------------------------------------------------------

        self.userDetail = {
            'firstName' : '',
            'lastName' : '',
            'email' : '',
            'department' : '',
            'gender' : '',
            'birthDate' : QDate.currentDate().toString('dd/MM/yyyy')
        }
        self.editUserDetail = None

    def onChangeFirstNameInput(self,text):
        self.userDetail['firstName'] = text
        # print(f"firstName: {self.firstName}")

    def onChangeLastNameInput(self,text):
        self.userDetail['lastName'] = text
        # print(f"LastName: {self.lastName}")

    def onChangeEmailInput(self,text):
        self.userDetail['email'] = text
        # print(f"Email: {self.email}")

    def onChangeDepartmentInput(self,text):
        self.userDetail['department'] = text
        # print(f"department: {self.department}")

    def onChangeGenderInput(self,index):
        # Get the current selected text
        selectedGender = self.formEditUi.getGenderInput().currentText()
        
        # Update the label text with the selected gender, or "None" if "Select Gender" is chosen
        if selectedGender == "Select Gender":
            print("Selected Gender: None")
        else:
            self.userDetail['gender'] = selectedGender
            # print(f"Selected Gender: {selectedGender}")

    def onChangeBirthDateInput(self,date):
        # print(f"Selected Date: {date.toString('dd/MM/yyyy')}")
        self.userDetail['birthDate'] = date.toString('dd/MM/yyyy')

    def submitUserDetail(self):
        

        if self.editUserDetail :
            # Update
            self.userDetail.update({'UserId':self.editUserDetail['UserId']})
            # print(self.userDetail)
            editUserStatus = self.db.editUserDetail(self.userDetail)

            if editUserStatus:
                showMessageBox(title='Edit', topic='Edit Success')  # Message Box
                self.stackedWidget.removeWidget(self.stackedWidget.widget(2))
                # Clear Data
                self.clearDataInForm()
                new_page = ControlPage(self.stackedWidget)
                self.stackedWidget.insertWidget(2,new_page)
                self.stackedWidget.setCurrentWidget(new_page)

            else:
                showMessageBox(title='Edit', topic='Edit Fail',mode='error')  # Message Box    

        else:
            # Insert
            createUserStatus =  self.db.createUserDetail(self.userDetail) 

            if createUserStatus:
                showMessageBox(title='Insert', topic='Insert Success')  # Message Box
                # Clear Data
                self.clearDataInForm()

                # Rerender ControlPage
                self.stackedWidget.removeWidget(self.stackedWidget.widget(2))
                new_page = ControlPage(self.stackedWidget)
                self.stackedWidget.insertWidget(2,new_page)
                self.stackedWidget.setCurrentWidget(new_page)

            else:
                showMessageBox(title='Insert', topic='Insert Fail',mode='error')  # Message Box      

    
    def closeEditPage(self):
        # Clear Data
        self.clearDataInForm()

        # Rerender ControlPage
        self.stackedWidget.removeWidget(self.stackedWidget.widget(2))
        new_page = ControlPage(self.stackedWidget)
        self.stackedWidget.insertWidget(2,new_page)
        self.stackedWidget.setCurrentWidget(new_page)




    def populateForm(self,user_data):
        self.editUserDetail = user_data
        if user_data:
            print(f"Populating form with data: {user_data}")
            self.formEditUi.getSubmitButton().setText('Edit')
            # Populate the form fields with the data from user_data
            self.formEditUi.getFirstNameInput().setText(user_data['FirstName'])
            self.formEditUi.getLastNameInput().setText(user_data['LastName'])
            self.formEditUi.getEmailInput().setText(user_data['Email'])
            self.formEditUi.getDepartmentInput().setText(user_data['Department'])
            self.formEditUi.getGenderInput().setCurrentText(user_data['Gender'])
            self.formEditUi.getBirthDateInput().setDate(QDate.fromString(user_data['BirthDate'], "dd/MM/yyyy"))

        else:
            print('No data received')
            self.formEditUi.getSubmitButton().setText('Submit')

    # Clear Data
    def clearDataInForm(self):
        self.formEditUi.getFirstNameInput().clear()
        self.formEditUi.getLastNameInput().clear()
        self.formEditUi.getEmailInput().clear()
        self.formEditUi.getDepartmentInput().clear()
        self.formEditUi.getGenderInput().setCurrentIndex(0)  # Reset to default or first item
        self.formEditUi.getBirthDateInput().setDate(QDate.currentDate()) 



# app = QCoreApplication.instance()
# if app is None: app = QApplication([])



# window = MainWindow()
# window.show()
# app.exec()