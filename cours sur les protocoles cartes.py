
"""
Utilisation de la méthode builtin __iter__ avec le constructeur yield
permet d'utiliser l'iteration (), le listage de données

introduction d'itertools et de la méthode itertools.product
"""

import itertools
from dataclasses import dataclass

@dataclass
class Carte:
    valeur:str
    couleur:str

    def __repr__(self):
        return f"{self.valeur}{self.couleur}"

class Jeu32Cartes:
    couleurs = ["♥","♠","♦","♣"]
    valeurs = ["A", "R", "D", "V","10","9","8","7"]
       
    def __init__(self):
        self._ensemble = list(Carte(valeur,couleur) for (valeur,couleur) in  itertools.product(self.valeurs,self.couleurs))

    def __iter__(self):
        yield from self._ensemble


print(list(Jeu32Cartes()))