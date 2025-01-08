# Question 4: Password checker with common password list

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

password1 = input("Enter new password: ")

if len(password1) < 8 or len(password1) > 12:
    print("Error: Password must be between 8 and 12 characters")
elif password1.lower() in BAD_PASSWORDS:
    print("Error: Password is too common")
else:
    password2 = input("Enter password again: ")
    if password1 == password2:
        print("Password Set")
    else:
        print("Error: Passwords do not match")
