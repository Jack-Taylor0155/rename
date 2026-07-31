import os
import re

# Specifies the directory that the files needing to be renamed are located
target_directory = r"C:\rename"
                        
def sanitize_filenames(target_directory):
    # Ensure the directory path exists
    if not os.path.exists(target_directory):
        print(f"Error: The directory '{target_directory}' does not exist.")
        return

    # List all contents in the directory
    files = os.listdir(target_directory)
    
    renamed_count = 0

    for filename in files:
        old_filepath = os.path.join(target_directory, filename)
        
        # Skip if it is a directory (only processing files)
        if os.path.isdir(old_filepath):
            continue
            
        # Separate the name from the extension to avoid stripping the dot
        name_part, ext_part = os.path.splitext(filename)
        print(name_part)
        print(ext_part)
        
        elements = name_part.split("_")

# Unpack elements directly into descriptive variables
        memnum, Name, datet, lettern, index1 = elements

        print(f"Membernum: {memnum}, Name: {Name}, Date: {datet}, Letter Name: {lettern}, Index: {index1}")

        
       
        new_name_part = f"{Name}^{memnum}^0^{datet}^00000^{lettern}"
        # Recombine the sanitized name with its original extension
        new_filename = f"{new_name_part}{ext_part}"
        new_filepath = os.path.join(target_directory, new_filename)
        
        # If the name actually changed, proceed with renaming
        if filename != new_filename:
            # Handle potential file name collisions
            if os.path.exists(new_filepath):
                print(f"Skipped: '{filename}' -> '{new_filename}' already exists.")
                continue
                
            try:
                os.rename(old_filepath, new_filepath)
                print(f"Renamed: '{filename}' -> '{new_filename}'")
                renamed_count += 1
            except Exception as e:
                print(f"Failed to rename '{filename}': {e}")
                
    print(f"\nProcessing finished. Total files renamed: {renamed_count}")

# --- Configuration ---
# Replace this path with your target directory
# Use "r" before the string to handle Windows backslashes cleanly
TARGET_DIR = r"C:\rename" 

if __name__ == "__main__":
    sanitize_filenames(TARGET_DIR)
