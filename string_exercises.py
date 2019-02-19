test_string = "Leet"

#Function returns a string in all uppercase
def upperString(string):
    return string.upper()

#Function returns a string that has been capitalized
def capitalizeString(string):
    firstLetter = string[0].upper()
    result = firstLetter
    count = 1
    while(count < len(string)):
        result += string[count]
        count += 1
    return result

#Function returns a string in reverse
def reverseString(string):
    count = len(string) - 1
    result = ""
    while count >= 0:
        result += string[count]
        count -= 1
    return result

#Function returns a LeetSpeak using a dictionary
def leetspeak(string):
    result = ""
    leetDict = {
        "A": 4,
        "E": 3,
        "G": 6,
        "I": 1,
        "O": 0,
        "S": 5,
        "T": 7 
    }

    for char in string.upper():
        if char in leetDict.keys():
            result += str(leetDict[char])
        if char not in leetDict.keys():
            result += char
        
    return result

#Function that extends long vowels
def long_vowel(string):
    count = 0
    index = 0
    for letter in string:
        if letter in ("a", "e", "i", "o", "u"):
            count += 1
        if count == 2:
            return string[:index] + (letter * 3) + string[index:]
        index += 1

cipher = "lbh zhfg hayrnea jung lbh unir yrnearq"
ciper_dict1 = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7, 
    
}

#Function that returns Caesar Cipher encryption
def caesar_cipher_encrypt(string):
    return 

#Function that returns Caesar Cipher Decryption
def caesar_cipher_decrypt(string):
    return

print(caesar_cipher_decrypt(cipher))