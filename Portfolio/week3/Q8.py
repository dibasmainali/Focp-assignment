# Question 8: Times table that can go forwards or backwards

number = int(input("Enter a number (negative for backwards table): "))
abs_number = abs(number)

if number < 0:
    # Count backwards from 12 to 0
    for i in range(12, -1, -1):
        result = i * abs_number
        print(f"{i} x {abs_number} = {result}")
else:
    # Count forwards from 0 to 12
    for i in range(13):
        result = i * abs_number
        print(f"{i} x {number} = {result}")
