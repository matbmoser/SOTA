
<?php
    # Esto es un ejemplo de como utilizar la clase RSACrypto para utilizar RSA en php.
    
    require "../class.RSACrypto.php";
    $cryptohandler = new RSACrypto();

    echo "<pre><p>Clave Publica = [\n".$cryptohandler->publicKey."]</p><br><br></pre>";
    
    echo "<pre><p>Clave Privada = [\n".$cryptohandler->privateKey."]</p><br></pre>";
    
    $mensaje = "Hola esto es un mensaje";
    
    echo $mensaje;
    
    $cryptText = $cryptohandler->encrypt($mensaje);
    
    echo "<p> <br>Mensaje Encriptado = [".$cryptText."] </p><br>";
    
    $plaintext = $cryptohandler->decrypt($cryptText);
    echo "\n".$plaintext;
        

    ?>
<!DOCTYPE html>
<head>
<meta charset = "utf-8" />
<title>AES JS Crypto Tool</title>
<link rel="stylesheet" type="text/css" href="assets/js/libs/cryptool/main.css"/>
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>

<!-- Import CryptoJS Library-->
<script src="assets/js/libs/cryptool/crypto-js.min.js"></script>

<!-- Import AES Crypto Class-->
<script src="assets/js/libs/cryptool/RSACrypto.js"></script>

</head>
<script>


    // Example to Encrypt and Decrypt using AESCrypto Class, using CryptoJS
    var globalplaintext = "Hola Mundo"
    // Start Handler with initialization vector
    const publicKey = `<?php echo $cryptohandler->publicKey;?>`
    const privateKey = `<?php echo $cryptohandler->privateKey;?>`
    cryptoHandler = new RSACrypto(publicKey, privateKey);


    console.log("PublicKey = [" + publicKey.toString()+"]")
    console.log("PrivateKey = [" + privateKey.toString()+"]")

    console.log(cryptoHandler.publicKey)
    console.log(cryptoHandler.privateKey)
    
    /*
    // Encrypt data and returns the string in base64 encrypted or null if there is any error
    var encrypted = cryptoHandler.encrypt(globalplaintext, globalkey, globalmode)
    
    // General information of encrypted object (Salt, IV, Key and Ciphertext will be null) 
    console.log("Encrypted Text (Base64): "+ encrypted.toString());
    console.log("Encrypted Text (Ciphertext): "+ encrypted.ciphertext);
    console.log("Encrypted Text (salt): "+ encrypted.salt);
    console.log("Encrypted Text (iv): "+ encrypted.iv);
    console.log("Encrypted Text (key): "+ encrypted.iv); 
    */
    // Decrypt data returns the string of the original plaintext or null if the key is not valid
    //var decrypted = cryptoHandler.decrypt(globalciphertext, globalkey, globalmode);

    //console.log("Decrypted Text: "+ decrypted);
    // Convert a hex string to a byte array

</script>
<div id="pagewrapper"> 
    <body>
        <header><nav> </nav></header>
        <div>
            <div id="config" class="hidden">
                <p>Input Plain Text to encrypt or Cipher text to decrypt</p>
                <label for="ciphertext">*Plain text | Cipher text:</label><br>
                <textarea style="width: 1240px; height: 110px;" id="ciphertext" name="ciphertext"></textarea><br><br>
                <label for="secretkey">*Secret Key:</label><br>
                <input type="text" style="width: 1240px; height: 20px;" id="secretkey" name="secretkey"><br><br>
                <label for="iv">IV:</label><br>
                <input type="text" style="width: 1240px; height: 20px;" placeholder="optional" id="iv" name="iv"><br><br>
                <label for="mode">Select Mode:</label>
                <input type="radio" id="ECB" name="mode" value="ECB">
                <label for="ECB">ECB</label>
                <input type="radio" id="CBC" name="mode" value="CBC">
                <label for="CBC">CBC</label><br>
                <button type="submit" id="encrypt">Encrypt</button>  
                <button type="submit" id="decrypt">Decrypt</button>
                <br><br>
                <div id="status"><span class="alert-fail">Waiting</span></div>
            </div>
        </div>
    </body>
</div>
<br><br>
<div style="width: 1240px; height: 180px;">
<textarea style="width: 100%; height: 100%" id="output" disabled></textarea>
<br>
<button style="width: 100%;" type="button" id="copy">Copy</button> 
</div>
<br>
<br>
<script src="assets/js/libs/cryptool/main.js"></script>
