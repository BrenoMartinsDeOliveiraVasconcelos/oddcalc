import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QPushButton
from PyQt6.QtCore import QRegularExpression, Qt
from PyQt6.QtGui import QRegularExpressionValidator

class OddCalc(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title and initial size
        self.setWindowTitle("Empty Grid Window")

        # Create a central widget (required for QMainWindow)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.number_regex = QRegularExpressionValidator(QRegularExpression("^[0-9]{1,}$"))

        # Create a QGridLayout and set it on the central widget
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Chance row
        chance_row = QHBoxLayout()

        chance_label = QLabel("Chances:")
        self.x_edit = QLineEdit()
        self.y_edit = QLineEdit()
        middle_label = QLabel("em")
        middle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.x_edit.setValidator(self.number_regex)
        self.y_edit.setValidator(self.number_regex)

        fraction = QVBoxLayout()
        fraction.addWidget(self.x_edit)
        fraction.addWidget(middle_label)
        fraction.addWidget(self.y_edit)

        chance_row.addWidget(chance_label)
        chance_row.addLayout(fraction)

        # Calc row
        calculate_row = QHBoxLayout()
        
        calc_button = QPushButton("Ok")

        calc_button.clicked.connect(self.on_calculate_click)

        calculate_row.addWidget(calc_button)

        # Result row
        result_row = QHBoxLayout()

        self.result_label = QLabel(" ")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        result_row.addWidget(self.result_label)


        layout.addLayout(chance_row)
        layout.addLayout(calculate_row)
        layout.addLayout(result_row)


    def on_calculate_click(self):
        self.result_label.setText(self.result_label.text()+"\n"+"Ok")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OddCalc()
    window.show()
    sys.exit(app.exec())