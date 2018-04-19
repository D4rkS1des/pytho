while True:
    def S_Z():
        # Шифрование
        def shifr():
            text = "hello world"
            keys = {
                'd': '$', 'e': '%', 'f': '^',
                'g': '&', 'h': '*', 'i': '(',
                'j': ')', 'k': '-', 'l': '=',
                'm': '+', 'n': '?', 'o': ':',
                'p': ';', 'q': '<', 'r': '>',
                's': '/', 't': '[', 'u': ']',
                'v': '{', 'w': '}', 'x': '|',
                'y': '.', 'z': ',', ' ': '~'
            }
            crypt = ""
            for i in text:
                if i in keys:
                    crypt += keys[i]
            with open('shifr.txt', 'w') as file:
                text = "Crypted text:\n" + crypt + "\n"
                file.write(text)

        # Расшифрование
        def rashifr():
            text = "*%==:~}:>=$"
            keys = {
                '!': 'a', '@': 'b', '#': 'c',
                '$': 'd', '%': 'e', '^': 'f',
                '&': 'g', '*': 'h', '(': 'i',
                ')': 'j', '-': 'k', '=': 'l',
                '+': 'm', '?': 'n', ':': 'o',
                ';': 'p', '<': 'q', '>': 'r',
                '/': 's', '[': 't', ']': 'u',
                '{': 'v', '}': 'w', '|': 'x',
                '.': 'y', ',': 'z', '~': ' '
            }
            decrypt = ""
            for i in text:
                if i in keys:
                    decrypt += keys[i]
            with open('shifr.txt', 'w') as file:
                text = "decrypted text:\n" + decrypt + "\n"
                file.write(text)
                # file.write(text.encode("utf-8"))

        k = input('что делаем с sz?(sh/rash)')
        if k == 'sh':
            shifr()
        elif k == 'rash':
            rashifr()
        else:
            print('hz')


    def cesarNew():
        cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
        if cryptMode not in ['E', 'D']:
            print("Error: mode is not Found!");
            raise SystemExit
        startMessage = input("Write the message: ").upper()
        try:
            rotKey = int(input("Write the key: "))
        except ValueError:
            print("Only numbers!");
            raise SystemExit

        def encryptDecrypt(mode, message, key, final=""):
            for symbol in message:
                if mode == 'E':
                    final += chr((ord(symbol) + key - 13) % 26 + ord('A'))
                else:
                    final += chr((ord(symbol) - key - 13) % 26 + ord('A'))
            return final

        print("Final message:", encryptDecrypt(cryptMode, startMessage, rotKey))
        with open('shifr.txt', 'w') as file:
            text = "Crypted/decrepted text:\n" + encryptDecrypt(cryptMode, startMessage, rotKey) + "\n"
            file.write(text)


    def shifr_c1():
        arr1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z', \
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

        arr2 = []
        for i in range(len(arr1)):
            arr2.append(arr1[i])

        def change_arr2():
            for i in range(number):
                arr2.append(arr2[0])
                arr2.remove(arr2[0])

        print("1) Crypt the text/file")
        print("2) Decrypt text from the file")
        print("3) Decrypt text from the terminal\n")

        try:

            ans = int(input("[*] Write the number:\n[number] > "))

            if ans == 1:
                number = int(input("[*] Write the key-number [0-%s]: " % (str(len(arr1)))))

                change_arr2()

                msg = input("\n[*] Write the text:\n[text] >> ")

                msgc = ""
                for i in msg:
                    for j in range(len(arr1)):
                        if i == arr1[j]:
                            msgc += arr2[j]
                crypt = open("shifr.txt", "w")
                print("\nCrypt-text: " + msgc + "\n")
                crypt.write(msgc)
                crypt.close()

                print(arr1)
                print()
                print(arr2)

            elif ans == 2:
                number = int(input("[*] Write the key-number [0-%s]: " % (str(len(arr1)))))

                change_arr2()

                decrypt_r = open("shifr.txt", "r")
                read = decrypt_r.read()
                msgd = ""
                for i in read:
                    for j in range(len(arr1)):
                        if i == arr2[j]:
                            msgd += arr1[j]
                print("\n[*] Decrypted text:")
                print("[text] << " + str(msgd))
                answer = input("\n[*] Save decrypted text in the file?\n[y/n] > ")
                if answer == "y" or answer == "Y":
                    decrypt_w = open("text_decrypt.txt", "w")
                    decrypt_w.write(msgd)
                    decrypt_w.close()
                    print("\n[+] File 'text_decrypt.txt' successfully saved! ")
                else:
                    pass
                decrypt_r.close()

            elif ans == 3:
                number = int(input("[*] Write the key-number [0-%s]: " % (str(len(arr1)))))

                change_arr2()

                msg = input("\n[*] Write the crypted text:\n[text] >> ")
                msgd = ""
                for i in msg:
                    for j in range(len(arr1)):
                        if i == arr2[j]:
                            msgd += arr1[j]
                print("\n[*] Decrypted text:")
                print("[text] << " + str(msgd))
            else:
                print("Number is not defined!")

        except ValueError:
            print("Error! Print only Integer numbers!")


    def replace():
        symbolsAlpha = [chr(x) for x in range(65, 91)]
        symbolsCrypt = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=',
                        '+', '?', ':', ';', '<', '>', '/', '[', ']', '{', '}', '|', '.', ',', '~']

        cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
        if cryptMode not in ['E', 'D']:
            print("Error: mode is not Found!");
            raise SystemExit
        startMessage = input("Write the message: ").upper()
        keys = dict(zip(symbolsAlpha, symbolsCrypt))

        def encryptDecrypt(mode, message, final=""):
            if mode == 'E':
                for symbol in message:
                    if symbol in keys: final += keys[symbol]
            else:
                for symbol in message:
                    for key in keys:
                        if symbol == keys[key]: final += key
            return final

        print("Final message:", encryptDecrypt(cryptMode, startMessage))
        with open('shifr.txt', 'w') as file:
            text = "Crypted text:\n" + encryptDecrypt(cryptMode, startMessage) + "\n"
            file.write(text)


    k = ''
    k = input('что делаем?(sz/cesar/cesar1/replace)')
    if k == 'sz':
        S_Z()
    elif k == 'cesar':
        cesarNew()
    elif k == 'cesar1':
        shifr_c1()
    elif k == 'replace':
        replace()
    else:
        print('Oshibka')
        break