key = 'aJwPjk129fK1zq0mber?df1!'

def encrypt(password):
    encoded_chars = []
    for i in range(len(password)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(password[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    return encoded_string

def decrypt(password):
    encoded_chars = []
    for i in range(len(password)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(password[i]) - ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    return encoded_string