from cryptography.fernet import Fernet

# key =  Fernet.generate_key()
# print(key)

key = b'5ypXLnou0AsbRzlud-j0XZ3gcfSqXGRCEowX8vyL8Rw='
print(key.decode())
fernet = Fernet(key)
encrypt_str = fernet.encrypt(b"2")
print(encrypt_str.decode())

decrypt_str =  fernet.decrypt(encrypt_str)
print(type(decrypt_str))
print(decrypt_str.decode())