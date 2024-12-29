# Question 1: Range Validation Function
# This program validates if a given integer is in the range 0-100 inclusive
# Returns True if in range, False otherwise

def validate_range(number):
    """
    Check if a given number is in range 0-100 inclusive
    Args:
        number: Integer to check
    Returns:
        Boolean: True if in range, False otherwise
    """
    return 0 <= number <= 100

# Test program
def main():
    test_numbers = [-1, 0, 50, 100, 101]
    for num in test_numbers:
        print(f"Number {num} is{'' if validate_range(num) else ' not'} in range")

if __name__ == "__main__":
    main()
