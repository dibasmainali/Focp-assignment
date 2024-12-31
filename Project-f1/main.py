import os
import json
import matplotlib.pyplot as plt
from tabulate import tabulate
from termcolor import colored

def load_driver_details(file_name="f1_drivers.json"):
    try:
        with open(file_name, 'r') as file:
            drivers = json.load(file)
        print(colored(f"Loaded driver details from '{file_name}' successfully.", "green"))
        return drivers
    except FileNotFoundError:
        print(colored(f"Error: '{file_name}' not found. Driver details will not be displayed.", "red"))
        return {}
    except json.JSONDecodeError:
        print(colored(f"Error: Failed to decode JSON in '{file_name}'.", "red"))
        return {}

def parse_lap_times(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        grand_prix_location = data.get("grand_prix_location", "Unknown Location")
        lap_times = data.get("lap_times", {})
        return grand_prix_location, lap_times
    except FileNotFoundError:
        print(colored(f"Error: File '{file_name}' not found.", "red"))
        return "Unknown Location", {}
    except json.JSONDecodeError:
        print(colored(f"Error: Failed to decode JSON in '{file_name}'.", "red"))
        return "Unknown Location", {}

def analyze_lap_times(lap_times):
    fastest_time_overall = float('inf')
    fastest_driver_overall = None
    driver_metrics = []

    for driver, times in lap_times.items():
        if not all(isinstance(time, (int, float)) for time in times):
            print(colored(f"Warning: Invalid lap time detected for driver {driver}. Skipping...\n", "yellow"))
            continue
        fastest_time = min(times)
        average_time = sum(times) / len(times)
        driver_metrics.append({"driver": driver, "fastest_time": fastest_time, "average_time": average_time})
        if fastest_time < fastest_time_overall:
            fastest_time_overall = fastest_time
            fastest_driver_overall = driver

    return fastest_driver_overall, fastest_time_overall, driver_metrics

def visualize_lap_times(grand_prix_location, driver_metrics, driver_details):
    drivers = [d["driver"] for d in driver_metrics]
    fastest_times = [d["fastest_time"] for d in driver_metrics]
    colors = plt.cm.viridis([time / max(fastest_times) for time in fastest_times])

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    bars = plt.bar(drivers, fastest_times, color=colors, edgecolor='black')
    plt.title(f"Fastest Lap Times - {grand_prix_location}", fontsize=16, color="darkblue")
    plt.xlabel("Driver Code", fontsize=14)
    plt.ylabel("Fastest Time (seconds)", fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    for bar in bars:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"{bar.get_height():.2f}", ha='center', va='bottom', fontsize=10, color="darkred")

    plt.subplot(1, 2, 2)
    plt.pie(fastest_times, labels=drivers, autopct="%1.1f%%", startangle=140, colors=plt.cm.tab20.colors, textprops={'fontsize': 12})
    plt.title("Lap Time Distribution", fontsize=16, color="darkblue")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
