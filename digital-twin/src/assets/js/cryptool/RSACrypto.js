

class RSACrypto{
    constructor(publicKey, privateKey){
      this.strPubKey = publicKey
      this.strPrivKey = privateKey
      this.publicKey = this.importPublicKey(publicKey);
      this.privateKey = this.importPrivateKey(privateKey);
    }
    async str2ab(str) {
      const buf = new ArrayBuffer(str.length);
      const bufView = new Uint8Array(buf);
      for (let i = 0, strLen = str.length; i < strLen; i++) {
        bufView[i] = str.charCodeAt(i);
      }
      return buf;
    }
    async ab2str(buf) {
        return String.fromCharCode.apply(null, new Uint8Array(buf));
    }

    async importPublicKey(pem) {
      // fetch the part of the PEM string between header and footer
      const pemHeader = "-----BEGIN PUBLIC KEY-----\n";
      const pemFooter = "\n-----END PUBLIC KEY-----\n";
      const pemContents = pem.substring(pemHeader.length, pem.length - pemFooter.length);
      console.log(pemContents)
      // base64 decode the string to get the binary data
      const binaryDerString = window.atob(pemContents);
      // convert from a binary string to an ArrayBuffer
      const binaryDer = this.str2ab(binaryDerString);
  
      return crypto.subtle.importKey(
        "spki",
        binaryDer,
        {
          name: "RSA-OAEP",
          hash: "SHA-256"
        },
        true,
        ["encrypt"]
      )
    }

    async importPrivateKey(pem) {
      // fetch the part of the PEM string between header and footer
      const pemHeader = "-----BEGIN PRIVATE KEY-----\n";
      const pemFooter = "\n-----END PRIVATE KEY-----\n";
      const pemContents = pem.substring(pemHeader.length, pem.length - pemFooter.length);
      // base64 decode the string to get the binary data
      const binaryDerString = atob(pemContents);
      // convert from a binary string to an ArrayBuffer
      const binaryDer = this.str2ab(binaryDerString);
  
      return window.crypto.subtle.importKey(
        "spki",
        binaryDer,
        {
          name: "RSA-OAEP",
          hash: "SHA-256"
        },
        true,
        ["encrypt"]
      )
    }
    
    encodeText(text){
      let enc = new TextEncoder();
      return enc.encode(text)
    }

    async encrypt(message, publicKey) {
        message = encodeText(message);
        return await crypto.subtle.encrypt(
            {
            name: "RSA-OAEP"
            },
            publicKey,
            message
        );
    }
    
    async decryption(ciphertext, privateKey) {
        return window.crypto.subtle.decrypt(
            {
              name: "RSA-OAEP"
            },
            privateKey,
            ciphertext
          );
    }


}