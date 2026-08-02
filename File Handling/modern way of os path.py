from pathlib import Path

file_path = Path("abc.txt")

print(file_path.exists())

print(file_path.is_file())

print(file_path.is_dir())

print(file_path.stat().st_size)
