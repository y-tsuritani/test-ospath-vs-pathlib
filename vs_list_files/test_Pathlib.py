from pathlib import Path

directory = Path("some_directory")
files = [f for f in directory.iterdir() if f.is_file()]

print(files)
