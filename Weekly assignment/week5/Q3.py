# Question 3: Find shortest argument

import sys

if len(sys.argv) < 2:
    print("Error: No arguments provided")
else:
    # Sort arguments by length, excluding program name (sys.argv[0])
    args_sorted = sorted(sys.argv[1:], key=len)
    print(f"Shortest argument: {args_sorted[0]}")
