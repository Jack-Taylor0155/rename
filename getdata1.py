from pathlib import Path

# Define the target directory
file_path = Path(r"C:\rename")
file_name = Path(file_path).stem

# Loop through all items in the directory
for f_path in file_path.iterdir():
    # Ensure we are only renaming files (skipping folders)
    if file_path.is_file():
        # Example: Add a prefix "new_" to the existing filename
        # Split the string by the underscore delimiter
        print("This is the path name", file_name)
        elements = file_name.split("_")

# Unpack elements directly into descriptive variables
        memnum, Name, datet, lettern, index1 = elements

        print(f"Membernum: {memnum}, Name: {Name}, Date: {datet}, Letter Name: {lettern}, Index: {index1}")

        new_name = f"new_{file_path.name}"
        
        # Define the target destination path
        new_file_path = file_path.with_name(new_name)
        
        # Rename the file
        file_path.rename(new_file_path)