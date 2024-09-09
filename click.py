from PyQt6.QtWidgets import QLabel, QApplication, QMessageBox, QVBoxLayout, QWidget
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtCore import Qt

app = QApplication([])

def on_label_click(event: QMouseEvent):
    if event.button() == Qt.MouseButton.LeftButton:
        QMessageBox.information(None, "Clicked!", "You clicked the label!")

window = QWidget()
layout = QVBoxLayout()

label = QLabel("Click me!")
label.mousePressEvent = on_label_click  # Override the mousePressEvent

layout.addWidget(label)
window.setLayout(layout)
window.show()

app.exec()
