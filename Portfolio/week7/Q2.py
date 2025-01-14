# This program defines functions to compare letters in two words.

# Letters that appear in at least one of the two words
def letters_in_either(word1, word2):
    return sorted(set(word1.lower()) | set(word2.lower()))

# Letters that appear in both words
def letters_in_both(word1, word2):
    return sorted(set(word1.lower()) & set(word2.lower()))

# Letters that appear in either word, but not in both
def letters_in_either_but_not_both(word1, word2):
    return sorted(set(word1.lower()) ^ set(word2.lower()))

# Test
print(letters_in_either("cheese", "bread"))       # Output: Sorted unique letters in both words
print(letters_in_both("cheese", "bread"))        # Output: Sorted common letters
print(letters_in_either_but_not_both("cheese", "bread"))  # Output: Unique letters not shared
