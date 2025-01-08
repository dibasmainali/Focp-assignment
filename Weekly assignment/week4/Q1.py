# Question 1: Range Validation Function

def validate_range(number):
    """
    Check if a given number is in range 0-100 inclusive
    """
    return 0 <= number <= 100

# Test program
def main():
    test_numbers = [-1, 0, 50, 100, 101]
    for num in test_numbers:
        print(f"Number {num} is{'' if validate_range(num) else ' not'} in range")

if __name__ == "__main__":
    main()
