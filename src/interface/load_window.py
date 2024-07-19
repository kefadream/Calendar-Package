"""
Module load_window
==================

Ce module définit la classe LoadWindow qui gère la fenêtre de chargement d'un horaire existant.
Il permet à l'utilisateur de sélectionner et de charger un horaire parmi une liste d'horaires disponibles.

Example:
    load_window = LoadWindow(parent, horaires, callback)
"""

import tkinter as tk
from tkinter import ttk, messagebox


class LoadWindow:
    def __init__(self, parent, horaires, callback):
        """
        Initialiser la fenêtre de chargement d'un horaire existant.

        Args:
            parent (tk.Tk): La fenêtre parent.
            horaires (dict): Le dictionnaire des horaires disponibles.
            callback (callable): La fonction de rappel après le chargement de l'horaire.
        """
        self.horaires = horaires
        self.callback = callback
        self.load_window = tk.Toplevel(parent)
        self.load_window.title("Charger un horaire existant")
        self.setup_load_ui(self.load_window)

    def setup_load_ui(self, window):
        """Configurer l'interface utilisateur pour le chargement d'un horaire."""
        frame = ttk.Frame(window, padding="10")
        frame.pack(fill="both", expand=True)

        self.horaire_listbox = tk.Listbox(frame)
        self.horaire_listbox.grid(row=0, column=0, sticky="nsew")

        for horaire in self.horaires.keys():
            self.horaire_listbox.insert(tk.END, horaire)

        self.load_button = ttk.Button(frame, text="Charger", command=self.charger_horaire)
        self.load_button.grid(row=1, column=0, pady=10)

    def charger_horaire(self):
        """Charger l'horaire sélectionné."""
        selection = self.horaire_listbox.curselection()
        if selection:
            horaire_key = self.horaire_listbox.get(selection[0])
            horaire = self.horaires[horaire_key]
            self.callback(horaire)
            self.load_window.destroy()
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner un horaire à charger.")
