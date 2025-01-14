# Question 3: Name Formatter
def format_name(name):
    """
    Format name with first letter uppercase and rest lowercase
    """
    return name.capitalize()

# Test program
def main():
    while True:
        name = input("Enter a name (or press Enter to exit): ")
        if not name:
            break
        formatted_name = format_name(name)
        print(f"Formatted name: {formatted_name}")

if __name__ == "__main__":
    main()
