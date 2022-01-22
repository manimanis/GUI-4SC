from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

def verif(ch):
    v = len(ch) > 0
    if v:
        try:
            float(ch)
        except:
            return False
    return v

def convert_tnd():
    if verif(win.txt_euro.text()) and verif(win.txt_prix_euro.text()):
        euro = float(win.txt_euro.text())
        prix_euro = float(win.txt_prix_euro.text())
        tnd = euro * prix_euro
        win.txt_tnd.setText(f"{tnd}")

def convert_euro():
    if verif(win.txt_tnd.text()) and verif(win.txt_prix_euro.text()):
        tnd = float(win.txt_tnd.text())
        prix_euro = float(win.txt_prix_euro.text())
        euro = tnd / prix_euro
        win.txt_euro.setText(f"{euro}")

app = QApplication([])
win = uic.loadUi("convertisseur.ui")
win.btn_tnd.clicked.connect(convert_tnd)
win.btn_euro.clicked.connect(convert_euro)
win.show()
app.exec()
