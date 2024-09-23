import os

file_path = os.path.join("../directory", "subdirectory", "file.txt")
file_exists = os.path.isfile(file_path)

parent_folder = os.path.dirname(file_path)  # ../directory/subdirectory
file_name = os.path.basename(file_path)  # file
extension = os.path.splitext(file_path)[-1]  # txt.

print(parent_folder)
print(file_name)
print(extension)
