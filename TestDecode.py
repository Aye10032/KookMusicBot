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

msg = 'YmQ5MzgyOTE0ODZlNWZkMnJhREV0NEJJOEdrVTNyQUs4SVAvcDZmNXhZaUNMZDV2bGErelRIcVA1TCtpcXBlNTJQVitFUDVGZS9vV1dWQXZlTzRhOEEzeWZMSWlPa0hxZDdlcEVkZlNhOVZuZE5odXVpVmFOLzRhQXhWUFJCa3FRSUhNeFpsYWlycGRyMnVKa0c3MmQ4QUNqWHRxWVhmMlREVHMyTENISHVRYWFlaUVtVkprQ1VPQ3Q1ST0='
key = '88MVdZ9'
decryptor = Encrypt(key)
decrypted_content = decryptor.aes_decrypt(msg)
print(decrypted_content)