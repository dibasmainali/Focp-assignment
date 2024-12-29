Formula 1 Lap Times Analysis
This Python project analyzes lap times from Formula 1 Grand Prix practice sessions. The program processes multiple JSON files containing lap times, identifies the fastest drivers, and saves detailed analysis logs for each race.

Features
Process Multiple Files: Analyzes lap times from multiple JSON files (lap_times_1.json, lap_times_2.json, lap_times_3.json).
Driver Details: Incorporates driver information (names and teams) from f1_drivers.json.
Detailed Analysis:
Fastest driver and lap time overall.
Fastest and average lap times for each driver.
Formatted Output: Displays results in a neat table format using the tabulate library.
Log Files: Saves analysis results to separate JSON logs for each race.
Requirements
Python 3.7 or later
Installed Python modules:
json
tabulate (install with pip install tabulate)
Files
Input Files
f1_drivers.json: Contains driver details, including their codes, names, and teams. Example:

json
Copy code
{
    "HAM": {"name": "Lewis Hamilton", "team": "Mercedes"},
    "VER": {"name": "Max Verstappen", "team": "Red Bull Racing"},
    "NOR": {"name": "Lando Norris", "team": "McLaren"}
}
Lap Times Files: JSON files containing lap times for multiple Grand Prix events:

lap_times_1.json
lap_times_2.json
lap_times_3.json
Each file should follow this format:

json
Copy code
{
    "grand_prix_location": "Monaco",
    "lap_times": {
        "HAM": [98.123, 100.456, 101.789],
        "VER": [99.456, 102.345, 100.678],
        "NOR": [100.123, 101.456, 102.789]
    }
}
Output Files
lap_times_1_log.json, lap_times_2_log.json, lap_times_3_log.json: Detailed analysis logs saved in JSON format.
Usage
1. Clone the Repository
Download or clone the repository to your local machine.

bash
Copy code
git clone https://github.com/your-repo/f1-lap-times.git
cd f1-lap-times
2. Install Dependencies
Install the required Python modules using pip:

bash
Copy code
pip install tabulate
3. Run the Program
Run the program from the command line:

bash
Copy code
python main.py
The program will:

Process each file (lap_times_1.json, lap_times_2.json, lap_times_3.json).
Display results in the console.
Save logs to JSON files (e.g., lap_times_1_log.json).
Example Output
Console Output:
plaintext
Copy code
Processing file: lap_times_1.json

Grand Prix Location: Monaco Grand Prix

Fastest Driver Overall: HAM with a time of 98.123 seconds

+------+-------------------+------------------+---------------+---------------+
| Code | Name              | Team             | Fastest Time  | Average Time  |
+------+-------------------+------------------+---------------+---------------+
| HAM  | Lewis Hamilton    | Mercedes         | 98.123        | 100.456       |
| VER  | Max Verstappen    | Red Bull Racing  | 99.456        | 101.789       |
| NOR  | Lando Norris      | McLaren          | 100.123       | 102.345       |
+------+-------------------+------------------+---------------+---------------+

Results have been saved to 'lap_times_1_log.json'.
Log File (lap_times_1_log.json):
json
Copy code
{
    "grand_prix_location": "Monaco",
    "fastest_driver": "HAM",
    "fastest_time": 98.123,
    "driver_details": [
        {
            "code": "HAM",
            "name": "Lewis Hamilton",
            "team": "Mercedes",
            "fastest_time": 98.123,
            "average_time": 100.456
        },
        {
            "code": "VER",
            "name": "Max Verstappen",
            "team": "Red Bull Racing",
            "fastest_time": 99.456,
            "average_time": 101.789
        },
        {
            "code": "NOR",
            "name": "Lando Norris",
            "team": "McLaren",
            "fastest_time": 100.123,
            "average_time": 102.345
        }
    ]
}
Troubleshooting
Missing Files: Ensure f1_drivers.json and all lap_times_X.json files are in the same directory as main.py.

Missing Dependencies: Install missing dependencies using:

bash
Copy code
pip install tabulate
File Format Errors: Verify the JSON files are properly formatted.

Author
Dibas Mainali
dibasmainali012@gmail.com