from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

def valide(ch):
    if len(ch) == 0:
        return False
    if not (0 <= int(ch) < 256):
        return False
    return True

def conv_bin(n, b):
    s = ""
    for i in range(b):
        s = str(n % 2) + s
        n = n // 2
    return s

def naturel_reflechi(nat):
    return nat ^ (nat // 2)

def convert():
    snbr = win.txt_decimal.text()
    win.txt_naturel.setText(f"-")
    win.txt_reflechi.setText(f"-")
    win.lbl_err.setText(f"-")
    if not valide(snbr):
        win.lbl_err.setText("Entrer un nombre entre 0 et 255")
        return
    
    nbr = int(snbr)
    bn = conv_bin(nbr, 8)
    br = conv_bin(naturel_reflechi(nbr), 8)
    win.txt_naturel.setText(f"{bn}")
    win.txt_reflechi.setText(f"{br}")

app = QApplication([])
win = uic.loadUi("reflechi.ui")
win.btn_convert.clicked.connect(convert)
win.show()
app.exec()