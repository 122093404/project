from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

import base64

# 生成密钥
key = RSA.generate(1024)

exportKey = key.publickey().exportKey() # 公钥
encrypted_key = key.exportKey() # 私钥

# 生成秘钥
with open("private_key.pem", "wb") as f:
    f.write(encrypted_key)
# 生成公钥
with open("public_key.pem", "wb") as f:
    f.write(key.publickey().exportKey())


def rsa_decode3(text):
    "rsa解密"
    # 加载私钥
    with open('project/private_key.pem', 'r') as f:
        private_key = RSA.import_key(f.read().encode())

    global cipher_rsa
    cipher_rsa = PKCS1_v1_5.new(private_key)

    confirmpassword = base64.b64decode(text)
    data = cipher_rsa.decrypt(confirmpassword, None)
    password = bytes.decode(data)
    return password