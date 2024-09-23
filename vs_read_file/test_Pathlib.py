from pathlib import Path

file_path = Path("directory") / "file.txt"
content = file_path.read_text()

print(content)
