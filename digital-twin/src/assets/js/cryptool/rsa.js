

class CryptRSA{

    ab2str(buf) {
        return String.fromCharCode.apply(null, new Uint8Array(buf));
      }
    
    addNewLines(str) {
        var finalString = '';
        while(str.length > 0) {
            finalString += str.substring(0, 64) + '\n';
            str = str.substring(64);
        }
    
        return finalString;
    }
    
    str2ab(str) {
        const buf = new ArrayBuffer(str.length);
        const bufView = new Uint8Array(buf);
        for (let i = 0, strLen = str.length; i < strLen; i++) {
          bufView[i] = str.charCodeAt(i);
        }
        return buf;
      }
      
    async exportPublicKey(publicKey) {
        const exported = await window.crypto.subtle.exportKey(
            "spki",
            publicKey
        );
        const exportedAsString = this.ab2str(exported);
        const exportedAsBase64 = window.btoa(exportedAsString);
        const pemExported = `-----BEGIN PUBLIC KEY-----\n${exportedAsBase64}\n-----END PUBLIC KEY-----\n`;
        
        return pemExported;
    }
    async exportPrivateKey(privateKey) {
        const exported = await window.crypto.subtle.exportKey(
            "spki",
            privateKey
        );
        const exportedAsString = this.ab2str(exported);
        const exportedAsBase64 = window.btoa(exportedAsString);
        const pemExported = `-----BEGIN RSA PRIVATE KEY-----\n${exportedAsBase64}\n-----END RSA PRIVATE KEY-----\n`;
        
        return pemExported;
    }
          
    async generateKey(){
        return await crypto.subtle.generateKey(
            {
              name: "RSA-OAEP",
              modulusLength: 2048,
              publicExponent: new Uint8Array([1, 0, 1]),
              hash: "SHA-256",
            },
            true,
            ["encrypt", "decrypt"]
          ).then((keyPair) => { 
            return exportPublicKey(keyPair.publicKey), exportPrivateKey(keyPair.privateKey)
          });
    }
      
    async encrypt(message, publicKey) {
        let enc = new TextEncoder();
        message = enc.encode(message);
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