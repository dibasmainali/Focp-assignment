# Question 2: Letter Case Counter

def count_case_letters(text):
    """
    Count uppercase and lowercase letters in a string
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
