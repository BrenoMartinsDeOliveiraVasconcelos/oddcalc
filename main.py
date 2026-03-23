import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtCore import QRegularExpression, Qt
from PyQt6.QtGui import QRegularExpressionValidator, QFont
import mathlib

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
        res_font = self.result_label.font()
        res_font.setPointSize(12)
        res_font.setBold(True)

        self.result_label.setFont(res_font)
        result_row.addWidget(self.result_label)


        layout.addLayout(chance_row)
        layout.addLayout(calculate_row)
        layout.addLayout(result_row)


    def on_calculate_click(self):
        if self.x_edit.text() == "" or self.y_edit.text() == "":
            QMessageBox.critical(None, "Erro", "Preencha todos os campos.")
            return


        result_text = ""
        results_strings = []
        result_template = "\\0%: \\1 tentativas"
        percents = [0.001, 0.01, 0.05, 0.10, 0.25, 0.50, 0.80, 0.90,  0.95, 0.99, 0.9999]
        x_val = int(self.x_edit.text())
        y_val = int(self.y_edit.text())

        if x_val <=0 or y_val <=0:
            QMessageBox.warning(None, "Aviso", "Os vlores não podem ser menor ou igual a zero.")

        for p in percents:
            tries = mathlib.calc_tries(p, x_val, y_val) if x_val != y_val else 1

            r_str = result_template.replace("\\0", str(p*100))
            r_str = r_str.replace("\\1", str(tries))

            result_text += r_str+"\n"

        
        self.result_label.setText(result_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OddCalc()
    window.show()
    sys.exit(app.exec())