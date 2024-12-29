# Question 7: Temperature Statistics Calculator
# This program reads exactly 6 temperatures in the format "numberC"
# and displays the maximum, minimum, and mean values

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit
    Args:
        celsius: Temperature in Celsius
    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * 9/5) + 32

def process_temperatures():
    """
    Process exactly 6 temperature inputs and calculate statistics
    """
    temperatures = []
    required_temps = 6
    
    print(f"Please enter {required_temps} temperatures in format 'numberC':")
    
    while len(temperatures) < required_temps:
        temp_input = input(f"Temperature {len(temperatures) + 1}: ")
        
        if temp_input.endswith('C'):
            try:
                temp_c = float(temp_input[:-1])
                temperatures.append(temp_c)
            except ValueError:
                print("Invalid temperature format. Please try again.")
        else:
            print("Temperature must end with 'C'. Please try again.")
    
    if temperatures:
        max_temp = max(temperatures)
        min_temp = min(temperatures)
        mean_temp = sum(temperatures) / len(temperatures)
        
        print(f"\nStatistics:")
        print(f"Maximum: {max_temp}C")
        print(f"Minimum: {min_temp}C")
        print(f"Mean: {mean_temp:.1f}C")

if __name__ == "__main__":
    process_temperatures()
