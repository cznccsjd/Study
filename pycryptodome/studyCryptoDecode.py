#coding:utf-8

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# 从前边文件中读取加密的内容(pycryptodome/studyCryptoEncode.py: line:21)
file_in = open("encrypted.bin", "rb")
# 依次读取key、iv和密文encrypted_data, 16等是各变量长度，最后的-1则表示读取到文件末尾
key, iv, encrypted_data = [file_in.read(x) for x in (16, AES.block_size, -1)]

# 实例化加密套件
cipher = AES.new(key, AES.MODE_CBC, iv)
# 解密，如无意外data值为最先加密的b"123456"
data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
print(data)