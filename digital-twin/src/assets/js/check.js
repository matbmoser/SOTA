/*
Created by: Mathias Moser
Hype Technology Spain
©2019-2021
*/

$(function() {
    let http = new XMLHttpRequest();
    let form = document.getElementById("loginform");
    form.addEventListener('submit', async function(event) {
        if (form.checkValidity() === false) {
            event.preventDefault();
            event.stopPropagation();
            form.classList.add('was-validated'); //Y cambia la classe del formulario, para validado
        } //Si son validos el bucle se detiene
        else{
            let user = document.getElementById("inputEmail").value;
            let pass = document.getElementById("inputPassword").value;
            let remember = document.getElementById("remember");
            if(remember.checked){
                setCookie("__chgn", CryptoJS.AES.encrypt(user, getSession()).toString(), 0.2);
                setCookie("__efbr", CryptoJS.AES.encrypt(pass, getSession()).toString(),0.2);
            }else{
                setCookie("__chgn", "", 0);
                setCookie("__efbr", "", 0);
            }
            let demo = document.getElementById("demo");
            const params = await encrypt(user,pass);
            let url = '../assets/mod/login.php';
            http.onreadystatechange = function() {
                if(http.readyState === 4) {
                    if(http.status === 200) { //LISTO
                        let sucess = "0";
                        let userid = "none";
                        let token = "null"
                        demo.style.display = "none!important";
                        try{
                            let obj = JSON.parse(http.responseText);
                            sucess = obj.success;
                            token = obj.token;
                            userid = obj.userid;
                        } catch(e){
                            sucess = "0";
                        }
                        if(sucess === '1'){
                            window.location.search = "?result=1";
                            window.location.href = "../index.php?id="+ userid + "&token=" + token;
                        }else if(sucess === '0'){
                            window.location.search = "?result=0";
                        }
                    } else { //DENEGADO
                        alert('Error Code: ' +  http.status);
                        alert('Error Message: ' + http.statusText);
                    }
                }else{
                    demo.style.display = "block!important";
                }
            }
            http.open('POST',url,false);
            http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            http.send(params);

        }

    }, false);
});

async function encrypt(user, pass){
    const cryptpass = await sha256(pass);
    const seed = user+cryptpass;
    const token = await sha256(seed);
    return 'names='+user+'&numbers='+ cryptpass + '&token=' + token;
}


function getSession() {
    cname = "PHPSESSID";
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1);
        if (c.indexOf(name) == 0) return c.substring(name.length,c.length);
    }
    return "";
}
async function sha256(message) {

    // encode as UTF-8
    const msgBuffer = new TextEncoder('utf-8').encode(message);

    // hash the message
    const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);

    // convert ArrayBuffer to Array
    const hashArray = Array.from(new Uint8Array(hashBuffer));

    // convert bytes to hex string
    const hashHex = hashArray.map(b => ('00' + b.toString(16)).slice(-2)).join('');
    return hashHex;
}

function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}