"""
File: horaire_creator.py

Module pour la création d'horaires.
"""

from datetime import datetime
from core import Horaire, SautDeTempsSecondes, SautDeTempsMinutes, SautDeTempsHeures


class HoraireCreator:
    def __init__(self, saut_type, intervalle, date_debut_str, date_fin_str):
        self.saut_type = saut_type
        self.intervalle = intervalle
        self.date_debut_str = date_debut_str
        self.date_fin_str = date_fin_str

    def creer_horaire(self):
        date_debut = datetime.strptime(self.date_debut_str, "%Y-%m-%d %H:%M:%S")
        date_fin = datetime.strptime(self.date_fin_str, "%Y-%m-%d %H:%M:%S")

        if self.saut_type == "secondes":
            saut_de_temps = SautDeTempsSecondes(self.intervalle)
        elif self.saut_type == "minutes":
            saut_de_temps = SautDeTempsMinutes(self.intervalle)
        elif self.saut_type == "heures":
            saut_de_temps = SautDeTempsHeures(self.intervalle)
        else:
            raise ValueError("Type de saut non valide")

        return Horaire(saut_de_temps=saut_de_temps, date_debut=date_debut, date_fin=date_fin)
