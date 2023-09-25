letters={}
for i in range(0,26):
    letters[i] = chr(i+97)
cypher = int(input("Choose a secret number: "))
text = input("Enter your secret text: ")


def encrypt(text, number):
    text = text.lower()
    result = ""
    for i in range(len(text)):
        if text[i].isalpha():
            index = (ord(text[i])-97+cypher)%26
            result += letters[index]
        else:
            result += text[i]    
    return result


def decrypt(text, number):
    text = text.lower()
    result = ""
    for i in range(len(text)):
        if text[i].isalpha():
            index = (ord(text[i])-97-cypher)%26
            result += letters[index]
        else:
            result += text[i]
    return result
            
            
encrypted_message = encrypt(text,cypher)
print(encrypted_message)
decrypted_message = decrypt(encrypted_message,cypher)
print(decrypted_message)
print(ord("a"))