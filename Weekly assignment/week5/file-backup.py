# Question 6: Create backup copy of a file

import sys
import shutil

if len(sys.argv) < 2:
    print("Error: Please provide a filename")
else:
    try:
        original = sys.argv[1]
        backup = original + '.backup'
        shutil.copy2(original, backup)
        print(f"Backup created: {backup}")
    except FileNotFoundError:
        print(f"Error: File '{original}' not found")
    except PermissionError:
        print("Error: Permission denied")
