from encryptool import encryptool
encryptool.generateKeys()
publicKey, privateKey = encryptool.loadKeys()
message = input('Write your message here:')

ciphertext = encryptool.encrypt(message, publicKey)
signature = encryptool.sign(message, privateKey)
text = encryptool.decrypt(ciphertext, privateKey)

print(f'Cipher text: {ciphertext}')
print(f'Signature: {signature}')
if text:
    print(f'Message text: {text}')
else:
    print(f'Unable to decrypt the message.')

if encryptool.verify(text, signature, publicKey):
    print("Successfully verified signature")
else:
    print('The message signature could not be verified')
