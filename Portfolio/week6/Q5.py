# This program hides a message by spacing its letters at random intervals and filling gaps with random letters.

import random
import string

def interval_encrypt(msg):
    gap = random.randint(2, 20)
    result = []
    msg_index = 0
    for i in range(len(msg) * gap):
        if i % gap == 0 and msg_index < len(msg):
            result.append(msg[msg_index])
            msg_index += 1
        else:
            result.append(random.choice(string.ascii_letters))
    return "".join(result), gap

# Test
encrypted_msg, gap = interval_encrypt("send cheese")
print("Encrypted message:", encrypted_msg)
print("Interval:", gap)
