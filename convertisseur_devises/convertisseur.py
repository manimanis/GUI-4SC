from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

def est_reel(ch):
    """Vérifie que ch contient un nombre réel."""
    v = len(ch) > 0
    if v:
        try:
            float(ch)
        except:
            return False
    return v

def convert_tnd():
    # (1) Récupérer le contenu des champs de textes
    seuro = win.txt_euro.text()
    sprix = win.txt_prix_euro.text()
    
    # (2) Vérifier que les champs sont valides
    if est_reel(seuro) and est_reel(sprix):
        # (3) convertir les Euros en TND
        euro = float(seuro)
        prix_euro = float(sprix)
        tnd = euro * prix_euro
        # (4) Afficher le résultat
        win.txt_tnd.setText(f"{tnd}")

def convert_euro():
    # (1) Récupérer le contenu des champs de textes
    stnd = win.txt_tnd.text()
    sprix = win.txt_prix_euro.text()
    
    # (2) Vérifier que les champs sont valides
    if est_reel(stnd) and est_reel(sprix):
        # (3) convertir les TND en Euros
        tnd = float(stnd)
        prix_euro = float(sprix)
        euro = tnd / prix_euro
        # (4) Afficher le résultat
        win.txt_euro.setText(f"{euro}")

app = QApplication([])
win = uic.loadUi("convertisseur.ui")
win.btn_tnd.clicked.connect(convert_tnd)
win.btn_euro.clicked.connect(convert_euro)
win.show()
app.exec()
