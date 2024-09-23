import os

dir_path = os.path.join("directory", "to", "new_directory")
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
