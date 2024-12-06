from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)
fernet = Fernet(key)

message = input('Enter your message >> ').encode('utf-8')
encrypted_message = fernet.encrypt(message)
print('Encrypted message: ', encrypted_message)

decrypted_message = fernet.decrypt(encrypted_message)
print('Decrypted message: ', decrypted_message.decode('utf-8'))
