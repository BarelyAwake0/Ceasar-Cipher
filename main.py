import string

ALPHA = list(string.ascii_lowercase)


def encrypt(string, key):

    cipher = ALPHA.copy() 

    #set-up cipher
    if key > 0:
        for i in range(key):
            x = cipher.pop(0)
            cipher.append(x)
    #print(cipher)
    elif key < 0:
        for i in range(abs(key)):
            x = cipher.pop(25)
            cipher.insert(0, x)

    #msg to list conversion mk2
    msg_low = string.lower()
    split_msg = msg_low.split(" ")

    code = []

    #msg to cipher
    for x in range(len(split_msg)):
        word = list(split_msg[x])
        for y in range(len(word)):
            for z in range(len(ALPHA)):
                if word[y] == ALPHA[z]:
                    position = z
            code_letter = cipher[position]
            code.append(code_letter)
        code.append(" ")

    encrypted = "".join(code)
    
    return encrypted


def decrypt(string, key):

    cipher = ALPHA.copy()

    # set-up cipher
    if key > 0:
        for i in range(key):
            x = cipher.pop(0)
            cipher.append(x)
    elif key < 0:
        for i in range(abs(key)):
            x = cipher.pop(25)
            cipher.insert(0, x)

    #encrypted to list conversion mk2
    msg_low = string.lower()
    split_msg = msg_low.split(" ")

    code = []

    # msg to cipher
    for x in range(len(split_msg)):
        word = list(split_msg[x])
        for y in range(len(word)):
            for z in range(len(cipher)):
                if word[y] == cipher[z]:
                    position = z
            alpha_letter = ALPHA[position]
            code.append(alpha_letter)
        code.append(" ")
    decrypted = "".join(code)

    return decrypted


status = False

while status == False:

    mode = int(input('''Would you like to encrypt or decrypt a message?
1) Encrypt
2) Decrypt \n'''))

    if mode == 1:

        print("\nENCRYPT YOUR MESSAGE\n")

        msg = input("Please enter your message...\n")
        key = int(input("Please enter your key...\n"))

        print(f"\nEncrypted message:\n{encrypt(msg, key)}")
        status = True
    elif mode == 2:

        print("\nDECRYPT YOUR MESSAGE\n")

        msg = input("Please enter your encrypted message...\n")
        key = int(input("Please enter your key...\n"))

        print(f"Decrypted message:\n{decrypt(msg,key)}")
        status = True
    else:
        print("Please select a valid option...\n")
        status = False

print("\nENCRYPTION/DECRYPTION COMPLETE\n")