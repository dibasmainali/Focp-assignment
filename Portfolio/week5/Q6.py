# Question 6: Create backup copy of a file
import sys
import shutil
import os

def backup_file():
    # Check if a filename is provided as an argument
    if len(sys.argv) < 2:
        print("Usage: python backup_file.py <filename>")
        return
    
    # Get the original file name from the arguments
    original_file = sys.argv[1]
    
    # Check if the file exists
    if not os.path.isfile(original_file):
        print(f"Error: The file '{original_file}' does not exist.")
        return
    
    # Generate the backup file name
    base_name, ext = os.path.splitext(original_file)
    backup_file = f"{base_name}_backup{ext}"
    
    try:
        # Copy the file
        shutil.copy(original_file, backup_file)
        print(f"Backup created successfully: {backup_file}")
    except Exception as e:
        print(f"Error creating backup: {e}")

# Run the function
backup_file()
