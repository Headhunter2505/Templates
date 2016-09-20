from simplecrypt import encrypt, decrypt

data = "Hello world"
key = "some_key"

encrypted_data = encrypt(password=key, data=data)

print(encrypted_data)

decrypted_data = decrypt(password=key, data=encrypted_data)

print(decrypted_data)
