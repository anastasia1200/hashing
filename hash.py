import math

def hash_division():
    text = input("Enter some text: ")
    text_list = text.split()
    hash_value = ''
    keys = [0] * len(text_list)
    for i in range(len(text_list)):
        for j in range(len(text_list[i])):
            keys[i] += ord(text_list[i][j])
    if len(text_list) == 1:
        hash_value = str(keys[0])
    else:
        for i in range(len(keys)):
            hash_value += str(keys[i] % len(text_list))
    print(f"The hash value of '{text}' is {hash_value}")

def hash_md5():
    text = input("Enter some text: ")
    s = [7, 12, 17, 22] * 4 + [5, 9, 14, 20] * 4 + [4, 11, 16, 23] * 4 + [6, 10, 15, 21] * 4
    K = [int(abs(math.sin(i + 1)) * 2 ** 32) & 0xFFFFFFFF for i in range(64)]
    a, b, c, d = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476
    message = bytearray(text.encode())
    message_len = (8 * len(message)) & 0xffffffffffffffff
    message.append(0x80)
    while len(message) % 64 != 56:
        message.append(0)
    message += message_len.to_bytes(8, byteorder='little')
    for i in range(0, len(message), 64):
        block = message[i:i + 64]
        A, B, C, D = a, b, c, d
        for j in range(64):
            if j < 16:
                F = (B & C) | ((~B) & D)
                g = j
            elif j < 32:
                F = (D & B) | ((~D) & C)
                g = (5 * j + 1) % 16
            elif j < 48:
                F = B ^ C ^ D
                g = (3 * j + 5) % 16
            else:
                F = C ^ (B | (~D))
                g = (7 * j) % 16
            F = (F + A + K[j] + int.from_bytes(block[4 * g:4 * g + 4], byteorder='little')) & 0xFFFFFFFF
            A, D, C, B = D, C, B, (B + ((F << s[j]) | (F >> (32 - s[j])))) & 0xFFFFFFFF
        a = (a + A) & 0xFFFFFFFF
        b = (b + B) & 0xFFFFFFFF
        c = (c + C) & 0xFFFFFFFF
        d = (d + D) & 0xFFFFFFFF
    hash_value = ((a << 96) | (b << 64) | (c << 32) | d)
    hash_value = format(hash_value, '032x')
    print(f"The MD5 hash value of '{text}' is {hash_value}")

while True:
    x = input('Input a task: ')
    if x == '1':
        hash_division()
    elif x == '2':
        hash_md5()
    elif x == '0':
        break
    else:
        print('Wrong input!')
