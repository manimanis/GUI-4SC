from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

def valide(ch, denom):
    if len(ch) == 0:
        return False
    if ch[0] == '-':
        ch = ch[1:]
    if not ch.isdigit():
        return False
    if denom and int(ch) == 0:
        return False
    return True

def pgcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def simplifier_fraction(a, b):
    p = pgcd(a, b)
    p = a // p
    q = b // p
    return p, q

def calc():
    sa = win.txt_a.text()
    sb = win.txt_b.text()

    win.lbl_num.setText("-")
    win.lbl_denom.setText("-")
    win.lbl_res.setText("")

    if not valide(sa, False):
        win.lbl_res.setText("a n'est pas un entier valide")
        return
    if not valide(sb, True):
        win.lbl_res.setText("b n'est pas un entier non nul valide")
        return
    a = int(sa)
    b = int(sb)
    p, q = simplifier_fraction(a, b)
    win.lbl_num.setText(f"{p}")
    win.lbl_denom.setText(f"{q}")

app = QApplication([])
win = uic.loadUi("fraction.ui")
win.btn_calc.clicked.connect(calc)
win.show()
app.exec()