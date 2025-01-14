# This program removes spaces from a message and reverses it to "encrypt" it.

def simple_encrypt(msg):
    return msg.replace(" ", "")[::-1]

# Test
print(simple_encrypt("hello world"))  # Output: "dlrowolleh"
