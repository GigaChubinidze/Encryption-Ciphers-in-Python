import string

class Ciphers:
    def encryptAtbashCipher(text):
        switcher = {" ": " ", "a": "z", "b": "y", "c": "x", "d": "w", "e": "v", "f": "u", "g": "t", "h": "s", "i": "r", "j": "q", "k": "p", "l": "o", "m": "n", "n": "m", "o": "l","p": "k", "q": "j", "r": "i", "s": "h", "t": "g","u": "f", "v": "e", "w": "d", "x": "c", "y": "b", "z": "a"}

        list = []
        for i in text:
            if i in switcher:
                list.append(switcher[i])

        return "".join(list)


    def decryptAtbashCipher(text):
        switcher = {" ": " ", "a": "z", "b": "y", "c": "x", "d": "w", "e": "v", "f": "u", "g": "t", "h": "s", "i": "r", "j": "q", "k": "p", "l": "o", "m": "n", "n": "m", "o": "l", "p": "k", "q": "j", "r": "i", "s": "h", "t": "g", "u": "f", "v": "e", "w": "d", "x": "c", "y": "b", "z": "a"}

        list = []
        for i in text:
            if i in switcher:
                list.append(switcher[i])

        return "".join(list)


    def encryptCaesarCipher(text, key):
        list = []
        special_dict = {".": ",", ",": ".", "!": "?", "?": "!", "0": "1", "1": "0", "2": "3", "3": "2", "4": "5", "5": "4", "6": "7", "7": "6", "8": "9", "9": "8"}

        for i in text:
            if i.isupper():
                list.append(chr((ord(i) + key - 65) % 26 + 65))
            elif i.islower():
                list.append(chr((ord(i) + key - 97) % 26 + 97))
            elif i == " ":
                list.append(i)
            elif i.isalpha():
                list.append(ord(chr(i) + key % 26))
            elif special_dict.__contains__(i):
                list.append(special_dict[i])
            else:
                list.append(i)

        return "".join(list)


    def decryptCaesarCipher(text, key):
        list = []
        special_dict = {".": ",", ",": ".", "!": "?", "?": "!", "0": "1", "1": "0", "2": "3", "3": "2", "4": "5", "5": "4", "6": "7", "7": "6", "8": "9", "9": "8"}

        for i in text:
            if i.isupper():
                list.append(chr((ord(i) - key - 65) % 26 + 65))
            elif i.islower():
                list.append(chr((ord(i) - key - 97) % 26 + 97))
            elif i == " ":
                list.append(i)
            elif i.isalpha():
                list.append(ord(chr(i) + key % 26))
            elif special_dict.__contains__(i):
                list.append(special_dict[i])
            else:
                list.append(i)

        return "".join(list)


    def encryptVigenereCipher(text, keyList):
        keys_to_nums = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9: "j", 10: "k", 11: "l", 12: "m", 13: "n", 14: "o", 15: "p", 16: "q", 17: "r", 18: "s", 19: "t", 20: "u", 21: "v", 22: "w", 23: "x", 24: "y", 25: "z"}
        list_of_keys = []

        fixed_key_list = []
        for i in keyList:
            fixed_key_list.append(i % 26)

        for i in fixed_key_list:
            list_of_keys.append(keys_to_nums[i])
        key = "".join(list_of_keys)

        if len(key) <= len(text):
            final_key = key * (len(text) // len(key)) + key[:len(text) % len(key)]

        result = []
        alph = string.ascii_lowercase
        i = 1
        for char in final_key:
            alphabet = string.ascii_lowercase
            ch = char.lower()
            new_alphabet = alphabet[alphabet.index(ch):] + alphabet[:alphabet.index(ch)]

            for j in text:
                if alph.count(j) == 1:
                    result.append(new_alphabet[alph.index(j)])
                    text = text[i:]
                    break
                elif alph.count(j.lower()) == 1:
                    result.append((new_alphabet[alph.index(j.lower())].upper()))
                    text = text[i:]
                    break
                else:
                    result.append(j)
                    text = text[i:]
                    break
        special_dict = {".": ",", ",": ".", "!": "?", "?": "!", "0": "1", "1": "0", "2": "3", "3": "2", "4": "5", "5": "4", "6": "7", "7": "6", "8": "9", "9": "8"}
        final_result = []
        for k in result:
            if special_dict.__contains__(k):
                final_result.append(special_dict[k])
            else:
                final_result.append(k)

        return "".join(final_result)


    def decryptVigenereCipher(text, keyList):
        keys_to_nums = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9: "j", 10: "k", 11: "l", 12: "m", 13: "n", 14: "o", 15: "p", 16: "q", 17: "r", 18: "s", 19: "t", 20: "u", 21: "v", 22: "w", 23: "x", 24: "y", 25: "z"}
        list_of_keys = []

        fixed_key_list = []
        for i in keyList:
            fixed_key_list.append(i % 26)

        for i in fixed_key_list:
            list_of_keys.append(keys_to_nums[i])
        key = "".join(list_of_keys)

        if len(key) <= len(text):
            final_key = key * (len(text) // len(key)) + key[:len(text) % len(key)]

        result = []
        alph = string.ascii_lowercase
        i = 1
        for char in final_key:
            alphabet = string.ascii_lowercase
            ch = char.lower()
            new_alphabet = alphabet[alphabet.index(ch):] + alphabet[:alphabet.index(ch)]

            for j in text:
                if alph.count(j) == 1:
                    result.append(alph[new_alphabet.index(j)])
                    text = text[i:]
                    break
                elif alph.count(j.lower()) == 1:
                    result.append((alph[new_alphabet.index(j.lower())].upper()))
                    text = text[i:]
                    break
                else:
                    result.append(j)
                    text = text[i:]
                    break
        special_dict = {".": ",", ",": ".", "!": "?", "?": "!", "0": "1", "1": "0", "2": "3", "3": "2", "4": "5", "5": "4", "6": "7", "7": "6", "8": "9", "9": "8"}
        final_result = []
        for k in result:
            if special_dict.__contains__(k):
                final_result.append(special_dict[k])
            else:
                final_result.append(k)

        return "".join(final_result)


    def encryptSimpleEnigmaCipher(text, keys):
        original_alphabet = string.ascii_lowercase
        original_word     = text
        word              = original_word.lower()
        result            = []
        space             = [" "]

        for i in range(len(word)):
            if word[i] not in original_alphabet and word[i] != " " and not word[i].isalpha():
                result.append(word[i])
            if word[i] in original_alphabet:
                result.append(keys[2][original_alphabet.index(keys[1][original_alphabet.index(keys[0][original_alphabet.index(word[i])])])])
            if original_word[i] == " ":
                result = result[:i] + space + result[i:]
            if original_word[i].isupper():
                result[i] = result[i].upper()

        return "".join(result)


    def decryptSimpleEnigmaCipher(text, keys):
        original_alphabet = string.ascii_lowercase
        original_word     = text
        word              = original_word.lower()
        result            = []
        space             = [" "]

        for i in range(len(word)):
            if word[i] not in original_alphabet and word[i] != " " and not word[i].isalpha():
                result.append(word[i])
            if word[i] in original_alphabet:
                result.append(original_alphabet[keys[0].index(original_alphabet[keys[1].index(original_alphabet[keys[2].index(word[i])])])])
            if original_word[i] == " ":
                result = result[:i] + space + result[i:]
            if original_word[i].isupper():
                result[i] = result[i].upper()

        return "".join(result)



key1 = "bcdefghijklmnopqrstuvwxyza"
key2 = "qwertyuioplkjhgfdsazxcvbnm"
key3 = "zxcvbnmlkjhgfdsaqwertyuiop"

# print(Ciphers.encryptAtbashCipher("programming")) # kiltiznnrmt
# print(Ciphers.encryptCaesarCipher("Cipher programming 101!", 2)) # Ekrjgt rtqitcookpi 010?
# print(Ciphers.encryptVigenereCipher("Cipher programming 101!",[1,3,2])) # Dlriht stpjtbpojqi 010?
# print(Ciphers.encryptSimpleEnigmaCipher("Cipher programming 101!",(key1,key2,key3))) # Wavsoz vznkzullamk 101!

# print(Ciphers.decryptAtbashCipher(Ciphers.encryptAtbashCipher("programming")))
# print(Ciphers.decryptCaesarCipher(Ciphers.encryptCaesarCipher("Cipher programming 101!",2),2))
# print(Ciphers.decryptVigenereCipher(Ciphers.encryptVigenereCipher("Cipher programming 101!",[1,3,2]),[1,3,2]))
# print(Ciphers.decryptSimpleEnigmaCipher(Ciphers.encryptSimpleEnigmaCipher("Cipher programming 101!",(key1,key2,key3)), (key1,key2,key3)))


