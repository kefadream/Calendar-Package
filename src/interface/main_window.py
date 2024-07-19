"""
Module main_window.py
==================

Ce module définit la classe MainWindow qui gère la fenêtre principale de l'application de gestion des horaires.

Classes:
    MainWindow: Fenêtre principale de l'application de gestion des horaires.
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
import json
import os
import threading
import logging

from .create_schedule_window import CreateScheduleWindow
from .load_window import LoadWindow
from .views import DailyViewWindow, WeeklyViewWindow, MonthlyViewWindow

from src.core import Horaire, SautDeTempsSecondes, SautDeTempsMinutes, SautDeTempsHeures, HoraireCreator
from src.config import load_config, save_config
from src.exceptions import *


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class MainWindow(tk.Tk):
    """
    Classe représentant la fenêtre principale de l'application de gestion des horaires.
    """

    def __init__(self):
        """
        Initialiser la fenêtre principale.
        """
        super().__init__()
        self.title("Gestion d'Horaires")
        self.horaires = {}
        self.current_horaire = None
        self.settings = load_config()
        self.directory = self.settings.get('directory', 'horaires')
        self.setup_ui()
        self.load_horaires()

    def setup_ui(self):
        """
        Configurer l'interface utilisateur de la fenêtre principale.
        """
        self.create_menu()

        self.main_frame = ttk.Frame(self, padding="10")
        self.main_frame.pack(fill="both", expand=True)

        self.menu_frame = ttk.Frame(self.main_frame)
        self.menu_frame.grid(row=0, column=0, sticky="ew")

        self.create_button = ttk.Button(self.menu_frame, text="Créer un nouvel horaire", command=self.creer_horaire_ui)
        self.create_button.grid(row=0, column=0, padx=5, pady=5)

        self.create_example_button = ttk.Button(self.menu_frame, text="Créer un exemple d'horaire",
                                                command=self.creer_horaire_exemple)
        self.create_example_button.grid(row=0, column=1, padx=5, pady=5)

        self.load_button = ttk.Button(self.menu_frame, text="Charger un horaire existant",
                                      command=self.charger_horaire_ui)
        self.load_button.grid(row=0, column=2, padx=5, pady=5)

        self.save_button = ttk.Button(self.menu_frame, text="Sauvegarder l'horaire actuel",
                                      command=self.sauvegarder_horaire)
        self.save_button.grid(row=0, column=3, padx=5, pady=5)

        self.select_folder_button = ttk.Button(self.menu_frame, text="Sélectionner le dossier des horaires",
                                               command=self.select_folder)
        self.select_folder_button.grid(row=0, column=4, padx=5, pady=5)

        self.horaire_listbox = tk.Listbox(self.main_frame)
        self.horaire_listbox.grid(row=1, column=0, sticky="nsew")
        self.horaire_listbox.bind('<<ListboxSelect>>', self.on_horaire_selected)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

    def create_menu(self):
        """
        Créer le menu de la fenêtre principale.
        """
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Fichier", menu=file_menu)
        file_menu.add_command(label="Créer un nouvel horaire", command=self.creer_horaire_ui)
        file_menu.add_command(label="Créer un exemple d'horaire", command=self.creer_horaire_exemple)
        file_menu.add_command(label="Charger un horaire existant", command=self.charger_horaire_ui)
        file_menu.add_command(label="Sauvegarder l'horaire actuel", command=self.sauvegarder_horaire)
        file_menu.add_separator()
        file_menu.add_command(label="Quitter", command=self.quit)

        view_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Affichage", menu=view_menu)
        view_menu.add_command(label="Vue quotidienne", command=self.afficher_vue_quotidienne)
        view_menu.add_command(label="Vue hebdomadaire", command=self.afficher_vue_hebdomadaire)

    def afficher_vue_quotidienne(self):
        """
        Afficher la vue quotidienne de l'horaire actuel.
        """
        try:
            if self.current_horaire:
                DailyViewWindow(tk.Toplevel(self), self.sauvegarder_horaire).display_horaire(self.current_horaire)
            else:
                raise HoraireError("Aucun horaire sélectionné pour afficher la vue quotidienne.")
        except HoraireError as e:
            messagebox.showerror("Erreur", str(e))
            logging.error(str(e))

    def afficher_vue_hebdomadaire(self):
        """
        Afficher la vue hebdomadaire de l'horaire actuel.
        """
        try:
            if self.current_horaire:
                WeeklyViewWindow(tk.Toplevel(self), self.sauvegarder_horaire).display_horaire(self.current_horaire)
            else:
                raise HoraireError("Aucun horaire sélectionné pour afficher la vue hebdomadaire.")
        except HoraireError as e:
            messagebox.showerror("Erreur", str(e))
            logging.error(str(e))

    def afficher_vue_mensuelle(self):
        """
        Afficher la vue mensuelle de l'horaire actuel.
        """
        try:
            if self.current_horaire:
                MonthlyViewWindow(tk.Toplevel(self), self.sauvegarder_horaire).display_horaire(self.current_horaire)
            else:
                raise HoraireError("Aucun horaire sélectionné pour afficher la vue mensuelle.")
        except HoraireError as e:
            messagebox.showerror("Erreur", str(e))
            logging.error(str(e))

    def creer_horaire_ui(self):
        """
        Ouvrir l'interface utilisateur pour créer un nouvel horaire.
        """
        CreateScheduleWindow(self, self.horaires, self.on_new_horaire_created)

    def creer_horaire_exemple(self):
        """
        Créer un exemple d'horaire.
        """
        nom = "Exemple 1"
        saut_type = "heures"
        intervalle = 1
        date_debut_str = "2024-07-19 00:00:00"
        date_fin_str = "2024-12-31 23:00:00"
        try:
            horaire_creator = HoraireCreator(saut_type, intervalle, date_debut_str, date_fin_str)
            horaire = horaire_creator.creer_horaire()
            horaire.nom = nom
            self.horaires[nom] = horaire
            self.on_new_horaire_created(horaire)
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la création de l'exemple d'horaire : {e}")
            logging.error(f"Erreur lors de la création de l'exemple d'horaire : {e}")

    def charger_horaire_ui(self):
        """
        Ouvrir l'interface utilisateur pour charger un horaire existant.
        """
        LoadWindow(self, self.horaires, self.on_horaire_loaded)

    def on_new_horaire_created(self, horaire):
        """
         Callback après la création d'un nouvel horaire.

         Args:
             horaire.nom (Horaire): Le nouvel horaire créé.
         """
        self.current_horaire = horaire
        self.horaires[horaire.nom] = horaire
        self.update_horaire_list()
        self.sauvegarder_horaire(horaire)

    def on_horaire_loaded(self, horaire):
        """
        Callback après le chargement d'un horaire.

        Args:
            horaire (Horaire): L'horaire chargé.
        """
        self.current_horaire = horaire
        DailyViewWindow(tk.Toplevel(self), self.sauvegarder_horaire).display_horaire(horaire)

    def on_horaire_selected(self, event):
        """
        Callback lorsque un horaire est sélectionné dans la liste.

        Args:
            event (tk.Event): L'événement de sélection.
        """
        selection = self.horaire_listbox.curselection()
        if selection:
            horaire_key = self.horaire_listbox.get(selection[0])
            self.current_horaire = self.horaires[horaire_key]
            DailyViewWindow(tk.Toplevel(self), self.sauvegarder_horaire).display_horaire(self.current_horaire)


    def sauvegarder_horaire(self, horaire=None):
        """
        Sauvegarder l'horaire actuel.

        Args:
            horaire (Horaire, optional): L'horaire à sauvegarder. Si None, l'horaire actuel est sauvegardé.
        """
        if horaire is None:
            horaire = self.current_horaire

        if horaire:
            if not os.path.exists(self.directory):
                os.makedirs(self.directory)
            fichier = os.path.join(self.directory, f"{horaire.nom}.json")
            try:
                with open(fichier, 'w', encoding='utf-8') as json_file:
                    json.dump(horaire.horaire, json_file, indent=4, ensure_ascii=False)
                messagebox.showinfo("Sauvegarde réussie", f"L'horaire a été sauvegardé avec succès dans {fichier}.")
                logging.info(f"L'horaire {horaire.nom} a été sauvegardé avec succès dans {fichier}.")
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors de la sauvegarde du fichier : {e}")
                logging.error(f"Erreur lors de la sauvegarde du fichier : {e}")
        else:
            messagebox.showerror("Erreur", "Aucun horaire à sauvegarder.")
            logging.error("Aucun horaire à sauvegarder.")

    def load_horaires(self):
        """
        Charger tous les horaires depuis le dossier configuré.
        """
        threading.Thread(target=self._load_horaires_thread).start()

    def _load_horaires_thread(self):
        """
        Thread de chargement des horaires.
        """
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        horaire_files = [f for f in os.listdir(self.directory) if f.endswith('.json')]
        for fichier in horaire_files:
            try:
                with open(os.path.join(self.directory, fichier), 'r', encoding='utf-8') as json_file:
                    horaire_data = json.load(json_file)
                    date_debut_str = list(horaire_data.keys())[0]
                    date_debut = datetime.strptime(date_debut_str, "%Y-%m-%d %H:%M:%S")
                    date_fin = datetime.strptime(list(horaire_data.keys())[-1], "%Y-%m-%d %H:%M:%S")
                    intervalle = (datetime.strptime(list(horaire_data.keys())[1], "%Y-%m-%d %H:%M:%S") - date_debut).seconds
                    if intervalle == 1:
                        saut_de_temps = SautDeTempsSecondes(intervalle)
                    elif intervalle == 60:
                        saut_de_temps = SautDeTempsMinutes(intervalle // 60)
                    elif intervalle == 3600:
                        saut_de_temps = SautDeTempsHeures(intervalle // 3600)
                    else:
                        raise IntervalleInvalideError("Intervalle non valide")
                    horaire = Horaire(saut_de_temps=saut_de_temps, date_debut=date_debut, date_fin=date_fin)
                    horaire.horaire = horaire_data
                    nom = os.path.splitext(fichier)[0]
                    horaire.nom = nom
                    self.horaires[nom] = horaire
                    logging.info(f"L'horaire {nom} a été chargé avec succès.")
            except IntervalleInvalideError as e:
                messagebox.showerror("Erreur", f"Erreur lors du chargement du fichier {fichier} : {e}")
                logging.error(f"Erreur lors du chargement du fichier {fichier} : {e}")
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors du chargement du fichier {fichier} : {e}")
                logging.error(f"Erreur lors du chargement du fichier {fichier} : {e}")

        self.update_horaire_list()

    def update_horaire_list(self):
        """
        Mettre à jour la liste des horaires affichés dans la fenêtre principale.
        """
        self.horaire_listbox.delete(0, tk.END)
        for horaire in self.horaires.keys():
            self.horaire_listbox.insert(tk.END, horaire)

    def select_folder(self):
        """
        Sélectionner le dossier où les horaires sont sauvegardés.
        """
        folder_selected = filedialog.askdirectory(initialdir=self.directory,
                                                  title="Sélectionner le dossier des horaires")
        if folder_selected:
            self.directory = folder_selected
            self.settings['directory'] = folder_selected
            save_config(self.settings)
            self.load_horaires()
            messagebox.showinfo("Dossier sélectionné", f"Le dossier des horaires a été défini sur : {self.directory}")
            logging.info(f"Le dossier des horaires a été défini sur : {self.directory}")


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
