import tkinter as tk
from tkinter import ttk
from datetime import timedelta
from .base_view import BaseCalendarView


class MonthlyViewWindow(BaseCalendarView):
    def __init__(self, parent, save_callback):
        super().__init__(parent, save_callback, "monthly")

    def update_calendar(self):
        self.date_label.config(text=self.selected_date.strftime("%B %Y"))
        for widget in self.inner_frame.winfo_children():
            widget.destroy()
        self.draw_calendar()

    def show_prev_period(self):
        self.selected_date = self.selected_date.replace(day=1) - timedelta(days=1)
        self.update_calendar()

    def show_next_period(self):
        days_in_month = (self.selected_date.replace(month=self.selected_date.month % 12 + 1, day=1) - timedelta(days=1)).day
        self.selected_date += timedelta(days=days_in_month)
        self.update_calendar()

    def draw_calendar(self):
        if self.horaire:
            start_of_month = self.selected_date.replace(day=1)
            end_of_month = self.selected_date.replace(month=self.selected_date.month % 12 + 1, day=1) - timedelta(days=1)
            day_height = 100

            current_day = start_of_month
            day = 0
            while current_day <= end_of_month:
                day_label = ttk.Label(self.inner_frame, text=current_day.strftime("%A %Y-%m-%d"), width=20)
                day_label.grid(row=day, column=0, sticky="w")

                task_frame = ttk.Frame(self.inner_frame)
                task_frame.grid(row=day, column=1, sticky="ew")

                note_frame = ttk.Frame(self.inner_frame)
                note_frame.grid(row=day, column=2, sticky="ew")

                for hour in range(24):
                    for minute in range(0, 60, self.horaire.saut_de_temps.seconds // 60):
                        time_str = f"{current_day.strftime('%Y-%m-%d')} {hour:02d}:{minute:02d}:00"
                        if time_str in self.horaire.horaire:
                            task_text = self.horaire.horaire[time_str].get('tache', '')
                            note_text = self.horaire.horaire[time_str].get('note', '')

                            if task_text:
                                task_label = ttk.Label(task_frame, text=f"{hour:02d}:{minute:02d} - {task_text}", background="lightblue", width=30, anchor="w")
                                task_label.pack(fill=tk.X, padx=5, pady=2)

                            if note_text:
                                note_label = ttk.Label(note_frame, text=f"{hour:02d}:{minute:02d} - {note_text}", background="lightgreen", width=30, anchor="w")
                                note_label.pack(fill=tk.X, padx=5, pady=2)

                edit_button = ttk.Button(self.inner_frame, text="Edit", command=lambda ts=time_str: self.edit_event(ts))
                edit_button.grid(row=day, column=3, sticky="e")

                current_day += timedelta(days=1)
                day += 1
