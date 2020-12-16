from cryptography.fernet import Fernet

def generatePassKey():
    key= Fernet.generate_key()
    keyFile= open("PasswordKey.key",'wb')
    keyFile.write(key)
    keyFile.close

def getMyKey():
    keyFile = open("PasswordKey.key",'rb')
    key = keyFile.read()
    keyFile.close()
    return key
    
def encryptMessage(message_Normal):
     key= getMyKey()
     k= Fernet(key)
     encrypted_Message= k.encrypt(message_Normal)
     return encrypted_Message

def decryptMessage(message_Secret):
     key= getMyKey()
     k= Fernet(key)
     decrypted_Message= k.decrypt(message_Secret)
     return decrypted_Message

if __name__ == "__main__":
    generatePassKey()
    
    print("Welcome to Cryptography App\n")
    
    while True:
        print("1. Show Your Secret Key on Screen")
        print("2. Encrypt Text")
        print("3. Decrypt Text")
        choice= int(input("Enter Your Choice:\n"))
    
        if choice == 1:
            key= getMyKey()
            print(key)
        elif choice == 2:
            message= input(b"Enter Text To Encrypt: ").encode()
            emessage= encryptMessage(message)
            print(emessage)
        elif choice == 3:
            enc_message= input(b"Enter Message To Be Decrypted:").encode()
            dec_message= decryptMessage(enc_message)
            print(dec_message.decode())
        else:
            break
        










