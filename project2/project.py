import random
import json
import re
import time
from datetime import datetime
import os
from colorama import init, Fore, Style
import platform
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
import questionary

# Initialize colorama for cross-platform color support
init()
console = Console()

def time_based_greeting():
    """Returns a greeting based on the current time."""
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning"
    elif hour < 18:
        return "Good afternoon"
    return "Good evening"

def clear_screen():
    """Clear the console screen based on the operating system."""
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def load_responses(file_path="responses.json"):
    """Loads chatbot responses from a JSON file with error handling."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        console.print(Panel("[red]Error: responses.json file not found!", title="Error"))
        return []
    except json.JSONDecodeError:
        console.print(Panel("[red]Error: Invalid JSON format in responses file!", title="Error"))
        return []

def generate_agent_name():
    """Returns a randomly chosen agent name with personality traits."""
    agents = {
        "Alex": "friendly and enthusiastic",
        "Jordan": "professional and thorough",
        "Taylor": "patient and understanding",
        "Morgan": "energetic and helpful",
        "Blake": "knowledgeable and precise"
    }
    name = random.choice(list(agents.keys()))
    return name, agents[name]

def log_session(user_name, logs):
    """Saves the chat log to a file with timestamp and formatting."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file_name = f"chat_logs/chat_log_{user_name.replace(' ', '_')}_{timestamp}.txt"
    
    # Create logs directory if it doesn't exist
    os.makedirs("chat_logs", exist_ok=True)
    
    with open(log_file_name, "w") as log_file:
        log_file.write(f"Chat Session Summary\n")
        log_file.write(f"User: {user_name}\n")
        log_file.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        log_file.write("=" * 50 + "\n\n")
        log_file.write("\n".join(logs))
    
    console.print(f"[green]Chat log saved to {log_file_name}")

def match_pattern(user_input, patterns):
    """Checks if the user input matches any of the given patterns."""
    return any(re.search(rf"\b{pattern}\b", user_input, re.IGNORECASE) for pattern in patterns)

def simulate_typing(response, speed=0.03):
    """Simulates typing with color and style."""
    for char in response:
        console.print(char, end="", style="bold blue")
        time.sleep(speed)
    print()

def display_welcome_banner():
    """Displays an attractive welcome banner."""
    welcome_text = """
    ╔══════════════════════════════════════╗
    ║    Welcome to The British college    ║
    ║         Interactive Chat Bot         ║
    ╚══════════════════════════════════════╝
    """
    console.print(Panel(welcome_text, style="bold blue"))

def show_help_menu():
    """Displays available commands and features."""
    help_text = """
    Available Commands:
    • 'help' - Show this help menu
    • 'clear' - Clear the chat screen
    • 'history' - View chat history
    • 'exit' or 'bye' - End the chat session
    
    Tips:
    • Type your questions naturally
    • You can ask about courses, fees, campus life, etc.
    • Use 'clear' if your screen gets too cluttered
    """
    console.print(Panel(help_text, title="Help Menu", style="bold green"))

def start_chat():
    """Main chatbot function with enhanced user interface."""
    clear_screen()
    display_welcome_banner()
    
    responses = load_responses()
    if not responses:
        return

    # Use questionary for better input experience
    user_name = questionary.text(
        "Please enter your name:",
        validate=lambda text: len(text.strip()) > 0
    ).ask()

    agent_name, agent_personality = generate_agent_name()
    
    with Progress() as progress:
        task = progress.add_task("[cyan]Loading chat system...", total=100)
        while not progress.finished:
            progress.update(task, advance=0.7)
            time.sleep(0.02)

    clear_screen()
    display_welcome_banner()
    
    greeting = f"{time_based_greeting()}, {user_name}! Welcome to Poppleton University Chat."
    console.print(Panel(greeting, style="bold green"))
    simulate_typing(f"I'm {agent_name}, your {agent_personality} virtual assistant!")
    console.print("[yellow]Type 'help' to see available commands.[/yellow]")

    chat_log = []
    context = None

    while True:
        try:
            user_input = questionary.text(f"{Fore.GREEN}{user_name}>{Style.RESET_ALL} ").ask()
            
            if not user_input:
                continue
                
            user_input = user_input.strip().lower()
            chat_log.append(f"User: {user_input}")

            # Command handling
            if user_input in ["bye", "quit", "exit"]:
                farewell_message = f"It was nice chatting with you, {user_name}. Have a great day! 👋"
                console.print(Panel(farewell_message, style="bold blue"))
                chat_log.append(f"Agent: {farewell_message}")
                break
                
            elif user_input == "help":
                show_help_menu()
                continue
                
            elif user_input == "clear":
                clear_screen()
                display_welcome_banner()
                continue
                
            elif user_input == "history":
                console.print(Panel("\n".join(chat_log[-10:]), title="Recent Chat History"))
                continue

            # Context and response handling
            if match_pattern(user_input, ["courses", "classes"]):
                context = "courses"
            elif match_pattern(user_input, ["fees", "tuition"]):
                context = "fees"

            response = None
            if context == "courses" and match_pattern(user_input, ["details", "subjects"]):
                response = "We offer detailed syllabi for all courses on our website."
            elif context == "fees" and match_pattern(user_input, ["cost", "price"]):
                response = "Our tuition fees vary by program. Please visit our fees page for detailed information."

            if not response:
                for item in responses:
                    if match_pattern(user_input, item["patterns"]):
                        response = random.choice(item["responses"])
                        break

            if not response:
                response = random.choice([
                    "I'm not quite sure about that. Could you rephrase your question?",
                    "Interesting question! Could you provide more details?",
                    "I'd like to help better - could you elaborate on that?",
                    "I'm here to help, but I might need more specific information."
                ])

            if random.random() < 0.5:
                response = f"{user_name}, {response}"

            console.print(f"{Fore.BLUE}{agent_name}:{Style.RESET_ALL}", end=" ")
            simulate_typing(response)
            chat_log.append(f"Agent: {response}")

        except KeyboardInterrupt:
            console.print("\n[yellow]Chat interrupted. Type 'exit' to leave properly.[/yellow]")
            continue
        except Exception as e:
            console.print(f"[red]An error occurred: {str(e)}[/red]")
            continue

    log_session(user_name, chat_log)

if __name__ == "__main__":
    try:
        start_chat()
    except Exception as e:
        console.print(f"[red]Critical error: {str(e)}[/red]")