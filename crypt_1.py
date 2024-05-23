import os
from cryptography.fernet import Fernet

userInp = int(input("Choose one option\n[ '(1) encrypt' , '(2) decrypt' ]\n"))

key = b"OBk3PBcFFZJv7m9QJetJAR0sUlqfXV6nycPCxp7paQQ="

files = [f for f in os.listdir() if os.path.isfile(os.path.join(f))]

f = Fernet(key)

def encrypter():
    
    for i in files:
        if i != 'crypt_1.py':
            with open(f'{i}','rb') as reader:
                rd = reader.read()
                token = f.encrypt(rd)
                with open(f'{i}','wb') as writer:
                    writer.write(token)
                    print(f"Encrypted successfully")
                    reader.close()
                    writer.close()
                    
def decrypter():
    
    for i in files:
        if i != 'crypt_1.py':
            with open(f'{i}','rb') as reader:
                token = reader.read()
                file = f.decrypt(token)
                with open(f'{i}','wb') as writer:
                    writer.write(file)
                    print('Decrypted successfully')
                    reader.close()
                    writer.close()
           

if userInp == 1:
    encrypter()
elif userInp == 2:
    decrypter()
else:
    print("Exit")