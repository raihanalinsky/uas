import os

def base_dir_import(name_file):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(BASE_DIR, "database", name_file)
     