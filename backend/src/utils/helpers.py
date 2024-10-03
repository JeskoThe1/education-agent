import os
import json
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import config


def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_to_json(data, filename):
    ensure_directory_exists(config.PROCESSED_DATA_DIR)
    with open(os.path.join(config.PROCESSED_DATA_DIR, filename), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_from_json(filename):
    file_path = os.path.join(config.PROCESSED_DATA_DIR, filename)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def save_to_text(data, filename):
    ensure_directory_exists(config.PROCESSED_DATA_DIR)
    text_path = os.path.join(config.PROCESSED_DATA_DIR, filename)
    with open(text_path, 'w', encoding='utf-8') as f:
        if isinstance(data, dict):
            for key, value in data.items():
                f.write(f'{key}: {value}\n')
        elif isinstance(data, list):
            for item in data:
                f.write(f'- {item}\n')
        else:
            f.write(str(data))