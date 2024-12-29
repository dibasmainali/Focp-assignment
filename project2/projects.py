import random
import json
import re
import time
from datetime import datetime
import os

# Load responses from a JSON file
def load_responses(file_path="responses.json"):
    """Loads chatbot responses from a JSON file."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: responses.json file not found!")
        return []

# Generate a random agent name
def generate_agent_name():
    """Returns a randomly chosen agent name."""
    return random.choice(["Alex", "Jordan", "Taylor", "Morgan", "Blake", "Casey", "Riley", "Dakota", "Avery", "Skyler"])

# Save chat log to a file
def log_session(user_name, logs):
    """Saves the chat log to a file."""
    log_file_name = f"chat_log_{user_name.replace(' ', '_')}.txt"
    with open(log_file_name, "w") as log_file:
        log_file.write(f"Chat session with {user_name}:\n")
        log_file.write("\n".join(logs))
    print(f"Chat log saved to {log_file_name}")

# Check if user input matches any patterns
def match_pattern(user_input, patterns):
    """Checks if the user input matches any of the given patterns."""
    return any(re.search(rf"\b{pattern}\b", user_input, re.IGNORECASE) for pattern in patterns)

# Simulate typing effect
def simulate_typing(response):
    """Simulates typing by printing characters with a delay."""
    for char in response:
        print(char, end="", flush=True)
        time.sleep(0.03)  # Typing speed
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

# Start the chatbot session
def start_chat():
    """Main chatbot function that handles user interaction."""
    responses = load_responses()
    if not responses:
        print("No responses loaded. Exiting.")
        return

    user_name = input("Welcome to Poppleton University Chat! Please enter your name: ").strip()
    print(f"{time_based_greeting()}, {user_name}! Welcome to Poppleton University Chat.")
    agent_name = generate_agent_name()
    simulate_typing(f"My name is {agent_name}, and I'm here to help you.")

    chat_log = []
    context = None  # Stores the context of the conversation

    while True:
        user_input = input(f"{user_name}: ").strip().lower()
        chat_log.append(f"User: {user_input}")

        # Exit conditions
        if user_input in ["bye", "quit", "exit"]:
            farewell_message = f"It was nice chatting with you, {user_name}. Goodbye!"
            simulate_typing(f"{agent_name}: {farewell_message}")
            chat_log.append(f"Agent: {farewell_message}")
            break

        # Special command to show chat history
        if user_input == "show chat history":
            simulate_typing("Here’s what we’ve discussed so far:")
            for entry in chat_log:
                simulate_typing(entry)
            continue

        # Update context based on user input
        if match_pattern(user_input, ["courses", "classes"]):
            context = "courses"
        elif match_pattern(user_input, ["fees", "tuition"]):
            context = "fees"

        # Context-aware responses
        response = None
        if context == "courses" and match_pattern(user_input, ["details", "subjects"]):
            response = "We offer detailed syllabi for all courses on our website."
        elif context == "fees" and match_pattern(user_input, ["cost", "price"]):
            response = "Our tuition fees vary by program. Please visit our fees page for detailed information."

        # Find a matching response if no specific context response
        if not response:
            for item in responses:
                if match_pattern(user_input, item["patterns"]):
                    response = random.choice(item["responses"])
                    break

        # Default response if no match
        if not response:
            response = random.choice([
                "I'm not sure about that. Can you clarify?",
                "That's interesting. Let me think about it!",
                "Can you provide more details about your question?",
                "I'm here to help, but I might need more information."
            ])

        # Include user's name in 50% of responses
        if random.random() < 0.5:
            response = f"{user_name}, {response}"

        simulate_typing(f"{agent_name}: {response}")
        chat_log.append(f"Agent: {response}")

    # Save chat log
    log_session(user_name, chat_log)

# Entry point
if __name__ == "__main__":
    start_chat()
