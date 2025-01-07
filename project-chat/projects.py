import random
import json
import re
import time
from datetime import datetime

# Validate the JSON structure
def validate_responses(responses):
    """Validates the structure of the loaded responses."""
    if not isinstance(responses, list):
        print("Error: Responses must be a list.")
        return False
    for response in responses:
        if not all(key in response for key in ["tag", "patterns", "responses"]):
            print(f"Error: Missing keys in response entry: {response}")
            return False
    return True

# Load responses from a JSON file
def load_responses(file_path="responses.json"):
    """Loads chatbot responses from a JSON file and validates them."""
    try:
        with open(file_path, "r") as file:
            responses = json.load(file)
            if validate_responses(responses):
                return responses
    except FileNotFoundError:
        print("Error: responses.json file not found!")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in responses.json!")
    return []

# Normalize text for consistent matching
def normalize_text(text):
    """Normalizes text to lower case and trims spaces."""
    return text.strip().lower()

# Check if user input matches any patterns
def match_pattern(user_input, patterns):
    """Checks if the normalized user input matches any normalized patterns."""
    normalized_input = normalize_text(user_input)
    return any(re.search(pattern.strip(), normalized_input, re.IGNORECASE) for pattern in patterns)

# Generate a random agent name
def generate_agent_name():
    """Returns a randomly chosen agent name."""
    agent_names = ["Pratik", "Bibas", "Debaki", "Anushil", "Janak", "Bishesh", "Bibek", "Nabin"]
    return random.choice(agent_names)

# Save chat log to a file
def log_session(user_name, logs):
    """Saves the chat log to a file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file_name = f"chat_log_{user_name.replace(' ', '_')}_{timestamp}.txt"
    with open(log_file_name, "w") as log_file:
        log_file.write(f"Chat session with {user_name} ({timestamp}):\n")
        log_file.write("\n".join(logs))
    print(f"Chat log saved to {log_file_name}")

# Log responses with tags for debugging
def log_response(user_input, tag, response):
    """Logs user input and chatbot responses with tags."""
    return f"User Input: {user_input} | Matched Tag: {tag} | Response: {response}"

# Simulate typing effect
def simulate_typing(response):
    """Simulates typing with speed based on response length."""
    speed = max(0.02, 0.5 / len(response))  # Adjust speed dynamically
    for char in response:
        print(char, end="", flush=True)
        time.sleep(speed)
    print()

# Generate a time-based greeting
def time_based_greeting():
    """Returns a greeting based on the current time."""
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning"
    elif hour < 18:
        return "Good afternoon"
    return "Good evening"

# Fetch response for user input
def get_response(user_input, responses):
    """Fetches a response based on user input."""
    for item in responses:
        if match_pattern(user_input, item.get("patterns", [])):
            return random.choice(item.get("responses", [])), item["tag"]
    # Fallback response
    fallback_responses = next((item["responses"] for item in responses if item["tag"] == "fallback"), [])
    return random.choice(fallback_responses) if fallback_responses else "I'm not sure I can help with that.", "fallback"

# Display help command
def display_help(responses):
    print("Here are the topics I can help with:\n")
    for item in responses:
        print(f" - {item['tag'].capitalize()}: {', '.join(item['patterns'])}")

# Start the chatbot session
def start_chat():
    """Main chatbot function that handles user interaction."""
    responses = load_responses()
    if not responses:
        print("No responses loaded. Exiting.")
        return

    user_name = input("Welcome to IntelliChat! Please enter your name: ").strip()
    print(f"{time_based_greeting()}, {user_name}! Welcome to IntelliChat.")
    agent_name = generate_agent_name()
    simulate_typing(f"My name is {agent_name}, and I'm here to help you.")

    chat_log = []

    while True:
        user_input = input(f"{user_name}: ").strip()
        chat_log.append(f"User: {user_input}")

        # Exit conditions
        if user_input.lower() in ["bye", "quit", "exit"]:
            farewell_message = f"It was nice chatting with you, {user_name}. Goodbye!"
            simulate_typing(f"{agent_name}: {farewell_message}")
            chat_log.append(f"Agent: {farewell_message}")
            break

        # Help command
        if user_input.lower() == "help":
            display_help(responses)
            continue

        # Match user input with responses
        response, tag = get_response(user_input, responses)
        simulate_typing(f"{agent_name}: {response}")
        chat_log.append(log_response(user_input, tag, response))

    # Save chat log
    log_session(user_name, chat_log)

# Entry point
if __name__ == "__main__":
    start_chat()
