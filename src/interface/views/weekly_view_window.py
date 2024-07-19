import tkinter as tk
from tkinter import ttk
from datetime import timedelta
from .base_view import BaseCalendarView


class WeeklyViewWindow(BaseCalendarView):
    def __init__(self, parent, save_callback):
        super().__init__(parent, save_callback, "weekly")

    def update_calendar(self):
        start_of_week = self.selected_date - timedelta(days=self.selected_date.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        self.date_label.config(text=f"Semaine du {start_of_week.strftime('%Y-%m-%d')} au {end_of_week.strftime('%Y-%m-%d')}")
        for widget in self.inner_frame.winfo_children():
            widget.destroy()
        self.draw_calendar()

    def show_prev_period(self):
        self.selected_date -= timedelta(weeks=1)
        self.update_calendar()

    def show_next_period(self):
        self.selected_date += timedelta(weeks=1)
        self.update_calendar()

    def draw_calendar(self):
        if self.horaire:
            start_of_week = self.selected_date - timedelta(days=self.selected_date.weekday())
            end_of_week = start_of_week + timedelta(days=6)
            day_height = 100
            hour_height = 40

            for day in range(7):
                current_day = start_of_week + timedelta(days=day)
                day_label = ttk.Label(self.inner_frame, text=current_day.strftime("%A %Y-%m-%d"), width=20)
                day_label.grid(row=day, column=0, sticky="w")

                for hour in range(24):
                    hour_label = ttk.Label(self.inner_frame, text=f"{hour:02d}:00", width=10)
                    hour_label.grid(row=day * 24 + hour, column=1, sticky="w")

                    task_frame = ttk.Frame(self.inner_frame)
                    task_frame.grid(row=day * 24 + hour, column=2, sticky="ew")

                    note_frame = ttk.Frame(self.inner_frame)
                    note_frame.grid(row=day * 24 + hour, column=3, sticky="ew")

                    for minute in range(0, 60, self.horaire.saut_de_temps.seconds // 60):
                        time_str = f"{current_day.strftime('%Y-%m-%d')} {hour:02d}:{minute:02d}:00"
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
                    edit_button.grid(row=day * 24 + hour, column=4, sticky="e")
