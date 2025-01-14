# 3. The Unix grep command searches a file and outputs the lines in the file that
import sys  # Importing the sys module
def grep_command(pattern, file_name):
    try:
        with open(file_name, 'r') as file:
            found = False  # Flag to check if any line is found
            for line in file:
                if pattern in line:
                    print(line.strip())
                    found = True  # Set flag to True if a match is found
            if not found:
                print(f"No lines found containing the pattern '{pattern}'.")  # Inform if no matches found
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found. Please check the file name and try again.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python grep_command.py <pattern> <file_name>")
    else:
        grep_command(sys.argv[1], sys.argv[2])
