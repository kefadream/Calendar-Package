"""
File: main.py

Point d'entrée principal de l'application Tkinter pour la gestion des horaires.
"""
from interface.main_window import MainWindow


def main():
    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    main()
