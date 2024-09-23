from pathlib import Path

dir_path = Path("directory") / "to" / "new_directory"
dir_path.mkdir(parents=True, exist_ok=True)
