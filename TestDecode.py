from Crypto.Cipher import AES
import base64


class Encrypt:
    def __init__(self, key, bs=32):
        pad = lambda s: s + (bs - len(s)) * "\0"
        key = pad(key)
        self.key = key.encode('utf-8')

    def aes_decrypt(self, content):
        str = base64.b64decode(content)
        iv = str[0:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return cipher.decrypt(base64.b64decode(str[16:])).decode('utf-8')


key = "88MVdZ9"
decryptor = Encrypt(key)
decrypted_content = decryptor.aes_decrypt(
    'MmRmNGFkZDE4NTIyNTBhYytYZy9PNEVqZjlUOUNJRm55TDV2MUR6cm9KRnkxOXFNbEcrNzBzdThwaUtYcFUrVDdGUEpWM1lvNGRKTGpFU0hRemZLekl3M21YZWJZT3BMQ0dEaGlXWUUvSHVGVUlZNWNnK0tXTjQyc2x0OHRicGhzMUpxd016WU4vVnpxY09OdXpjYk9yVEI1VkozUll6UThXbnJOb0ZoVzkrODc5NnpnMllic1FOSzhiZz0=')
print(decrypted_content)