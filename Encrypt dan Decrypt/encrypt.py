# pip install rsa
import rsa

publicKey, privateKey = rsa.newkeys(1024)

message = input("Enter a message: ")

def encrypt(str):
    encMessage = rsa.encrypt(str.encode(),publicKey)
    print('\n')
    return encMessage

def decrypt(encMsg):
    decMessage = rsa.decrypt(encMsg, privateKey).decode()
    print('\n')
    return decMessage

print("Encrypt Message:", encrypt(message))
print('\n')

displayDecrypt = input("Apakah mau menampilkan hasil Decrypt? [y/n]: ")
if (displayDecrypt == 'y' or displayDecrypt == 'Y'):
    print("Decrypted Message:", decrypt(encrypt(message)))
else:
    exit()