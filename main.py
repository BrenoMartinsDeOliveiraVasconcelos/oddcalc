import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout

class OddCalc(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title and initial size
        self.setWindowTitle("Empty Grid Window")
        self.resize(400, 300)

        # Create a central widget (required for QMainWindow)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a QGridLayout and set it on the central widget
        layout = QGridLayout()
        central_widget.setLayout(layout)

        # The layout is empty – you can add widgets later as needed

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OddCalc()
    window.show()
    sys.exit(app.exec())