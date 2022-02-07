from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def premier(n):
    cpt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cpt = cpt + 1
    return cpt == 2

def rotation(n):
    # 1234
    # 4123
    nch = str(n)
    # dernier caractère de nch est à l'indice -1
    # les n-1 caractères de nch
    return int(nch[-1] + nch[:-1])

def circulaire(n):
    if not premier(n):
        return False
    p = rotation(n)
    while p != n and premier(p):
        p = rotation(p)
    return n == p

def verif_circulaire():
    chn = win.txt_saisie.text()
    if chn.isdigit():
        n = int(chn)
        if not premier(n):
            msg = "Nombre non premier"
        else:
            if circulaire(n):
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



    
        
