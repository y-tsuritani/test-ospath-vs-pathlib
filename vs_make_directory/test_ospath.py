import os

dir_path = os.path.join("directory", "to", "new_directory")
os.makedirs(dir_path, exist_ok=True)
