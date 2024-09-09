from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import QTimer, QDateTime
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Real-Time Date and Time")

        # Create a QLabel to display the date and time
        self.date_time_label = QLabel()
        self.date_time_label.setStyleSheet("font-size: 18px;")  # Optional styling

        # Set up a layout
        layout = QVBoxLayout()
        layout.addWidget(self.date_time_label)
        self.setLayout(layout)

        # Set up a QTimer to update the QLabel every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_date_time)
        self.timer.start(1000)  # Update every 1000 milliseconds (1 second)

        # Initialize the date and time display
        self.update_date_time()

    def update_date_time(self):
        # Get the current date and time
        current_date_time = QDateTime.currentDateTime()
        # Format it to display as needed
        formatted_date_time = current_date_time.toString("dddd, MMMM d, yyyy hh:mm:ss AP")
        # Update the QLabel with the current date and time
        self.date_time_label.setText(formatted_date_time)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
