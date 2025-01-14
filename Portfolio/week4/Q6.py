# Question 6: Temperature Input Converter

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit
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
