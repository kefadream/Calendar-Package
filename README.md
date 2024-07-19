#![Main_interface](https://github.com/user-attachments/assets/8ce6a707-f517-49fd-8f02-ef0bc37c5902)
![horaire_ex1](https://github.com/user-attachments/assets/3323c9df-f685-4098-b986-7a4c3e1d7b58)
![HoraireGestionEx1](https://github.com/user-attachments/assets/f90f304f-8026-40f1-88af-7f3c081e62a9)


## Gestion d'Horaires

Ce projet est une application Tkinter pour la gestion des horaires. Il permet de créer, charger, sauvegarder et afficher les horaires sous différentes vues (quotidienne, hebdomadaire, mensuelle).

## Fonctionnalités

- Créer un nouvel horaire
- Charger un horaire existant
- Sauvegarder un horaire
- Afficher l'horaire en vue quotidienne, hebdomadaire et mensuelle
- Éditer les tâches et notes pour chaque horaire

## Utilisation (De John)
1. Ouvre ta console et tappe : 
```
cd chemin_vers_src_du_projet
```


2. Ensuite tappe :
```
python main.py
```

## Installation

1. Clonez le dépôt :

    ```bash
    git clone https://github.com/votre-utilisateur/votre-depot.git
    ```

2. Naviguez dans le répertoire du projet :

    ```bash
    cd votre-depot
    ```

3. Installez les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

## Utilisation

Pour lancer l'application, exécutez :

```bash
python -m src.interface.main_window
```

## `setup.py`

```python
from setuptools import setup, find_packages

setup(
    name='gestion_horaires',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'tkinter',  # Note: tkinter is part of the standard library and may not need to be installed separately
    ],
    entry_points={
        'console_scripts': [
            'gestion_horaires=src.interface.main_window:main',
        ],
    },
    author='Votre Nom',
    author_email='votre.email@example.com',
    description='Une application Tkinter pour la gestion des horaires',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/votre-utilisateur/votre-depot',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
```

## .gitignore

```gitignore
# Python
*.pyc
__pycache__/
*.pyo
*.pyd
.Python
env/
venv/
ENV/
env.bak/
venv.bak/

# Editor
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
```

## LICENSE

MIT License

Copyright (c) 2024 johndoe1711

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


## Structure du projet

```markdown
gestion_horaires/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── exceptions.py
│   ├── interface/
│   │   ├── __init__.py
│   │   ├── create_schedule_window.py
│   │   ├── event_editor.py
│   │   ├── load_window.py
│   │   ├── main_window.py
│   │   ├── views/ 
│   │   │   ├── __init__.py
│   │   │   ├── base_view.py
│   │   │   ├── daily_view_window.py
│   │   │   ├── weekly_view_window.py
│   │   │   ├── monthly_view_window.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── horaire.py
│   │   ├── horaire_creator.py
│   │   ├── horaire_editor.py
│   │   ├── event_editor.py
│   │   ├── sauts.py
│
├── README.md
├── setup.py
├── requirements.txt
├── .gitignore
├── LICENSE
```

## Instructions
Cloner le dépôt :

```bash
git clone https://github.com/votre-utilisateur/votre-depot.git
```

Naviguer dans le répertoire du projet :

```bash
cd votre-depot
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

Lancer l'application :

```bash
python main_window.py
```

Créer le package :

```bash
python setup.py sdist bdist_wheel
```

Installer le package localement pour tester :

```bash
pip install .
```
