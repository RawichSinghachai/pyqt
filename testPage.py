import cv2
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QCoreApplication, Qt , QSize,QTimer, QDateTime,QDate
from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QImage

from camera import process_camera

class TestPage(QWidget):
    def __init__(self,stackedWidget):
        super().__init__()

        # Create QTimer for frame updates
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

        # Variable to control camera
        self.cap = None

        self.user_data = {
            'firstName' : '',
            'lastName' : '',
            'email' : '',
            'department' : '',
            'gender' : '',
            'birthDate' : QDate.currentDate().toString('dd/MM/yyyy')
        }
        # print(self.user_data)
        # -----------------------------------------------------------------------------------------

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
        self.firstname_lable = QLabel()
        self.sidebar.addWidget(self.firstname_lable)

        self.text_countdown = QLabel('10')
        self.sidebar.addWidget(self.text_countdown)

# ----------------------------------------------------------------------------------------------------------
    def open_camera(self):
        # Check if the camera is already open
        if not self.cap:
            self.cap = cv2.VideoCapture(1)
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
                processed_frame = process_camera(frame)
                
                # Get the height, width, and channel of the processed frame
                h, w = processed_frame.shape
                qt_image = QImage(processed_frame.data, w, h, QImage.Format.Format_Grayscale8)
                # qt_image = QImage(processed_frame.data, w, h, QImage.Format.Format_RGB888)

                # Convert QImage to QPixmap and display it in QLabel
                self.image_label.setPixmap(QPixmap.fromImage(qt_image))

    def closeEvent(self, event):
        # Release the camera when closing the app
        self.close_camera()
        event.accept()

    def setUser(self,user_data):
        if user_data:
            self.user_data = user_data
            print(self.user_data)
            self.firstname_lable.setText(user_data['FirstName'])

        # Open camera when the page opens
        self.open_camera()
