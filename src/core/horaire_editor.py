import tkinter as tk
from tkinter import ttk, messagebox

class HoraireEditor:
    def __init__(self, parent, horaire, save_callback):
        self.horaire = horaire
        self.save_callback = save_callback
        self.window = tk.Toplevel(parent)
        self.window.title("Éditeur d'Horaires")

    def setup_ui(self, time_str):
        self.time_str = time_str
        self.frame = ttk.Frame(self.window, padding="10")
        self.frame.pack(fill="both", expand=True)

        self.label_time = ttk.Label(self.frame, text="Temps :")
        self.label_time.grid(row=0, column=0, sticky="w")

        self.time_var = tk.StringVar(value=self.time_str)
        self.time_entry = ttk.Entry(self.frame, textvariable=self.time_var, state='readonly')
        self.time_entry.grid(row=0, column=1, sticky="ew")

        self.label_tache = ttk.Label(self.frame, text="Tâche :")
        self.label_tache.grid(row=1, column=0, sticky="w")

        self.tache_var = tk.StringVar(value=self.horaire.horaire[self.time_str].get('tache', ''))
        self.tache_entry = ttk.Entry(self.frame, textvariable=self.tache_var)
        self.tache_entry.grid(row=1, column=1, sticky="ew")

        self.label_note = ttk.Label(self.frame, text="Note :")
        self.label_note.grid(row=2, column=0, sticky="w")

        self.note_var = tk.StringVar(value=self.horaire.horaire[self.time_str].get('note', ''))
        self.note_entry = ttk.Entry(self.frame, textvariable=self.note_var)
        self.note_entry.grid(row=2, column=1, sticky="ew")

        self.save_button = ttk.Button(self.frame, text="Sauvegarder", command=self.save)
        self.save_button.grid(row=3, columnspan=2, pady=10)

    def save(self):
        tache = self.tache_var.get().strip()
        note = self.note_var.get().strip()
        self.horaire.ajouter_tache(self.time_str, tache)
        self.horaire.ajouter_note(self.time_str, note)
        self.save_callback(self.horaire)
        self.window.destroy()
        messagebox.showinfo("Succès", "Tâche/Note ajoutée avec succès")
