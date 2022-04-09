from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


def est_valide(sn):
    """Retourne True si sn contient un nombre entier valide"""
    pass


def decomposition(n):
    """Retourne la décomposition en nombres du facteurs premiers"""
    tf = [0]*32
    nf = 0
    # A faire
    return nf, tf


def convert_tableau(n, t):
    """Retourne un tableau en une chaîne de caractères"""
    return ""


def decomp():
    """Gestionnaire de l'évènements clicked de btn_dec"""
    pass

app = QApplication([])
win = uic.loadUi("decomposition.ui")
win.btn_dec.clicked.connect(decomp)
win.show()
app.exec()