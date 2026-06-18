import os

BASE_DIR = "database"

def get_csv_path(nama_file):
    os.makedirs(BASE_DIR, exist_ok=True)
    
    return os.path.join(
        BASE_DIR,
        nama_file
    )