# This program finds all factors of a positive integer.

def find_factors(num):
    if num <= 0:
        raise ValueError("Only positive integers are allowed.")
    return [i for i in range(1, num + 1) if num % i == 0]

# Test
print(find_factors(12))  # Output: [1, 2, 3, 4, 6, 12]
