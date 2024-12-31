# F1 Lap Time Analysis

## Overview
This Python project analyzes Formula 1 lap times from JSON data files, calculates driver performance metrics, and presents the results in a user-friendly format. It includes a variety of features like tabled results, bar charts, and pie charts to visualize data effectively.

## Features
- Parse lap time data from multiple JSON files.
- Analyze lap times to determine the fastest driver and average lap times.
- Save results to a JSON log file for further reference.
- Display data in a tabulated format with enhanced console output using `termcolor` and `tabulate` libraries.
- Visualize data with:
  - Bar chart of the fastest lap times.
  - Pie chart for lap time distribution.

## Requirements
- Python 3.7 or higher
- Libraries:
  - `json`
  - `matplotlib`
  - `tabulate`
  - `termcolor`

## Installation
1. Clone this repository or download the project files.
2. Install the required Python libraries using pip:
   ```bash
   pip install matplotlib tabulate termcolor
   ```
3. Ensure that JSON files (`f1_drivers.json`, `lap_times_1.json`, etc.) are present in the project directory.

## Usage
1. Run the script using the following command:
   ```bash
   python <script_name>.py
   ```
2. The program will automatically process all JSON files defined in the `lap_times_files` list and display results on the console.
3. Results include:
   - Formatted table of driver performances.
   - Bar and pie charts to visualize lap time data.
   - A JSON log file summarizing the results.

## File Structure
- `f1_drivers.json`: Contains driver details (code, name, team).
- `lap_times_x.json`: Contains lap time data for a specific Grand Prix.
- `log_file_name.json`: Output logs containing analyzed data.
- `script_name.py`: Main Python script.

## Output
- **Console:**
  - Tabulated results showing driver performance metrics.
  - Summary of the fastest driver and their lap time.
- **Charts:**
  - Bar chart showing the fastest lap times for each driver.
  - Pie chart representing the lap time distribution among drivers.
- **Logs:**
  - JSON file storing the results of the analysis.

## Example JSON Files
### `f1_drivers.json`
```json
{
  "HAM": {"name": "Lewis Hamilton", "team": "Mercedes"},
  "VER": {"name": "Max Verstappen", "team": "Red Bull"},
  "LEC": {"name": "Charles Leclerc", "team": "Ferrari"}
}
```

### `lap_times_1.json`
```json
{
  "grand_prix_location": "Monaco",
  "lap_times": {
    "HAM": [74.5, 73.8, 75.1],
    "VER": [72.9, 73.3, 72.7],
    "LEC": [73.2, 74.0, 73.7]
  }
}
```

## How It Works
1. **Data Loading:**
   - Driver details are loaded from `f1_drivers.json`.
   - Lap time data is parsed from JSON files like `lap_times_x.json`.
2. **Analysis:**
   - The fastest driver and their lap time are calculated.
   - Average lap times are computed for each driver.
3. **Visualization:**
   - Results are visualized using bar and pie charts.
4. **Logging:**
   - Analysis results are saved in a structured JSON log file.

## Customization
- Update `lap_times_files` in the script to include additional JSON files.
- Modify the visualization style by changing `matplotlib` configurations.

## Notes
- Ensure all JSON files are correctly formatted.
- If a file is missing or has invalid JSON, appropriate error messages will be displayed.

## License
This project is licensed under the MIT License. Feel free to use and modify it for your needs.

