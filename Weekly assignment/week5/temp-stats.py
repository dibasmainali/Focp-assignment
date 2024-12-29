# Question 5: Process temperature values from command line

import sys

if len(sys.argv) < 2:
    print("Error: No temperatures provided")
else:
    try:
        # Convert all arguments to floats, excluding program name
        temps = [float(arg) for arg in sys.argv[1:]]
        
        print(f"Maximum temperature: {max(temps)}")
        print(f"Minimum temperature: {min(temps)}")
        print(f"Mean temperature: {sum(temps) / len(temps):.1f}")
    except ValueError:
        print("Error: All arguments must be numbers")
