def cipher(str):
    def conv_char(c):
        if c.islower():
            return chr(219 - ord(c))
        else:
            return c

    return ''.join([conv_char(c) for c in str])

if __name__ == '__main__':
    plain = 'Hello world!'
    encrypted = cipher(plain)
    decrypted = cipher(encrypted)

    print(plain)
    print(encrypted)
    print(decrypted)
