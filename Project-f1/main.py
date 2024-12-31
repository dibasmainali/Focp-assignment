import json
import matplotlib.pyplot as plt
from tabulate import tabulate
from termcolor import colored

def load_driver_details(file_name="f1_drivers.json"):
    """Load driver details from a JSON file."""
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
    """Parse lap times from a JSON file."""
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
    """Analyze lap times to find fastest times and calculate metrics."""
    fastest_time_overall = float('inf')
    fastest_driver_overall = None
    driver_metrics = []

    for driver, times in lap_times.items():
        fastest_time = min(times)
        average_time = sum(times) / len(times)

        driver_metrics.append({
            "driver": driver,
            "fastest_time": fastest_time,
            "average_time": average_time
        })

        if fastest_time < fastest_time_overall:
            fastest_time_overall = fastest_time
            fastest_driver_overall = driver

    return fastest_driver_overall, fastest_time_overall, driver_metrics

def save_to_json_log(grand_prix_location, fastest_driver, fastest_time, driver_metrics, driver_details, log_file):
    """Save analysis results to a JSON log file."""
    log_data = {
        "grand_prix_location": grand_prix_location,
        "fastest_driver": fastest_driver,
        "fastest_time": fastest_time,
        "driver_details": []
    }

    for d in driver_metrics:
        details = driver_details.get(d["driver"], {"name": "Unknown", "team": "Unknown"})
        log_data["driver_details"].append({
            "code": d["driver"],
            "name": details["name"],
            "team": details["team"],
            "fastest_time": d["fastest_time"],
            "average_time": d["average_time"]
        })

    with open(log_file, "w") as file:
        json.dump(log_data, file, indent=4)

    print(colored(f"Results have been saved to '{log_file}'.", "green"))

def display_results(grand_prix_location, fastest_driver, fastest_time, driver_metrics, driver_details):
    """Display results in a formatted table."""
    print(colored(f"\nGrand Prix Location: {grand_prix_location}\n", "cyan", attrs=["bold"]))
    print(colored(f"Fastest Driver Overall: {fastest_driver} with a time of {fastest_time:.3f} seconds\n", "yellow", attrs=["bold"]))

    driver_metrics_sorted = sorted(driver_metrics, key=lambda x: x["fastest_time"])
    table = []

    for d in driver_metrics_sorted:
        details = driver_details.get(d["driver"], {"name": "Unknown", "team": "Unknown"})
        table.append([
            d["driver"],
            details["name"],
            details["team"],
            f"{d['fastest_time']:.3f}",
            f"{d['average_time']:.3f}"
        ])

    print(tabulate(table, headers=["Code", "Name", "Team", "Fastest Time", "Average Time"], tablefmt="fancy_grid"))

def visualize_lap_times(grand_prix_location, driver_metrics, driver_details):
    """Visualize lap times using Matplotlib."""
    drivers = []
    fastest_times = []

    for d in driver_metrics:
        drivers.append(d["driver"])
        fastest_times.append(d["fastest_time"])

    # Bar Chart
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    bars = plt.bar(drivers, fastest_times, color='skyblue', edgecolor='black')
    plt.title(f"Fastest Lap Times - {grand_prix_location}", fontsize=16, color="darkblue")
    plt.xlabel("Driver Code", fontsize=14)
    plt.ylabel("Fastest Time (seconds)", fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    for bar in bars:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"{bar.get_height():.2f}", ha='center', va='bottom', fontsize=10, color="darkred")

    # Pie Chart
    plt.subplot(1, 2, 2)
    plt.pie(fastest_times, labels=drivers, autopct="%1.1f%%", startangle=140, colors=plt.cm.tab20.colors)
    plt.title("Lap Time Distribution", fontsize=16, color="darkblue")

    plt.tight_layout()
    plt.show()

def main():
    """Main function to process lap time data."""
    lap_times_files = ["lap_times_1.json", "lap_times_2.json", "lap_times_3.json"]

    driver_details = load_driver_details()  # Load driver details from f1_drivers.json

    for lap_times_file in lap_times_files:
        print(colored(f"\nProcessing file: {lap_times_file}\n", "blue", attrs=["bold"]))

        # Parse lap times from JSON
        grand_prix_location, lap_times = parse_lap_times(lap_times_file)

        if not lap_times:
            print(colored(f"No data found in {lap_times_file}. Skipping...\n", "red"))
            continue

        # Analyze lap times
        fastest_driver, fastest_time, driver_metrics = analyze_lap_times(lap_times)

        # Display results on console
        display_results(grand_prix_location, fastest_driver, fastest_time, driver_metrics, driver_details)

        # Save results to a JSON log
        log_file_name = f"{lap_times_file.split('.')[0]}_log.json"
        save_to_json_log(grand_prix_location, fastest_driver, fastest_time, driver_metrics, driver_details, log_file_name)

        # Visualize results
        visualize_lap_times(grand_prix_location, driver_metrics, driver_details)

if __name__ == "__main__":
    main()
