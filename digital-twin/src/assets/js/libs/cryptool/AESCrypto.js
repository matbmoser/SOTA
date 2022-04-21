/** © CGI | All Rights Reserved | 2022
 *  Author: Mathias Brunkow Moser
 *  AES Class Crypto Tool 
 *  Mandatory Library: https://cryptojs.gitbook.io/docs/#ciphers 
 * **/
  


class AESCrypto{
  /*Class to Encrypt and Decrypt AES using two methods (ECB and CBC), include iv if necesary.*/

      constructor(iv=null){
        // IV is empty by default
        this.iv = { words: [ 0, 0, 0, 0 ], sigBytes: 16 };
        
        // If IV is introduced 
        if(iv != null && iv != ""){

          this.iv = CryptoJS.enc.Utf8.parse(iv);

        }
      }
      
      // Pass from hex to ascci
      hex_to_ascii(str1)
      {
          var hex  = str1.toString();
          var str = '';
          for (var n = 0; n < hex.length; n += 2) {
              str += String.fromCharCode(parseInt(hex.substr(n, 2), 16));
          }
          return str;
      }
      // Encrypt a plaintext with AES (base64)
      encrypt(plaintext, key, mode="ECB"){
        try{
          let encrypted = null;
          switch (mode){

            case "ECB":
              encrypted = CryptoJS.AES.encrypt(plaintext, CryptoJS.enc.Utf8.parse(key), { iv: this.iv, mode: CryptoJS.mode.ECB, padding: CryptoJS.pad.Pkcs7 }).toString();
              break;

            case "CBC":
              encrypted = CryptoJS.AES.encrypt(plaintext, CryptoJS.enc.Utf8.parse(key), { iv: this.iv, mode: CryptoJS.mode.CBC, padding: CryptoJS.pad.Pkcs7 }).toString();
              break;

            default:
              encrypted = null;

          }

          return encrypted;
        }
        catch(e){
          console.log("[CRITICAL] AESCrypto.encrypt(): "+ e.toString());
          return null;
        }
      }
      
      // Decrypt a ciphertext with AES (base64)
      decrypt(ciphertext, key, mode="ECB"){
        try{
          let decrypted = null;
          switch (mode){

            case "ECB":
              decrypted = this.hex_to_ascii(CryptoJS.AES.decrypt(ciphertext, CryptoJS.enc.Utf8.parse(key), { iv: this.iv, mode: CryptoJS.mode.ECB, padding: CryptoJS.pad.Pkcs7 }).toString());
              break;

            case "CBC":
              decrypted = this.hex_to_ascii(CryptoJS.AES.decrypt(ciphertext, CryptoJS.enc.Utf8.parse(key), { iv: this.iv, mode: CryptoJS.mode.CBC, padding: CryptoJS.pad.Pkcs7 }).toString());
              break;

            default:
              decrypted = null;
          }

          return decrypted;
        }
        catch(e){

          console.log("[CRITICAL] AESCrypto.decrypt(): "+ e.toString());
          return null;

        }
      }
  }