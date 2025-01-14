# This program decrypts a message that was encoded using random intervals.

def interval_decrypt(encrypted_msg, gap):
    return "".join([encrypted_msg[i] for i in range(0, len(encrypted_msg), gap)])

# Test
encrypted_msg = "sxyexynxydxycxyhxyexyexysxye"
gap = 3
print(interval_decrypt(encrypted_msg, gap))  # Output: "sendcheese"
