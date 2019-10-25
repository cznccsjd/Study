#coding:utf-8
'''
学习pycryptodome
参考资料:https://blog.csdn.net/weixin_30347335/article/details/99123821
对称加密算法
4.1 对称加密算法说明
别名：对称加密算法，又称密钥加密算法、单密钥算法、共享密钥算法，英文名Symmetric Encryption Algorithms。

原理：对称加密算法最关键的就是SP变换，S变换通过代替操作实现混乱（即消除统计信息），P变换通过换位操作实现扩散（即雪崩效应）；加解密是使用同一个密钥的逆操作过程。

用途：对称加密可以还原内容，且代替和换位操作运算量不大，适用于大量内容的加解密。对称加密算法的缺点是加解密双方密钥分发困难。

其他：对称加密算法有ECB、CBC、CFB、OFB、CTR等等多种模式，各种模式的加密是有些区别的，比如ECB不需要IV、CBC等则需要IV、EAX则需要nonce和tag等等，所以实现不同模式时写法会有差别需要具体研究，不能完全照搬下边的例子。
'''

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

# 要加密的内容
data = b"123456"
# 随机生成16字节（即128位）的加密密钥
key = get_random_bytes(16)
# 实例化加密套件，使用CBC模式
clipher = AES.new(key, AES.MODE_CBC)
# 对内容进行加密，pad函数用于分组和填充
encrypted_data = clipher.encrypt(pad(data, AES.block_size))

# 将加密内容写入文件
file_out = open("encrypted.bin", "wb")
# 在文件中依次写入key、iv和密文encrypted_data
[file_out.write(x) for x in (key, clipher.iv, encrypted_data)]

