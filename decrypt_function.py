from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

def decrypt_data(encrypted_data, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(base64.b64decode(encrypted_data)), AES.block_size)
    return decrypted
