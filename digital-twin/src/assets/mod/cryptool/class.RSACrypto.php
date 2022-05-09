<?php
<<<<<<< HEAD
## Clase creada para encriptar y desencriptar en PHP, utilizando criptografia asimétrica.
=======

>>>>>>> 6c5d8de44c44d84f729a1e49a2816e63bc70c168
class RSACrypto{
    function __construct(){
        $config = array(
            "digest_alg" => "sha256",
            "private_key_bits" => 2048,
            "private_key_type" => OPENSSL_KEYTYPE_RSA,
        );
        $this->keygen = $this->generateKeys($config);
        $this->padding = OPENSSL_PKCS1_OAEP_PADDING;
        $this->privateKey = $this->generatePrivateKey($this->keygen);
        $this->publicKey = $this->generatePublicKey($this->keygen);
    }
    function generateKeys($config){
<<<<<<< HEAD
        // Generamos las claves
=======
        // Create the private and public key
>>>>>>> 6c5d8de44c44d84f729a1e49a2816e63bc70c168
        return openssl_pkey_new($config);
    }

    function generatePrivateKey($keygen){
<<<<<<< HEAD
        // Extraemos la clave privada
=======
        // Extract the private key from $res to $privKey
>>>>>>> 6c5d8de44c44d84f729a1e49a2816e63bc70c168
        openssl_pkey_export($keygen, $privKey);

        return $privKey;
    }

    function generatePublicKey($keygen){
<<<<<<< HEAD
        // Extraemos la clave publica
=======
        // Extract the public key from $res to $pubKey
>>>>>>> 6c5d8de44c44d84f729a1e49a2816e63bc70c168
        $pubKey = openssl_pkey_get_details($keygen);
        $pubKey = $pubKey["key"];

        return $pubKey;
    }

    function encrypt($data){
<<<<<<< HEAD
        // Encriptamos el mensaje
=======
        // Encrypt the data to $encrypted using the public key
>>>>>>> 6c5d8de44c44d84f729a1e49a2816e63bc70c168
        openssl_public_encrypt($data, $encrypted, $this->publicKey, $this->padding);
        return $encrypted;
    }

    function decrypt($encrypted){
<<<<<<< HEAD
        // Desencriptamos el mensaje
=======
>>>>>>> 6c5d8de44c44d84f729a1e49a2816e63bc70c168
        openssl_private_decrypt($encrypted, $decrypted, $this->privateKey, $this->padding);
        return $decrypted;
    }
}

