
var encryptbutton = document.getElementById('encrypt');
var decryptbutton = document.getElementById('decrypt');
var copybutton = document.getElementById('copy');
var output = document.getElementById("output");

encryptbutton.onclick = function(){
  
    var plaintext = document.getElementById('ciphertext').value;
    var key = document.getElementById('secretkey').value;
    var iv = document.getElementById('iv').value;
    var mode = document.querySelector('input[name="mode"]:checked');

    if(iv == ""){
      iv = null;
    }
    
    if(plaintext!="" && key!="" && mode!=null){
      cryptoHandler = new AESCrypto(iv);

      encrypted = cryptoHandler.encrypt(plaintext,key,mode.value)
      
      if(encrypted!=null && encrypted!=""){

        console.log("Cipher text: ["+encrypted+"]");
        setEncrypted();
        writeToScreen(encrypted);

      }else{
        setFail();
        writeToScreen("[ERROR] Was not posible to encrypt: ["+plaintext+"] !");
      }
    }else{
      setFail();
      alert("Plain Text, Key and Mode fields need to be filled!");
    }
}

function setDecrypted(){
  document.getElementById("status").innerHTML = '<span class="alert-decrypted">DECRYPTED</span>';
  output.style.color="#198754";
}
function setEncrypted(){
  document.getElementById("status").innerHTML = '<span class="alert-encrypted">ENCRYPTED</span>';
  output.style.color="#0063de";
}
function setFail(){
  document.getElementById("status").innerHTML = '<span class="alert-danger">FAIL</span>';
  output.style.color="#dc3545";
}

// Copy to clipboard
copybutton.onclick = function(){
  /* Get the text field */
  var copyText = document.getElementById("output");

  /* Select the text field */
  copyText.select();
  copyText.setSelectionRange(0, 99999); /* For mobile devices */

   /* Copy the text inside the text field */
  navigator.clipboard.writeText(copyText.value);

  /* Alert the copied text */
  alert("Output text copied!");
}

decryptbutton.onclick = function(){


    var ciphertext = document.getElementById('ciphertext').value;
    var key = document.getElementById('secretkey').value;
    var iv = document.getElementById('iv').value;
    var mode = document.querySelector('input[name="mode"]:checked');
    
    if(iv == ""){
      iv = null;
    }

    cryptoHandler = new AESCrypto(iv);

    if(ciphertext!="" && key!="" && mode!=null){
      
      
      decrypted = cryptoHandler.decrypt(ciphertext,key,mode.value);
      
      if(decrypted!=null && decrypted!=""){

        console.log("Plain text: ["+decrypted+"]");
        
        setDecrypted();
        writeToScreen(decrypted);
      }
      else{
        setFail();
        writeToScreen("[ERROR] Was not posible to decrypt: ["+ciphertext+"] !");
      }

    }else{
      setFail();
      alert("Cipher Text, Key and Mode fields need to be filled!");
    }
}

function writeToScreen(message) {
  output.value=message;
}
