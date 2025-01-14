# # This program manages a list of countries and their capitals.

# def country_capitals():
#     capitals = {}
#     while True:
#         country = input("Enter the name of a country (or type 'exit' to quit): ").strip().lower()
#         if country == "exit":
#             break
#         if country in capitals:
#             print(f"The capital of {country.title()} is {capitals[country]}.")
#         else:
#             capital = input(f"Enter the capital of {country.title()}: ").strip().title()
#             capitals[country] = capital
#             print(f"Added {capital} as the capital of {country.title()}.")

# # Run
# country_capitals()

import os

def load_data(filename):
    """Load country-capital data from a file into a dictionary."""
    capitals = {}
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                country, capital = line.strip().split(":")
                capitals[country.lower()] = capital
    return capitals

def save_data(filename, capitals):
    """Save country-capital data from a dictionary into a file."""
    with open(filename, "w") as file:
        for country, capital in capitals.items():
            file.write(f"{country}:{capital}\n")

def country_capitals():
    filename = "Q3.txt"
    capitals = load_data(filename)
    
    while True:
        country = input("Enter the name of a country (or type 'exit' to quit): ").strip().lower()
        if country == "exit":
            save_data(filename, capitals)
            print("Data saved. Goodbye!")
            break
        if country in capitals:
            print(f"The capital of {country.title()} is {capitals[country]}.")
        else:
            capital = input(f"Enter the capital of {country.title()}: ").strip().title()
            capitals[country] = capital
            print(f"Added {capital} as the capital of {country.title()}.")

# Run
country_capitals()
