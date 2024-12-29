# Question 5: Temperature Conversion Functions
# This program provides functions to convert between Celsius and Fahrenheit

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit
    Args:
        celsius: Temperature in Celsius
    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius
    Args:
        fahrenheit: Temperature in Fahrenheit
    Returns:
        float: Temperature in Celsius
    """
    return (fahrenheit - 32) * 5/9

# Test program
def main():
    test_temps_celsius = [0, 25, 100]
    print("Testing temperature conversions:")
    
    for temp_c in test_temps_celsius:
        temp_f = celsius_to_fahrenheit(temp_c)
        print(f"{temp_c}°C = {temp_f:.1f}°F")
        # Convert back to verify accuracy
        converted_back = fahrenheit_to_celsius(temp_f)
        print(f"{temp_f:.1f}°F = {converted_back:.1f}°C")
        print()

if __name__ == "__main__":
    main()
