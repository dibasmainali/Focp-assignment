# Question 6: Temperature Input Converter
# This program takes a temperature in the format "numberC"
# and converts it to Fahrenheit

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit
    Args:
        celsius: Temperature in Celsius
    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * 9/5) + 32

def convert_temperature():
    """
    Convert single temperature input in format "numberC" to Fahrenheit
    """
    while True:
        temp_input = input("Enter temperature (e.g., 23C) or press Enter to exit: ")
        if not temp_input:
            break
            
        if temp_input.endswith('C'):
            try:
                temp_c = float(temp_input[:-1])
                temp_f = celsius_to_fahrenheit(temp_c)
                print(f"{temp_f:.1f}F")
            except ValueError:
                print("Invalid temperature format")
        else:
            print("Temperature must end with 'C'")

if __name__ == "__main__":
    convert_temperature()
