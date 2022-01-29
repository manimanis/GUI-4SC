from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

def premier(n):
    cpt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cpt = cpt + 1
    return cpt == 2

def chance(ch):
    if not (ch.isdigit() and len(ch) == 8 and ch[0] in ["2", "4", "5", "9"]):
        msg = "Vérifier le numéro de téléphone !"
    else:
        msg = "Désolé, vous n'avez pas gagné."
        s = 0
        for i in range(len(ch)):
            s = s + int(ch[i]) * i
        if premier(s):
            msg = "Félicitations, vous avez gagné."
    return msg

def play():
    num_tel = win.txt_tel.text()
    res = chance(num_tel)
    win.lbl_res.setText(res)

app = QApplication([])
win = uic.loadUi("interface_jeu.ui")
win.btn_play.clicked.connect(play)
win.show()
app.exec()

