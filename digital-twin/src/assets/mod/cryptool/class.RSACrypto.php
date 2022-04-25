<?php

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
        // Create the private and public key
        return openssl_pkey_new($config);
    }

    function generatePrivateKey($keygen){
        // Extract the private key from $res to $privKey
        openssl_pkey_export($keygen, $privKey);

        return $privKey;
    }

    function generatePublicKey($keygen){
        // Extract the public key from $res to $pubKey
        $pubKey = openssl_pkey_get_details($keygen);
        $pubKey = $pubKey["key"];

        return $pubKey;
    }

    function encrypt($data){
        // Encrypt the data to $encrypted using the public key
        openssl_public_encrypt($data, $encrypted, $this->publicKey, $this->padding);
        return $encrypted;
    }

    function decrypt($encrypted){
        openssl_private_decrypt($encrypted, $decrypted, $this->privateKey, $this->padding);
        return $decrypted;
    }
}

