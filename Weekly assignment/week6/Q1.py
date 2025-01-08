# This program converts a positive integer to its binary (base 2) representation.

def to_binary(n):
    # Check if the number is positive
    if n <= 0:
        return "Input must be a positive integer."
    
    # Convert the number to binary using bin() function and remove the '0b' prefix
    return bin(n)[2:]

# Example usage
num = 7
print(f"The binary representation of {num} is {to_binary(num)}.")

