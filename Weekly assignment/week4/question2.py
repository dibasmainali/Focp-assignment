# Question 2: Letter Case Counter
# This program counts uppercase and lowercase letters in a given string
# Returns a tuple of (uppercase_count, lowercase_count)

def count_case_letters(text):
    """
    Count uppercase and lowercase letters in a string
    Args:
        text: String to analyze
    Returns:
        Tuple: (uppercase_count, lowercase_count)
    """
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    return upper_count, lower_count

# Test program
def main():
    test_string = "Hello World! 123"
    upper, lower = count_case_letters(test_string)
    print(f"String: {test_string}")
    print(f"Uppercase letters: {upper}")
    print(f"Lowercase letters: {lower}")

if __name__ == "__main__":
    main()
