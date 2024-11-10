import cv2
import mediapipe as mp

from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QCoreApplication, Qt , QSize, pyqtSignal,QDate,QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, \
    QHBoxLayout, QGridLayout, QLineEdit, QMessageBox, QGroupBox, QSpacerItem, QStackedWidget,QMainWindow
from PyQt6.QtGui import QIcon,QImage
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
# from testPage import TestPage




class TestPage(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()

        # Create QTimer for frame updates
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils

        # Variable to control camera
        self.cap = None

        self.user_data = {
            'firstName': '',
            'lastName': '',
            'email': '',
            'department': '',
            'gender': '',
            'birthDate': QDate.currentDate().toString('dd/MM/yyyy')
        }

        # Layout Background
        hBox = QHBoxLayout()
        hBox.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(hBox)

        # Widget to display camera feed
        self.image_label = QLabel(self)
        hBox.addWidget(self.image_label)

        # Right Sidebar
        self.sidebar = QVBoxLayout()
        hBox.addLayout(self.sidebar)

        # Example widget in sidebar
        self.firstname_label = QLabel()
        self.sidebar.addWidget(self.firstname_label)

        self.text_countdown = QLabel('10')
        self.sidebar.addWidget(self.text_countdown)

    def open_camera(self):
        # Check if the camera is already open
        if not self.cap:
            self.cap = cv2.VideoCapture(0)
            self.timer.start(30)  # Start QTimer to update frames every 30 ms

    def close_camera(self):
        # Check if there's an open camera
        if self.cap:
            self.timer.stop()  # Stop updating frames
            self.cap.release()  # Release the camera
            self.cap = None  # Reset cap to None
            self.image_label.clear()  # Clear the QLabel image


    def update_frame(self):
        # Check if the camera is open before reading frames
        if self.cap and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                # Process the frame using `process_camera`
                processed_frame = self.process_camera(frame)

                # Get the height, width, and channel of the processed frame
                h, w, _ = processed_frame.shape  # Unpacking with 3 values (height, width, channels)

                qt_image = QImage(processed_frame.data, w, h, QImage.Format.Format_BGR888)

                # Convert QImage to QPixmap and display it in QLabel
                self.image_label.setPixmap(QPixmap.fromImage(qt_image))


    def closeEvent(self, event):
        # Release the camera when closing the app
        self.close_camera()
        event.accept()

    def setUser(self, user_data):
        if user_data:
            self.user_data = user_data
            print(self.user_data)
            self.firstname_label.setText(user_data['FirstName'])

        # Open camera when the page opens
        self.open_camera()

    # -----------------------------------------------------------------------------------------------
    # Instance method to determine left or right hand
    def get_hand_side(self, wrist_x, image_width):
        if wrist_x < image_width / 2:
            return "Left Hand"
        else:
            return "Right Hand"

    # Instance method to determine if hand is front or back with left-right distinction
    def check_hand_orientation(self, landmarks, hand_side):
        palm_center = landmarks[9]
        thumb = landmarks[4]
        pinky = landmarks[20]

        # Check thumb relative position depending on hand side
        if hand_side == "Left Hand":
            if thumb.x > palm_center.x:
                return "Front (Palm)"
            else:
                return "Back (Dorsal)"
        else:
            if thumb.x < palm_center.x:
                return "Front (Palm)"
            else:
                return "Back (Dorsal)"

    # Instance method to process the camera frame and detect hand landmarks
    def process_camera(self, frame):
        """
        Processes the camera frame, detects hands, determines hand side and orientation,
        and draws landmarks and labels.
        """
        # Flip the image horizontally for a later selfie-view display
        frame = cv2.flip(frame, 1)

        # Convert the BGR image to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the image and detect hand landmarks
        with self.mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=2) as hands:
            results = hands.process(frame_rgb)

            # Draw landmarks and check hand orientation for each detected hand
            if results.multi_hand_landmarks:
                for hand_index, hand_landmarks in enumerate(results.multi_hand_landmarks):
                    # Draw hand landmarks on the image
                    self.mp_drawing.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

                    # Determine hand side (left or right)
                    wrist_x = hand_landmarks.landmark[0].x * frame.shape[1]
                    hand_side = self.get_hand_side(wrist_x, frame.shape[1])

                    # Determine orientation (front or back) with respect to hand side
                    orientation = self.check_hand_orientation(hand_landmarks.landmark, hand_side)

                    # Display information near the detected hand
                    h, w, _ = frame.shape
                    cx, cy = int(hand_landmarks.landmark[0].x * w), int(hand_landmarks.landmark[0].y * h)
                    label = f"{hand_side}: {orientation}"
                    cv2.putText(frame, label, (cx, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2, cv2.LINE_AA)

        return frame


class LoginPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python")
        self.setWindowIcon(QIcon("mainWindow.png"))
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

        # Test Page
        self.testPage = TestPage(self.stackedWidget)
        self.stackedWidget.addWidget(self.testPage)



        # Set LoginPage as the initial widget
        # self.stackedWidget.setCurrentWidget(self.loginPageWidget)
        # for test
        # self.stackedWidget.setCurrentWidget(self.testPage)
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
        # print(self.stackedWidget.currentIndex())

    # Keyboard Event 
    def keyPressEvent(self, event):
        if self.stackedWidget.currentIndex() == 0:
            if event.key() == Qt.Key.Key_Enter or event.key() == Qt.Key.Key_Return:
                print("Enter key pressed")
                self.submitLogin()


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