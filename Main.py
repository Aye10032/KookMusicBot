import zlib

from flask import Flask, request, jsonify
from Crypto.Cipher import AES
import base64
import json

app = Flask(__name__)


# class Encrypt:
#     def __init__(self, key, bs=32):
#         pad = lambda s: s + (bs - len(s)) * "\0"
#         key = pad(key)
#         self.key = key.encode('utf-8')
#
#     def aes_decrypt(self, content):
#         str = base64.b64decode(content)
#         iv = str[0:16]
#         cipher = AES.new(self.key, AES.MODE_CBC, iv)
#         return cipher.decrypt(base64.b64decode(str[16:])).decode('utf-8')

def aes_decrypt(encrypt_key, cipher_data_base64):
    # Base64解码密文得到二进制数据
    cipher_data = base64.b64decode(cipher_data_base64)

    # 取得前16位作为初始化向量 iv，剩余的作为新的密文
    iv = cipher_data[:16]
    cipher_data = cipher_data[16:]

    # Base64解码新的密文，得到待解密数据
    msg = base64.b64decode(cipher_data)

    # encryptKey 后补充 \0 直到长度为32位，得到32字节的密钥 key
    key = (encrypt_key + (16 - len(encrypt_key) % 16) * '\0').encode('utf-8')

    # 使用Python内置的PyCryptodome库进行解密
    decryptor = AES.new(key, AES.MODE_CBC, iv)
    event_json = decryptor.decrypt(msg).decode('utf-8')

    return event_json


@app.route('/', methods=['POST'])
def process_json():
    compressed_data = request.data
    uncompressed_data = zlib.decompress(compressed_data)
    parsed_message = json.loads(uncompressed_data)  # 解析JSON字符串
    encrypted_content = parsed_message['encrypt']  # 提取密文

    key = "88MVdZ9"
    decrypted_content = aes_decrypt(key, encrypted_content)

    print('[' + decrypted_content + ']')

    data = json.loads(str(decrypted_content))
    print(data)
    challenge = data['d']['challenge']
    return jsonify({'challenge': challenge})


if __name__ == '__main__':
    app.run(port=9500, debug=True)
