from pathlib import Path
import os
# Path to your target directory
dir_path = Path(r"C:\rename")
file_names = [file.name for file in dir_path.iterdir() if file.is_file()]
#print(file_names)


file_count = sum(1 for item in Path(dir_path).iterdir() if item.is_file())
print(file_count)
old_filepath = os.path.join(dir_path, file_names)
print(old_filepath)
#elements = file_names.split("_")

#print(elements)
