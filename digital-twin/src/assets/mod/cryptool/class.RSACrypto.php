<?php
## Clase creada para encriptar y desencriptar en PHP, utilizando criptografia asimétrica.
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
        // Generamos las claves
        return openssl_pkey_new($config);
    }

    function generatePrivateKey($keygen){
        // Extraemos la clave privada
        openssl_pkey_export($keygen, $privKey);

        return $privKey;
    }

    function generatePublicKey($keygen){
        // Extraemos la clave publica
        $pubKey = openssl_pkey_get_details($keygen);
        $pubKey = $pubKey["key"];

        return $pubKey;
    }

    function encrypt($data){
        // Encriptamos el mensaje
        openssl_public_encrypt($data, $encrypted, $this->publicKey, $this->padding);
        return $encrypted;
    }

    function decrypt($encrypted){
        // Desencriptamos el mensaje
        openssl_private_decrypt($encrypted, $decrypted, $this->privateKey, $this->padding);
        return $decrypted;
    }
}

