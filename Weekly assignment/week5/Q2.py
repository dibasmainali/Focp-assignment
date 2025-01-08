# Question 2: Count command-line arguments

import sys

# sys.argv[0] is the program name, so we subtract 1
num_args = len(sys.argv) - 1
print(f"Number of arguments provided: {num_args}")
