from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

def verifier(ch):
    return ch.isdigit() and 0 <= int(ch) <= 1000

def calc_somme():
    if not verifier(win.txt_a.text()) or not verifier(win.txt_b.text()):
        win.lbl_res.setText("Erreur")
        return
    
    s = int(win.txt_a.text()) + int(win.txt_b.text())
    win.lbl_res.setText(f"Résultat = {s}")

app = QApplication([])
win = uic.loadUi("somme.ui")
win.btn_somme.clicked.connect(calc_somme)
win.show()
app.exec()