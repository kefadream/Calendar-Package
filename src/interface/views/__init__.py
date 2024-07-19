"""
Module __init__
===============

Ce module initialise le package `calendar_view` et importe les classes de vue de calendrier :
- BaseCalendarView
- DailyView
- WeeklyView
- MonthlyView

Ces classes permettent d'afficher et d'interagir avec les données de calendrier sur des périodes
quotidiennes, hebdomadaires et mensuelles.

Example:
    from calendar_view import DailyView, WeeklyView, MonthlyView

"""

from .base_view import BaseCalendarView
from .daily_view_window import DailyViewWindow
from .weekly_view_window import WeeklyViewWindow
from .monthly_view_window import MonthlyViewWindow
