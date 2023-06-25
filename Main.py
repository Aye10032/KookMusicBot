import zlib

from flask import Flask, request
from Crypto.Cipher import AES
import base64
import json

app = Flask(__name__)


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


@app.route('/', methods=['POST'])
def process_json():
    compressed_data = request.data
    uncompressed_data = zlib.decompress(compressed_data)

    # key = "88MVdZ9"
    # decryptor = Encrypt(key)
    # decrypted_content = decryptor.aes_decrypt(uncompressed_data)
    print(json.dumps(uncompressed_data, indent=4))
    return 'OK'


if __name__ == '__main__':
    app.run(port=9500, debug=True)
