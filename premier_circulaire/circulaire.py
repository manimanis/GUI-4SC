from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def premier(n):
    cpt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cpt = cpt + 1
    return cpt == 2

def rotation(n):
    # [7] [793] est un nombre premier
    # [793] [7] 
    # 7937 est un nombre premier
    # 9377 est un nombre premier
    # 3779 est un nombre premier
    # 7793
    chn = str(n)
    return int(chn[1:] + chn[0])

def circulaire(n):
    if not premier(n):
        return False
    p = rotation(n)
    while p != n and premier(p):
        p = rotation(p)
    return p == n

def verif_circulaire():
    chn = win.txt_n.text()
    if len(chn) > 0 and chn.isdigit():
        n = int(chn)
        if not premier(n):
            msg = "Nombre non premier"
        elif circulaire(n):
            msg = "Nombre premier circulaire"
        else:
            msg = "Nombre premier non circulaire"
    else:
        msg = "Erreur de saisie"
    win.lbl_res.setText(msg)

app = QApplication([])
win = loadUi("circulaire.ui")
win.btn_verif.clicked.connect(verif_circulaire)
win.show()
app.exec()
