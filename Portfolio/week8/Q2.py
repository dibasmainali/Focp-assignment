# 2. The Unix diff command compares two files and reports the dierences, if any.

import sys  # Importing the sys module
import difflib  # Importing the difflib module for showing differences
def diff_command(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            content1 = f1.readlines()
            content2 = f2.readlines()
            
            if content1 == content2:
                print("Files are the same.")
            else:
                print("Files are different.")
                # Show the differences
                print("\nDifferences:")
                diff = difflib.unified_diff(content1, content2, fromfile=file1, tofile=file2)
                for line in diff:
                    print(line, end='')  # Print differences without extra newline
    except FileNotFoundError as e:
        print(f"Error: The file '{e.filename}' was not found. Please check the file name and try again.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python diff_command.py <file1> <file2>")
    else:
        diff_command(sys.argv[1], sys.argv[2])
