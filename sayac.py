import sys
from PyQt5 import QtWidgets
import time


class Windows(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.real_def()

    def real_def(self):

        self.setWindowTitle("Sayaç")
        self.txt = QtWidgets.QLabel("0")
        self.buton = QtWidgets.QPushButton("Tıklayınız...")
        self.sayac = 0
        self.setGeometry(1690, 30, 230, 1018)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.txt)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.buton.clicked.connect(self.tikla)
        self.show()

    def tikla(self):

        self.sayac += 1
        self.txt.setText(str(self.sayac))
        if self.sayac == 10:
            self.txt.setText("Sayaç Tamamlandı...")



app = QtWidgets.QApplication(sys.argv)
pencere = Windows()
sys.exit(app.exec_())