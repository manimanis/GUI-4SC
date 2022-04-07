from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

def calc_somme():
    # (étape 1) récupérer le contenu des deux champs
    sa = win.txt_a.text()
    sb = win.txt_b.text()
    
    # (étape 2) vérifier la validité des deux champs
    if not sa.isdigit() or not sb.isdigit():
        win.lbl_res.setText("Entrer deux valeurs numériques")
        return
    
    # (étape 3) calculer la somme des deux nombres
    a = int(sa)
    b = int(sb)
    s = a + b
    
    # (étape 4) afficher le résultat
    win.lbl_res.setText(f"Résultat = {s}")

app = QApplication([])
win = uic.loadUi("somme.ui")
win.btn_somme.clicked.connect(calc_somme)
win.show()
app.exec()