"""
Module schedule_creator_window
==============================

Ce module contient la classe CreateScheduleWindow qui permet de créer un nouvel horaire à l'aide d'une interface utilisateur graphique.

Classes:
    CreateScheduleWindow: Fenêtre permettant de créer un nouvel horaire.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import logging
from src.core import HoraireCreator


class CreateScheduleWindow:
    """
    Classe représentant une fenêtre de création d'un nouvel horaire.

    Args:
        parent (tk.Tk): La fenêtre parente.
        horaires (dict): Un dictionnaire contenant les horaires existants.
        callback (callable): Fonction de rappel à appeler après la création de l'horaire.
    """

    def __init__(self, parent, horaires, callback):
        self.horaires = horaires
        self.callback = callback
        self.create_window = tk.Toplevel(parent)
        self.create_window.title("Créer un nouvel horaire")
        self.setup_create_ui(self.create_window)

    def setup_create_ui(self, window):
        """
        Configurer l'interface utilisateur pour la création d'un horaire.

        Args:
            window (tk.Toplevel): La fenêtre dans laquelle l'interface utilisateur est créée.
        """
        frame = ttk.Frame(window, padding="10")
        frame.pack(fill="both", expand=True)

        self.label_nom = ttk.Label(frame, text="Nom de l'horaire :")
        self.label_nom.grid(row=0, column=0, sticky="w")

        self.nom_var = tk.StringVar()
        self.nom_entry = ttk.Entry(frame, textvariable=self.nom_var)
        self.nom_entry.grid(row=0, column=1, sticky="ew")

        self.label_saut = ttk.Label(frame, text="Saut de temps :")
        self.label_saut.grid(row=1, column=0, sticky="w")

        self.saut_var = tk.StringVar()
        self.saut_combobox = ttk.Combobox(frame, textvariable=self.saut_var, values=["secondes", "minutes", "heures"])
        self.saut_combobox.grid(row=1, column=1, sticky="ew")

        self.label_intervalle = ttk.Label(frame, text="Intervalle :")
        self.label_intervalle.grid(row=2, column=0, sticky="w")

        self.intervalle_var = tk.StringVar()
        self.intervalle_entry = ttk.Entry(frame, textvariable=self.intervalle_var)
        self.intervalle_entry.grid(row=2, column=1, sticky="ew")

        self.label_debut = ttk.Label(frame, text="Date et heure de début :")
        self.label_debut.grid(row=3, column=0, sticky="w")

        self.debut_year_var = tk.StringVar()
        self.debut_year_combobox = ttk.Combobox(frame, textvariable=self.debut_year_var,
                                                values=[str(i) for i in range(2020, 2031)])
        self.debut_year_combobox.grid(row=3, column=1, sticky="ew")

        self.debut_month_var = tk.StringVar()
        self.debut_month_combobox = ttk.Combobox(frame, textvariable=self.debut_month_var,
                                                 values=[f"{i:02d}" for i in range(1, 13)])
        self.debut_month_combobox.grid(row=3, column=2, sticky="ew")

        self.debut_day_var = tk.StringVar()
        self.debut_day_combobox = ttk.Combobox(frame, textvariable=self.debut_day_var,
                                               values=[f"{i:02d}" for i in range(1, 32)])
        self.debut_day_combobox.grid(row=3, column=3, sticky="ew")

        self.debut_hour_var = tk.StringVar()
        self.debut_hour_combobox = ttk.Combobox(frame, textvariable=self.debut_hour_var,
                                                values=[f"{i:02d}" for i in range(24)])
        self.debut_hour_combobox.grid(row=4, column=1, sticky="ew")

        self.debut_minute_var = tk.StringVar()
        self.debut_minute_combobox = ttk.Combobox(frame, textvariable=self.debut_minute_var,
                                                  values=[f"{i:02d}" for i in range(60)])
        self.debut_minute_combobox.grid(row=4, column=2, sticky="ew")

        self.debut_second_var = tk.StringVar()
        self.debut_second_combobox = ttk.Combobox(frame, textvariable=self.debut_second_var,
                                                  values=[f"{i:02d}" for i in range(60)])
        self.debut_second_combobox.grid(row=4, column=3, sticky="ew")

        self.label_fin = ttk.Label(frame, text="Date et heure de fin :")
        self.label_fin.grid(row=5, column=0, sticky="w")

        self.fin_year_var = tk.StringVar()
        self.fin_year_combobox = ttk.Combobox(frame, textvariable=self.fin_year_var,
                                              values=[str(i) for i in range(2020, 2031)])
        self.fin_year_combobox.grid(row=5, column=1, sticky="ew")

        self.fin_month_var = tk.StringVar()
        self.fin_month_combobox = ttk.Combobox(frame, textvariable=self.fin_month_var,
                                               values=[f"{i:02d}" for i in range(1, 13)])
        self.fin_month_combobox.grid(row=5, column=2, sticky="ew")

        self.fin_day_var = tk.StringVar()
        self.fin_day_combobox = ttk.Combobox(frame, textvariable=self.fin_day_var,
                                             values=[f"{i:02d}" for i in range(1, 32)])
        self.fin_day_combobox.grid(row=5, column=3, sticky="ew")

        self.fin_hour_var = tk.StringVar()
        self.fin_hour_combobox = ttk.Combobox(frame, textvariable=self.fin_hour_var,
                                              values=[f"{i:02d}" for i in range(24)])
        self.fin_hour_combobox.grid(row=6, column=1, sticky="ew")

        self.fin_minute_var = tk.StringVar()
        self.fin_minute_combobox = ttk.Combobox(frame, textvariable=self.fin_minute_var,
                                                values=[f"{i:02d}" for i in range(60)])
        self.fin_minute_combobox.grid(row=6, column=2, sticky="ew")

        self.fin_second_var = tk.StringVar()
        self.fin_second_combobox = ttk.Combobox(frame, textvariable=self.fin_second_var,
                                                values=[f"{i:02d}" for i in range(60)])
        self.fin_second_combobox.grid(row=6, column=3, sticky="ew")

        self.create_button = ttk.Button(frame, text="Créer l'horaire", command=self.creer_horaire)
        self.create_button.grid(row=7, columnspan=4, pady=10)

    def creer_horaire(self):
        """
        Créer un nouvel horaire en utilisant les informations saisies dans l'interface utilisateur.
        """
        try:
            nom = self.nom_var.get().strip()
            if not nom:
                raise ValueError("Le nom de l'horaire ne peut pas être vide.")
            if nom in self.horaires:
                raise ValueError("Un horaire avec ce nom existe déjà.")

            saut_type = self.saut_var.get().strip().lower()
            intervalle = int(self.intervalle_var.get().strip())

            date_debut_str = f"{self.debut_year_var.get()}-{self.debut_month_var.get()}-{self.debut_day_var.get()} {self.debut_hour_var.get()}:{self.debut_minute_var.get()}:{self.debut_second_var.get()}"
            date_fin_str = f"{self.fin_year_var.get()}-{self.fin_month_var.get()}-{self.fin_day_var.get()} {self.fin_hour_var.get()}:{self.fin_minute_var.get()}:{self.fin_second_var.get()}"

            horaire_creator = HoraireCreator(saut_type, intervalle, date_debut_str, date_fin_str)
            horaire = horaire_creator.creer_horaire()
            horaire.nom = nom
            self.horaires[nom] = horaire
            self.callback(horaire)
            self.create_window.destroy()
        except ValueError as e:
            messagebox.showerror("Erreur de création", str(e))
            logging.error(f"Erreur de création : {e}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur inattendue est survenue : {e}")
            logging.error(f"Erreur inattendue : {e}")
