from pathlib import Path

file_path = Path("../directory") / "subdirectory" / "file.txt"
file_exists = file_path.is_file()

parent_folder = file_path.parent  # ../directory/subdirectory
file_name = file_path.name  # file
extension = file_path.suffix  # txt.

print(parent_folder)
print(file_name)
print(extension)
