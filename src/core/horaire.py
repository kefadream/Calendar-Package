"""
File: horaire.py

Contient les classes principales pour la gestion des horaires.
"""

from datetime import datetime, timedelta
from .sauts import SautDeTemps


class Horaire:
    def __init__(self, saut_de_temps: SautDeTemps, date_debut: datetime, date_fin: datetime, format_jsonl=False):
        self.saut_de_temps = saut_de_temps
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.horaire = self.generer_horaire()
        self.format_jsonl = format_jsonl

    def generer_horaire(self):
        horaire = {}
        current_time = self.date_debut
        while current_time <= self.date_fin:
            horaire[current_time.strftime("%Y-%m-%d %H:%M:%S")] = {}
            current_time += timedelta(seconds=self.saut_de_temps.seconds)
        return horaire

    def ajouter_tache(self, time_str, tache):
        if time_str in self.horaire:
            self.horaire[time_str]['tache'] = tache
        else:
            raise ValueError("Temps non trouvé dans l'horaire")

    def ajouter_note(self, time_str, note):
        if time_str in self.horaire:
            self.horaire[time_str]['note'] = note
        else:
            raise ValueError("Temps non trouvé dans l'horaire")
