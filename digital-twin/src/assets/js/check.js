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
            let user = document.getElementById("inputEmail").value.toLowerCase();
            let pass = document.getElementById("inputPassword").value;
            if (user == "" || pass == "" || user==null || pass==null){
                event.preventDefault();
                event.stopPropagation();
                form.classList.add('was-validated'); //Y cambia la classe del formulario, para validado
                return true 
            }

            let remember = document.getElementById("remember");
            if(remember.checked){
                setCookie("__chgn", CryptoJS.AES.encrypt(user, getSession()).toString(), 0.2);
                //setCookie("__efbr", CryptoJS.AES.encrypt(pass, getSession()).toString(),0.2);
            }else{
                setCookie("__chgn", "", 0);
                //setCookie("__efbr", "", 0);
            }
            let loading = document.getElementById("loading");
            const params = await encrypt(user,pass);
            let url = '../assets/mod/login.php';
            http.onreadystatechange = function() {
                if(http.readyState === 4) {
                    if(http.status === 200) { //LISTO
                        let sucess = "0";
                        let username = "none";
                        let token = "null"
                        loading.style.display = "none!important";
                        try{
                            let obj = JSON.parse(http.responseText);
                            sucess = obj.success;
                            token = obj.token;
                            username = obj.username;
                            alert(http.responseText)
                        } catch(e){
                            sucess = 0;
                        }
                        if(sucess == 1){
                            setCookie("__LOGIN__", "TRUE",0.2,"/");
                            window.location.href = "../index.php?username="+ username + "&token=" + token;
                        }else if(sucess == 0){
                            window.location.search = "?result=0";
                        }
                    } else { //DENEGADO
                        alert('Error Code: ' +  http.status);
                        alert('Error Message: ' + http.statusText);
                    }
                }else{
                    loading.style.display = "block!important";
                }
            }
            http.open('POST',url,false);
            http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            http.send(params);

        }

    }, false);
});

async function encrypt(user, pass){
    const cryptpass = await sha512(pass);
    const seed = user+cryptpass;
    const token = await sha256(seed);
    const UUID = getCookie("UUID");
    return 'email='+user+'&pass='+ cryptpass + '&token=' + token + "&uuid=" + UUID;
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