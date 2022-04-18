import rsa
from operators.op import op


class encryptool:
    @staticmethod
    def generateKeys(bytes=1024, uid="default", store=True, saveMode='PEM'):
        (publicKey, privateKey) = rsa.newkeys(bytes)
        op.makeDir('keys/'+str(uid))
        if(store):
            with open('keys/'+str(uid)+'/publicKey.pem', '+ab') as p:
                p.write(publicKey.save_pkcs1(saveMode))
            with open('keys/'+str(uid)+'/privateKey.pem', '+ab') as p:
                p.write(privateKey.save_pkcs1(saveMode))
        return publicKey, privateKey

    @staticmethod
    def getPkcs1Keys(publicKey, privateKey,  saveMode='PEM'):
        return publicKey.save_pkcs1(saveMode), privateKey.save_pkcs1(saveMode)

    @staticmethod
    def loadKeys(uid="default"):
        with open('keys/'+str(uid)+'/publicKey.pem', 'rb') as p:
            publicKey = rsa.PublicKey.load_pkcs1(p.read())
        with open('keys/'+str(uid)+'/privateKey.pem', 'rb') as p:
            privateKey = rsa.PrivateKey.load_pkcs1(p.read())
        return privateKey, publicKey

    @staticmethod
    def encrypt(message, key):
        return rsa.encrypt(message.encode('ascii'), key)

    @staticmethod
    def decrypt(ciphertext, key):
        try:
            return rsa.decrypt(ciphertext, key).decode('ascii')
        except:
            return False

    @staticmethod
    def sign(message, key):
        return rsa.sign(message.encode('ascii'), key, 'SHA-256')

    @staticmethod
    def verify(message, signature, key):
        try:
            return rsa.verify(message.encode('ascii'), signature, key,) == 'SHA-256'
        except:
            return False
