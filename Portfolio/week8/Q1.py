# 1. The Unix nl command prints the lines of a text file with a line number at the start
import sys  # Importing the sys module
def nl_command(file_name):
    try:
        with open(file_name, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                print(f"{line_number:4}: {line.strip()}")  # Print line number and content
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found. Please check the file name and try again.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python nl_command.py <file_name>")
    else:
        nl_command(sys.argv[1])
