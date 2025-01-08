# Question 7: Custom times table (0-12)

number = int(input("Enter a number (0-12): "))

if 0 <= number <= 12:
    for i in range(13):
        result = i * number
        print(f"{i} x {number} = {result}")
else:
    print("Number must be between 0 and 12")
