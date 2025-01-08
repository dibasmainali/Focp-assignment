# Question 5: Password checker that loops until successful

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    password1 = input("Enter new password: ")
    
    if len(password1) < 8 or len(password1) > 12:
        print("Error: Password must be between 8 and 12 characters")
        continue
        
    if password1.lower() in BAD_PASSWORDS:
        print("Error: Password is too common")
        continue
        
    password2 = input("Enter password again: ")
    
    if password1 == password2:
        print("Password Set")
        break
    else:
        print("Error: Passwords do not match")
