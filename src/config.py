import json
import os

CONFIG_FILE = 'config.json'

def load_config():
    """Charger la configuration depuis le fichier JSON."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r', encoding='utf-8') as config_file:
            return json.load(config_file)
    else:
        return {}

def save_config(config):
    """Sauvegarder la configuration dans le fichier JSON."""
    with open(CONFIG_FILE, 'w', encoding='utf-8') as config_file:
        json.dump(config, config_file, indent=4, ensure_ascii=False)
