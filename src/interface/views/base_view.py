import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from interface.event_editor import EventEditor
import logging


class BaseCalendarView(tk.Frame):
    def __init__(self, parent, save_callback, view):
        super().__init__(parent)
        self.save_callback = save_callback
        self.view = view
        self.selected_date = datetime.now()
        self.horaire = None
        self.title = "Calendrier"
        self.setup_ui()
        self.pack(fill="both", expand=True)

    def setup_ui(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)

        self.prev_button = ttk.Button(self.main_frame, text="<", command=self.show_prev_period)
        self.prev_button.grid(row=0, column=0, sticky="w")

        self.date_label = ttk.Label(self.main_frame, text=self.selected_date.strftime("%Y-%m-%d"), font=("Helvetica", 16))
        self.date_label.grid(row=0, column=1, sticky="ew")

        self.next_button = ttk.Button(self.main_frame, text=">", command=self.show_next_period)
        self.next_button.grid(row=0, column=2, sticky="e")

        self.canvas_frame = ttk.Frame(self.main_frame)
        self.canvas_frame.grid(row=1, column=0, columnspan=3, sticky="nsew")

        self.canvas = tk.Canvas(self.canvas_frame, bg="white")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', self.on_canvas_configure)

        self.inner_frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(1, weight=1)
        self.inner_frame.columnconfigure(1, weight=1)

    def on_canvas_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def display_horaire(self, horaire):
        self.horaire = horaire
        self.selected_date = horaire.date_debut
        self.update_calendar()

    def update_calendar(self):
        raise NotImplementedError("Cette méthode doit être implémentée par les sous-classes")

    def show_prev_period(self):
        raise NotImplementedError("Cette méthode doit être implémentée par les sous-classes")

    def show_next_period(self):
        raise NotImplementedError("Cette méthode doit être implémentée par les sous-classes")

    def draw_calendar(self):
        raise NotImplementedError("Cette méthode doit être implémentée par les sous-classes")

    def edit_event(self, time_str):
        try:
            editor_window = tk.Toplevel(self)
            editor_window.title(f"Éditeur d'Horaires - {time_str}")
            EventEditor(editor_window, self.horaire, time_str, self.save_callback)
            editor_window.focus()
        except Exception as e:
            logging.error(f"Erreur lors de l'ouverture de l'éditeur d'événements : {e}")
            messagebox.showerror("Erreur", f"Erreur lors de l'ouverture de l'éditeur d'événements : {e}")
