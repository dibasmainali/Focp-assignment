# This program finds the six most common letters in a string.

from collections import Counter

def most_common_letters(text):
    text = ''.join([char for char in text.lower() if char.isalpha()])
    letter_counts = Counter(text)
    return letter_counts.most_common(6)

# Test
print(most_common_letters("Eerie encryption experiment!"))  # Output: Top 6 letters with counts
