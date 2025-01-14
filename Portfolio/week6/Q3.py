# This program checks if a number is a prime number.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Test
print(is_prime(11))  # Output: True
print(is_prime(12))  # Output: False
