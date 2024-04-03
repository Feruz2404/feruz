import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton


class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password Generator")
        self.setGeometry(200, 200, 300, 150)

        layout = QVBoxLayout()

        self.length_label = QLabel("Length:")
        self.length_input = QLineEdit()
        layout.addWidget(self.length_label)
        layout.addWidget(self.length_input)

        self.include_symbols_label = QLabel("Include Symbols:")
        self.include_symbols_input = QLineEdit()
        layout.addWidget(self.include_symbols_label)
        layout.addWidget(self.include_symbols_input)

        self.generate_button = QPushButton("Generate Password")
        self.generate_button.clicked.connect(self.generate_password)
        layout.addWidget(self.generate_button)

        self.password_label = QLabel("")
        layout.addWidget(self.password_label)

        self.setLayout(layout)

    def generate_password(self):
        length = int(self.length_input.text())
        include_symbols = self.include_symbols_input.text()

        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        if include_symbols.lower() == "yes":
            chars += "!@#$%^&*()_+-=[]{}|;:,.<>?/~"

        password = "".join(random.choice(chars) for _ in range(length))
        self.password_label.setText("Generated Password: " + password)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec_())
