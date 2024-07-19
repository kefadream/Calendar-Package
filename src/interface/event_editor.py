"""
Module event_editor
===================

Ce module définit la classe EventEditor qui gère l'édition des événements dans un horaire.

Example:
    event_editor = EventEditor(parent, horaire, time_str, save_callback)
"""
import tkinter as tk
from tkinter import ttk

class EventEditor:
    def __init__(self, parent, horaire, time_str, save_callback):
        """
        Initialiser l'éditeur d'événements.
        Args:
            parent (tk.Toplevel): La fenêtre parente.
            horaire (Horaire): L'objet Horaire contenant les données.
            time_str (str): La chaîne de caractères représentant le temps de l'événement à éditer.
            save_callback (callable): Fonction de rappel pour sauvegarder les données de l'horaire.
        """
        self.horaire = horaire
        self.time_str = time_str
        self.save_callback = save_callback
        self.setup_ui(parent)

    def setup_ui(self, parent):
        """Configurer l'interface utilisateur de l'éditeur d'événements."""
        self.window = tk.Toplevel(parent)
        self.window.title(f"Éditeur d'Horaires - {self.time_str}")
        frame = ttk.Frame(self.window, padding="10")
        frame.pack(fill="both", expand=True)

        self.label_tache = ttk.Label(frame, text="Tâche :")
        self.label_tache.grid(row=0, column=0, sticky="w")

        self.tache_var = tk.StringVar(value=self.horaire.horaire[self.time_str].get('tache', ''))
        self.tache_entry = ttk.Entry(frame, textvariable=self.tache_var)
        self.tache_entry.grid(row=0, column=1, sticky="ew")

        self.label_note = ttk.Label(frame, text="Note :")
        self.label_note.grid(row=1, column=0, sticky="w")

        self.note_var = tk.StringVar(value=self.horaire.horaire[self.time_str].get('note', ''))
        self.note_entry = ttk.Entry(frame, textvariable=self.note_var)
        self.note_entry.grid(row=1, column=1, sticky="ew")

        self.save_button = ttk.Button(frame, text="Sauvegarder", command=self.save)
        self.save_button.grid(row=2, columnspan=2, pady=10)

    def save(self):
        """Sauvegarder les modifications apportées à l'événement."""
        tache = self.tache_var.get().strip()
        note = self.note_var.get().strip()
        self.horaire.ajouter_tache(self.time_str, tache)
        self.horaire.ajouter_note(self.time_str, note)
        self.save_callback(self.horaire)
        self.window.destroy()
