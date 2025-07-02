print("Welcome To CAESAR CIPHER ")

image = '''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88 '''

print(image)
def encrypt(message, shift):
    #message = message.lower()
    ans = ""
    for ch in message:
        if ch == " ":
            ans += " "
        elif "A"<=ch<="Z":
            shifted = (ord(ch) - ord('A') + shift) % 26
            ans += chr(ord('A') + shifted)
        elif "a"<=ch<="z":
            shifted = (ord(ch)-ord('a')+shift)%26
            ans += chr(ord('a')+shifted)
        else:
            ans += ch

    print(ans)
    return ans


def decrypt(message,shift):
    ans = ""
    for ch in message:
        if ch == " ":
            ans += " "
        elif "A" <= ch <= "Z":
            shifted = (ord(ch) - ord('A') - shift) % 26
            ans += chr(ord('A') + shifted)
        elif "a" <= ch <= "z":
            shifted = (ord(ch) - ord('a') - shift) % 26
            ans += chr(ord('a') + shifted)
        else:
            ans += ch

    print(ans)
    return ans

#Function calling
play = input("Do you wish to encrypt. Type 'yes' or 'no': ").lower()

while play=='yes':

    work = input("Do you wish to encrypt or decrypt: ")

    if work == "encrypt":
        mess = input("Write your message to encrypt: ")
        shift = int(input("How much shift you want in encryption: "))
        ans = encrypt(mess, shift)
        print("**************************************************************************")


    elif work == "decrypt":
        mess = input("Write your message to decrypt: ")
        shift = int(input("How much shift you want in decryption: "))
        ans = decrypt(mess, shift)
        print("**************************************************************************")

    else:
        print("Invalid. Type that is acceptable")


    play = input("Do you wish to encrypt. Type 'yes' or 'no': ").lower()