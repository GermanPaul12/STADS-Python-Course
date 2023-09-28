letters={}
for i in range(0,26):
    letters[i] = chr(i+97)
#cypher = int(input("Choose a secret number: "))
#text = input("Enter your secret text: ")

cypher = 3
text = "woir treffen uns am bahnhof um 16 uhr! Sei dort"

def encrypt(text, num):
    res = ""
    text = text.lower()
    for i in text:
        if i.isalpha():
            index = (ord(i)-97+num)%26 
            #print(ord(i)%26+num)
            #print(letters[index])
            res += letters[index]
        else:
            res += i    
    return res        

def decrypt(text, num):
    res = ""
    text = text.lower()
    for i in text:
        if i.isalpha():
            index = (ord(i)-97-num)%26 
            #print(ord(i)%26-num)
            #print(letters[index])
            res += letters[index]
        else:
            res += i  
    return res
        
encrypted = encrypt(text,cypher)
print(encrypted)           
print(decrypt(encrypted, cypher)) 