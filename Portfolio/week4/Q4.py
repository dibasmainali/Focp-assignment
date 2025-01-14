# Question 4: Last Character Remover
def remove_last_char(text):
    """
    Remove the last character from a string if length > 1
    """
    return text[:-1] if len(text) > 1 else text

# Test program
def main():
    test_strings = ["Hello", "A", ""]
    for text in test_strings:
        result = remove_last_char(text)
        print(f"Original: '{text}' -> Modified: '{result}'")

if __name__ == "__main__":
    main()
