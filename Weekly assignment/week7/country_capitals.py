# This program manages a list of countries and their capitals.

def country_capitals():
    capitals = {}
    while True:
        country = input("Enter the name of a country (or type 'exit' to quit): ").strip().lower()
        if country == "exit":
            break
        if country in capitals:
            print(f"The capital of {country.title()} is {capitals[country]}.")
        else:
            capital = input(f"Enter the capital of {country.title()}: ").strip().title()
            capitals[country] = capital
            print(f"Added {capital} as the capital of {country.title()}.")

# Run
country_capitals()
