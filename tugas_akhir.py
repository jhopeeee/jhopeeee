import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikasi GUI Sederhana")
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel("Masukkan Nama:", self)
        self.label.move(50, 50)

        self.textbox = QLineEdit(self)
        self.textbox.move(150, 50)
        self.textbox.resize(100, 20)

        self.button = QPushButton("Submit", self)
        self.button.move(150, 100)
        self.button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        input_text = self.textbox.text()
        self.label.setText("Halo, " + input_text + "!")
        self.textbox.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
