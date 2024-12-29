# Question 8: Temperature Statistics Calculator (Variable Input)
# This program reads any number of temperatures until Enter is pressed
# and displays the maximum, minimum, and mean values

def process_temperatures():
    """
    Process multiple temperature inputs and calculate statistics
    Input terminates when user presses Enter without value
    """
    temperatures = []
    
    print("Enter temperatures in format 'numberC' (press Enter to finish):")
    
    while True:
        temp_input = input(f"Temperature {len(temperatures) + 1}: ")
        if temp_input == "":
            break
            
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
        
        print(f"\nProcessed {len(temperatures)} temperatures")
        print(f"Maximum: {max_temp}C")
        print(f"Minimum: {min_temp}C")
        print(f"Mean: {mean_temp:.1f}C")
    else:
        print("No valid temperatures entered")

if __name__ == "__main__":
    process_temperatures()
