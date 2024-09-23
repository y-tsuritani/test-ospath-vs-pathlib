import os

file_path = os.path.join("directory", "file.txt")
with open(file_path) as file:
    content = file.read()

print(content)
