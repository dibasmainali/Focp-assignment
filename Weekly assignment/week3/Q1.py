# Question 1: Simple greeting program with default "Stranger"

name = input("Please enter your name: ")
if not name:  # If user just presses enter
    print("Hello, Stranger!")
else:
    print(f"Hello, {name}!")
