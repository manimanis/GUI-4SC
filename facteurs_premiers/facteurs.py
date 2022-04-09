from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


def est_valide(sn):
    if len(sn) == "":
        return False
    if not sn.isdigit():
        return False
    if int(sn) <= 0:
        return False
    return True


def decomposition(n):
    tf = [0]*32
    nf = 0
    f = 2
    while n > 1:
        if n % f == 0:
            tf[nf] = f
            nf = nf + 1
            n = n // f
        elif f == 2:
            f = f + 1
        else:
            f = f + 2
    return nf, tf


def convert_tableau(n, t):
    s = ""
    for i in range(n):
        if i != 0:
            s = s +"*"
        s = s + str(t[i])
    return s


def decomp():
    sn = win.txt_n.text()
    if not est_valide(sn):
        win.lbl_res.setText("Entrer un nombre valide!")
        return
    n = int(sn)
    nf, tf = decomposition(n)
    res = convert_tableau(nf, tf)
    win.lbl_res.setText(f"{n} = {res}")


app = QApplication([])
win = uic.loadUi("facteurs.ui")
win.btn_dec.clicked.connect(decomp)
win.show()
app.exec()
