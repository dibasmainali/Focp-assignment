# Question 4: Check if website exists at URL

import sys
import requests

if len(sys.argv) < 2:
    print("Error: Please provide a URL")
else:
    url = sys.argv[1]
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Website exists at {url}")
        else:
            print(f"No working website at {url}")
    except requests.RequestException:
        print(f"Error: Could not connect to {url}")
