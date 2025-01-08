# IntelliChat: A Python Chatbot

IntelliChat is an interactive chatbot implemented in Python. It uses pattern matching with regex to respond to user inputs based on a predefined JSON file of responses. The chatbot provides a friendly user experience, including a typing simulation, session logging, and contextual responses.

---

## Features

- **Dynamic Responses**: Supports dynamic loading of responses from a JSON file.
- **Pattern Matching**: Matches user inputs with regex patterns for intelligent responses.
- **Time-based Greetings**: Greets users appropriately based on the current time.
- **Agent Names**: Randomly selects and introduces itself with one of several predefined agent names.
- **Chat Logs**: Saves chat logs to a text file for future reference.
- **Typing Simulation**: Simulates typing for a more human-like interaction.
- **Help Command**: Displays available topics and patterns for user guidance.
- **Fallback Handling**: Provides default responses when no patterns match.

---

## Requirements

- Python 3.7 or higher

---

## Installation

1. Clone the repository or download the script.
2. Ensure you have Python installed on your system.
3. Install any necessary dependencies (optional, but `time`, `datetime`, `random`, `json`, and `re` are part of Python’s standard library).

---

## Usage

### Preparing the Responses File

Create a `responses.json` file in the same directory as the chatbot script. The structure should look like this:

```json
[
  {
    "tag": "greeting",
    "patterns": ["hello", "hi", "hey"],
    "responses": ["Hello! How can I help you?", "Hi there!"]
  },
  {
    "tag": "fallback",
    "patterns": [],
    "responses": ["I'm not sure I can help with that.", "Could you clarify your question?"]
  }
]
```

### Running the Chatbot

1. Run the script using:
   ```bash
   python chatbot.py
   ```
2. Enter your name when prompted.
3. Interact with the chatbot by typing your queries.
4. Type `help` to view available topics.
5. Type `bye`, `quit`, or `exit` to end the session.

### Chat Logs

Chat logs are saved automatically in the format:
```
chat_log_<user_name>_<timestamp>.txt
```

---

## Code Overview

### Main Components

- **`load_responses`**: Loads responses from the JSON file.
- **`validate_responses`**: Ensures the JSON structure is correct.
- **`match_pattern`**: Matches user inputs with predefined patterns.
- **`simulate_typing`**: Simulates typing for a natural experience.
- **`log_session`**: Saves chat logs to a file.
- **`time_based_greeting`**: Provides a greeting based on the current time.
- **`get_response`**: Retrieves the appropriate response based on user input.

### Key Functions

| Function              | Purpose                                      |
|-----------------------|----------------------------------------------|
| `validate_responses`  | Validates the JSON response structure.      |
| `load_responses`      | Loads and parses the JSON file.             |
| `match_pattern`       | Matches user input with regex patterns.     |
| `simulate_typing`     | Simulates typing effect for responses.      |
| `log_session`         | Logs the chat session to a file.            |
| `time_based_greeting` | Generates time-based greetings.             |
| `get_response`        | Retrieves a matching or fallback response.  |

---

## Customization

### Adding New Responses

1. Open the `responses.json` file.
2. Add a new response entry:

```json
{
  "tag": "new_topic",
  "patterns": ["pattern1", "pattern2"],
  "responses": ["Response 1", "Response 2"]
}
```

3. Save the file and restart the chatbot.

### Changing Agent Names

1. Modify the `agent_names` list in the `generate_agent_name` function.

```python
agent_names = ["Alice", "Bob", "Charlie"]
```

---

## Error Handling

- **Invalid JSON**: The chatbot validates and reports issues with the `responses.json` structure.
- **File Not Found**: If the `responses.json` file is missing, the chatbot exits gracefully.
- **Empty Input**: Prompts users to enter meaningful input instead of falling back unnecessarily.

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

---

## Future Enhancements

- Add support for more advanced NLP techniques.
- Integrate a graphical user interface (GUI).
- Enable dynamic learning of new patterns and responses.
- Support multiple languages.

