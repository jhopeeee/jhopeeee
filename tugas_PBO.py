import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QDialog


class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pengukur Berat Badan Ideal")
        
        # Membuat widget utama
        widget = QWidget(self)
        self.setCentralWidget(widget)
        
        # Membuat layout utama
        layout = QVBoxLayout(widget)
        
        # Membuat label dan line edit untuk memasukkan tinggi badan
        self.label_tinggi = QLabel("Tinggi Badan (cm):")
        self.lineedit_tinggi = QLineEdit()
        
        # Membuat label dan line edit untuk memasukkan berat badan
        self.label_berat = QLabel("Berat Badan (kg):")
        self.lineedit_berat = QLineEdit()
        
        # Membuat tombol hitung
        self.button_hitung = QPushButton("Hitung")
        self.button_hitung.clicked.connect(self.hitung_berat_ideal)
        
        # Menambahkan widget ke layout
        layout.addWidget(self.label_tinggi)
        layout.addWidget(self.lineedit_tinggi)
        layout.addWidget(self.label_berat)
        layout.addWidget(self.lineedit_berat)
        layout.addWidget(self.button_hitung)
        
    def hitung_berat_ideal(self):
        tinggi = float(self.lineedit_tinggi.text())
        berat = float(self.lineedit_berat.text())
        
        # Menghitung berat badan ideal
        berat_ideal = tinggi - 100 - (0.1 * (tinggi - 100))
        
        # Menghitung selisih berat badan dengan berat badan ideal
        selisih = berat - berat_ideal
        
        # Menampilkan hasil
        dialog = QDialog(self)
        dialog.setWindowTitle("Hasil")
        layout = QVBoxLayout(dialog)
        layout.addWidget(QLabel(f"Berat Badan Ideal: {berat_ideal:.2f} kg"))
        layout.addWidget(QLabel(f"Selisih: {selisih:.2f} kg"))
        dialog.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec_())

