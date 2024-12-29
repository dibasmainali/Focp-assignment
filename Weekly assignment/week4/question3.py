# Question 3: Name Formatter
# This program formats names to have the first letter uppercase
# and the rest lowercase, regardless of input format

def format_name(name):
    """
    Format name with first letter uppercase and rest lowercase
    Args:
        name: String containing the name
    Returns:
        String: Properly formatted name
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
