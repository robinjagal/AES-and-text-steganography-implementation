from Crypto import Random
from Crypto.Hash import SHA256
from Crypto.Cipher import AES


class aes:
    def __init__(self, key):
        self.key = key

    def pad(self, s):
        return s + "\0" * (AES.block_size - len(s) % AES.block_size)

    def keytohash(self,key):
        key = self.pad(self.key)
        h_obj = SHA256.new(key.encode('utf-8'))
        hkey = h_obj.digest()
        return hkey

    def encrypt(self, message):
        hkey = self.keytohash(self.key)
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(hkey, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message.encode('utf-8'))

    def decrypt(self, ciphertext):
        iv = ciphertext[:AES.block_size]
        hkey = self.keytohash(self.key)
        cipher = AES.new(hkey, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0").decode('utf-8')

