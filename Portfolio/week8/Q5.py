# 5. The Unix spell command is a simple spell-checker. It prints out all the words in a

import sys  # Importing the sys module

def spell_command(file_name, dictionary_file):
    try:
        with open(dictionary_file, 'r') as dict_file:
            dictionary = set(word.strip().lower() for word in dict_file)
        
        with open(file_name, 'r') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    # Improved word stripping using str.isalpha
                    stripped_word = ''.join(char for char in word if char.isalpha()).lower()
                    if stripped_word and stripped_word not in dictionary:
                        print(f"Misspelled word: {stripped_word}")  # Clearer output
    except FileNotFoundError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python spell_command.py <file_name> <dictionary_file>")
    else:
        spell_command(sys.argv[1], sys.argv[2])
