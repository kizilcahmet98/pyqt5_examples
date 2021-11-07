import sys
import sqlite3
from PyQt5 import QtWidgets

class Windows(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.real_def()
        self.data_base()

    def data_base(self):

        connect = sqlite3.connect("database.db")
        self.cursor = connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Members (user TEXT, pas TEXT)")

        connect.commit()

    def real_def(self):

        self.text_box2 = QtWidgets.QLabel("Kullancı Adı Girin:")
        self.user_name = QtWidgets.QLineEdit()
        self.text_box3 = QtWidgets.QLabel("Parola Girin:")
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.text_box = QtWidgets.QLabel("\n\n\n")
        self.sing_up = QtWidgets.QPushButton("Kayıt Ol")
        self.log_in = QtWidgets.QPushButton("Giriş Yap")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.text_box2)
        v_box.addWidget(self.user_name)
        v_box.addWidget(self.text_box3)
        v_box.addWidget(self.password)
        v_box.addWidget(self.text_box)
        v_box.addStretch()
        v_box.addWidget(self.sing_up)
        v_box.addWidget(self.log_in)

        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()


        self.setLayout(h_box)
        self.setWindowTitle("Karabey Tech")
        self.log_in.clicked.connect(self.login)
        self.sing_up.clicked.connect(self.singup)
        self.show()

    def singup(self):

        names = self.user_name.text()
        pas_s =  self.password.text()

        connect = sqlite3.connect("database.db")
        self.cursor = connect.cursor()
        self.cursor.execute("INSERT INTO Members VALUES(?, ?)", (names, pas_s))
        connect.commit()
        self.text_box.setText("Kayıt Başarılı")


    def login(self):

        names = self.user_name.text()
        pas_s = self.password.text()

        self.cursor.execute("SELECT * FROM Members WHERE user = ? AND pas = ? ", (names, pas_s))

        data = self.cursor.fetchall()

        if len(data) == 0:
            self.text_box.setText("Kullanıcı veya Parola Hatalı")
        else:
            self.text_box.setText("Giriş Başarılı")


app = QtWidgets.QApplication(sys.argv)

window = Windows()

sys.exit(app.exec_())