from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QCoreApplication, Qt , QSize, pyqtSignal
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, \
    QHBoxLayout, QGridLayout, QLineEdit, QMessageBox, QGroupBox, QSpacerItem, QStackedWidget
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

from formLogin import FormLogin
from imageTitle import ImageTitle
from messageBox import showMessageBox
from database import Database
from createAccountPage import CreateAccountPage
from controlPage import ControlPage
from editPage import EditPage
from tableUi import TableUi


class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")

        self.setFixedSize(QSize(800, 500))
        self.setStyleSheet("background-color: #B4B4B4;")
        
        # Root Layout
        vBox = QVBoxLayout()
        vBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(vBox)

        # LoginPage Widget
        self.loginPageWidget = QWidget()
        loginPageVBox = QVBoxLayout()
        loginPageVBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.loginPageWidget.setLayout(loginPageVBox)

        # Title
        self.titleLoginLabel = QLabel('Hand Hygiene Testing')
        self.titleLoginLabel.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.titleLoginLabel.setStyleSheet(
            '''
                font-size: 30px;
                font-weight: bold;
            '''
        )
        loginPageVBox.addWidget(self.titleLoginLabel)

        # Center layout
        hBoxCenter = QHBoxLayout()
        hBoxCenter.setAlignment(Qt.AlignmentFlag.AlignCenter)
        loginPageVBox.addLayout(hBoxCenter)

        # Image Title
        self.imageTitle = ImageTitle()
        hBoxCenter.addWidget(self.imageTitle, alignment=Qt.AlignmentFlag.AlignCenter)

        # FormLogin UI
        self.formLogin = FormLogin()
        hBoxCenter.addWidget(self.formLogin, alignment=Qt.AlignmentFlag.AlignCenter)

        # Stack Widget ----------------------------------------------------------------------------------
        self.stackedWidget = QStackedWidget()
         # Add LoginPage and CreateAccountPage to QStackedWidget
        self.stackedWidget.addWidget(self.loginPageWidget)

        # Create Account Page
        self.createAccountPage = CreateAccountPage(self.stackedWidget)
        self.stackedWidget.addWidget(self.createAccountPage)

        # Control Page
        self.controlPage = ControlPage(self.stackedWidget)
        self.stackedWidget.addWidget(self.controlPage)


        # Edit Page
        self.editPage = EditPage(self.stackedWidget)
        self.stackedWidget.addWidget(self.editPage)



        # Set LoginPage as the initial widget
        self.stackedWidget.setCurrentWidget(self.loginPageWidget)
        # for test
        # self.stackedWidget.setCurrentWidget(self.controlPage)


        vBox.addWidget(self.stackedWidget)

        # ------------------------------------------------------------------------------------------

        # Logic --------------------------------------------------------------------------------------

        # Get UserInput instance
        self.formLogin.getUserInput().textChanged.connect(self.onUserInputChanged)
        # Get PasswordInput instance
        self.formLogin.getPasswordInput().textChanged.connect(self.onPasswordInputChanged)

        # Get signUpBtn instance
        self.formLogin.getSignUpBtn().clicked.connect(self.submitLogin)

        # Get instance of LableToPageRegister
        self.formLogin.getLableToCreateAccountPage().mousePressEvent = self.onClickToCreateAccount

    # Database ------------------------------------------------------------------------------------
        self.db = Database()

    # Event -------------------------------------------------------------------------------------
        self.adminLogin = {
            'username' : '',
            'password' : ''
        }


    def onClickToCreateAccount(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.stackedWidget.setCurrentWidget(self.createAccountPage)  # Switch to CreateAccountPage
            print('Clicked Register label')

    # Get username
    def onUserInputChanged(self, text):
        print(f"Username changed to: {text}")
        self.adminLogin['username'] = text

    # Get password
    def onPasswordInputChanged(self, text):
        print(f"Password changed to: {text}")
        self.adminLogin['password'] = text

    # Submit Login
    def submitLogin(self):
        # Check Login in SQLite; return True when login is successful
        loginStatus = self.db.checkLogin(self.adminLogin)

        if loginStatus:
            showMessageBox(title='Login', topic='Login Success')  # Message Box
            self.stackedWidget.setCurrentWidget(self.controlPage) 
        
        else:
            showMessageBox(title='Login', topic='Login Fail',mode='error')  # Message Box
        
        print(f"Login username: {self.adminLogin['username']} password: {self.adminLogin['password']}")



if __name__ == "__main__":
    app = QCoreApplication.instance()
    if app is None:
        app = QApplication([])

    window = LoginPage()
    window.show()
    app.exec()
