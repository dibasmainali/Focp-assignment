# This program returns a sorted list of all unique letters in a given string.

def unique_letters(text):
    return sorted(set(text.lower()))

# Test
print(unique_letters("cheese"))  # Output: ['c', 'e', 'h', 's']
