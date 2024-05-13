def create_mapping(base_cipher=28, base_plain='e', factor=2):
    # Calculate the offset
    offset = base_cipher - (ord(base_plain) * factor)

    # Create a mapping dictionary
    mapping = {}
    for i in range(26):  # For each lowercase letter
        plain_char = chr(ord('a') + i)
        cipher_value = ord(plain_char) * factor + offset
        mapping[cipher_value] = plain_char

    return mapping


def decrypt_with_mapping(ciphertext, mapping):
    plaintext = ""
    for number in ciphertext:
        if number in mapping:
            plaintext += mapping[number]
        else:
            plaintext += '?'
    return plaintext


# Create the mapping dictionary
mapping = create_mapping()

# Example list of ciphertext numbers
ciphertext_numbers = [20, 22, 42, 20, 24, 40, 34, 48, 42, 28, 36, 56, 20, 54, 28, 32, 36, 48, 46, 48, 30, 56, 50, 20, 24, 28, 58, 36, 44, 28, 64, 34, 28, 54, 28, 32, 54, 20, 62, 36, 58, 68, 36, 56, 56, 48, 56, 58, 54, 48, 46, 32, 58, 34, 20, 58, 46, 48, 58, 34, 36, 46, 32, 46, 48, 50, 20, 54, 58, 36, 24, 42, 28, 56, 48, 54, 28, 62, 28, 46, 28, 42, 28, 24, 58, 54, 48, 44, 20, 32, 46, 28, 58, 36, 24, 54, 20, 26, 36, 20, 58, 36, 48, 46, 56, 60, 24, 34, 20, 56, 42, 36, 32, 34, 58, 24, 20, 46, 28, 56, 24, 20, 50, 28, 30, 54, 48, 44, 36, 58, 58, 34, 28, 58, 34, 28, 48, 54, 68, 48, 30, 32, 28, 46, 28, 54, 20, 42, 54, 28, 42, 20, 58, 36, 62, 36, 58, 68, 50, 54, 28, 26, 36, 24, 58, 56, 58, 34, 20, 58, 20, 56, 60, 30, 30, 36, 24, 36, 28, 46, 58, 42, 68, 24, 48, 44, 50, 20, 24, 58, 44, 20, 56, 56, 24, 20, 46, 26, 28, 30, 48, 54, 44, 56, 50, 20, 24, 28, 58, 36, 44, 28, 58, 48, 30, 48, 54, 44, 20, 22, 42, 20, 24, 40, 34, 48, 42, 28, 58, 34, 28, 22, 48, 60, 46, 26, 20, 54, 68, 48, 30, 58, 34, 28, 54, 28, 32, 36, 48, 46, 30, 54, 48, 44, 64, 34, 36, 24, 34, 46, 48, 28, 56, 24, 20, 50, 28, 36, 56, 50, 48, 56, 56, 36, 22, 42, 28, 36, 56, 24, 20, 42, 42, 28, 26, 58, 34, 28, 28, 62, 28, 46, 58, 34, 48, 54, 36, 70, 48, 46, 20, 42, 58, 34, 48, 60, 32, 34, 58, 34, 28, 28, 62, 28, 46, 58, 34, 48, 54, 36, 70, 48, 46, 34, 20, 56, 20, 46, 28, 46, 48, 54, 44, 48, 60, 56, 28, 30, 30, 28, 24, 58, 48, 46, 58, 34, 28, 30, 20, 58, 28, 20, 46, 26, 24, 36, 54, 24, 60, 44, 56, 58, 20, 46, 24, 28, 56, 48, 30, 20, 46, 48, 22, 38, 28, 24, 58, 24, 54, 48, 56, 56, 36, 46, 32, 36, 58, 36, 58, 34, 20, 56, 46, 48, 42, 48, 24, 20, 42, 42, 68, 26, 28, 58, 28, 24, 58, 20, 22, 42, 28, 30, 28, 20, 58, 60, 54, 28, 56, 36, 46, 44, 20, 46, 68, 64, 20, 68, 56, 20, 22, 42, 20, 24, 40, 34, 48, 42, 28, 20, 24, 58, 56, 42, 36, 40, 28, 20, 46, 36, 26, 28, 20, 42, 22, 42, 20, 24, 40, 22, 48, 26, 68, 20, 56, 36, 58, 54, 28, 30, 42, 28, 24, 58, 56, 46, 48, 42, 36, 32, 34, 58, 44, 48, 54, 28, 48, 62, 28, 54, 52, 60, 20, 46, 58, 60, 44, 30, 36, 28, 42, 26, 58, 34, 28, 48, 54, 68, 36, 46, 24, 60, 54, 62, 28, 26, 56, 50, 20, 24, 28, 58, 36, 44, 28, 50, 54, 28, 26, 36, 24, 58, 56, 58, 34, 20, 58, 28, 62, 28, 46, 58, 34, 48, 54, 36, 70, 48, 46, 56, 28, 44, 36, 58, 34, 20, 64, 40, 36, 46, 32, 54, 20, 26, 36, 20, 58, 36, 48, 46, 64, 36, 58, 34, 58, 34, 28, 56, 20, 44, 28, 56, 50, 28, 24, 58, 54, 60, 44, 20, 56, 20, 22, 42, 20, 24, 40, 22, 48, 26, 68, 48, 30, 20, 58, 28, 44, 50, 28, 54, 20, 58, 60, 54, 28, 36, 46, 62, 28, 54, 56, 28, 42, 68, 50, 54, 48, 50, 48, 54, 58, 36, 48, 46, 20, 42, 58, 48, 36, 58, 56, 44, 20, 56, 56, 58, 34, 36, 56, 58, 28, 44, 50, 28, 54, 20, 58, 60, 54, 28, 36, 56, 48, 46, 58, 34, 28, 48, 54, 26, 28, 54, 48, 30, 22, 36, 42, 42, 36, 48, 46, 58, 34, 56, 48, 30, 20, 40, 28, 42, 62, 36, 46, 30, 48, 54, 22, 42, 20, 24, 40, 34, 48, 42, 28, 56, 48, 30, 56, 58, 28, 42, 42, 20, 54, 44, 20, 56, 56, 44, 20, 40, 36, 46, 32, 36, 58, 28, 56, 56, 28, 46, 58, 36, 20, 42, 42, 68, 36, 44, 50, 48, 56, 56, 36, 22, 42, 28, 58, 48, 48, 22, 56, 28, 54, 62, 28, 48, 22, 38, 28, 24, 58, 56, 64, 34, 48, 56, 28, 32, 54, 20, 62, 36, 58, 20, 58, 36, 48, 46, 20, 42, 30, 36, 28, 42, 26, 56, 20, 54, 28, 58, 48, 48, 56, 58, 54, 48, 46, 32, 30, 48, 54, 42, 36, 32, 34, 58, 58, 48, 28, 56, 24, 20, 50, 28, 64, 28, 54, 28, 30, 36, 54, 56, 58, 24, 48, 46, 56, 36, 26, 28, 54, 28, 26, 36, 46, 58, 34, 28, 28, 36, 32, 34, 58, 28, 28, 46, 58, 34, 24, 28, 46, 58, 60, 54, 68, 22, 68, 38, 48, 34, 46, 44, 36, 24, 34, 28, 42, 42, 20, 46, 26, 50, 36, 28, 54, 54, 28, 56, 36, 44, 48, 46, 42, 20, 50, 42, 20, 24, 28, 58, 34, 28, 30, 36, 54, 56, 58, 44, 48, 26, 28, 54, 46, 58, 34, 28, 48, 54, 68, 48, 30, 32, 28, 46, 28, 54, 20, 42, 54, 28, 42, 20, 58, 36, 62, 36, 58, 68, 58, 34, 20, 58, 64, 48, 60, 42, 26, 24, 34, 20, 54, 20, 24, 58, 28, 54, 36, 70, 28, 20, 22, 42, 20, 24, 40, 34, 48, 42, 28, 64, 20, 56, 26, 28, 56, 24, 54, 36, 22, 28, 26, 22, 68, 40, 20, 54, 42, 56, 24, 34, 64, 20, 54, 70, 56, 24, 34, 36, 42, 26]

# Decrypt using the mapping dictionary
decrypted_text = decrypt_with_mapping(ciphertext_numbers, mapping)
print("Decrypted Text:", decrypted_text)
