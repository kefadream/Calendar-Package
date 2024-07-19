import tkinter as tk
from tkinter import ttk
from datetime import timedelta
from .base_view import BaseCalendarView
from core import HoraireEditor


class DailyViewWindow(BaseCalendarView):
    def __init__(self, parent, save_callback):
        super().__init__(parent, save_callback, "daily")

    def update_calendar(self):
        self.date_label.config(text=self.selected_date.strftime("%Y-%m-%d"))
        for widget in self.inner_frame.winfo_children():
            widget.destroy()
        self.draw_calendar()

    def show_prev_period(self):
        self.selected_date -= timedelta(days=1)
        self.update_calendar()

    def show_next_period(self):
        self.selected_date += timedelta(days=1)
        self.update_calendar()

    def draw_calendar(self):
        if self.horaire:
            start_hour = 0
            end_hour = 24
            hour_height = 40

            for hour in range(start_hour, end_hour):
                y = hour * hour_height
                hour_label = ttk.Label(self.inner_frame, text=f"{hour:02d}:00", width=10)
                hour_label.grid(row=hour, column=0, sticky="w")

                task_frame = ttk.Frame(self.inner_frame)
                task_frame.grid(row=hour, column=1, sticky="ew")

                note_frame = ttk.Frame(self.inner_frame)
                note_frame.grid(row=hour, column=2, sticky="ew")

                for minute in range(0, 60, self.horaire.saut_de_temps.seconds // 60):
                    time_str = f"{self.selected_date.strftime('%Y-%m-%d')} {hour:02d}:{minute:02d}:00"
                    if time_str in self.horaire.horaire:
                        task_text = self.horaire.horaire[time_str].get('tache', '')
                        note_text = self.horaire.horaire[time_str].get('note', '')

                        if task_text:
                            task_label = ttk.Label(task_frame, text=f"{minute:02d}m - {task_text}", background="lightblue", width=30, anchor="w")
                            task_label.pack(fill=tk.X, padx=5, pady=2)

                        if note_text:
                            note_label = ttk.Label(note_frame, text=f"{minute:02d}m - {note_text}", background="lightgreen", width=30, anchor="w")
                            note_label.pack(fill=tk.X, padx=5, pady=2)

                edit_button = ttk.Button(self.inner_frame, text="Edit", command=lambda ts=time_str: self.edit_event(ts))
                edit_button.grid(row=hour, column=3, sticky="e")

    def edit_event(self, time_str):
        editor = HoraireEditor(self, self.horaire, self.save_callback)
        editor.setup_ui(time_str)
