$(function(){
    button = document.getElementById('dark-mode')
    button.addEventListener('click', function(){
        if(localStorage.getItem("light") === "true"){
                localStorage.setItem("light", "false");
                cambiarModo("dark");
                cambiarBoton(button, "dark");
        } else{
                localStorage.setItem("light", "true");
                cambiarModo("light");
                cambiarBoton(button,"light");
        }
    });
   
   });

   document.addEventListener("readystatechange", function() {
           
        if (document.readyState === "interactive") {
           if(localStorage.getItem("light") === "true"){
                   cambiarModo("light");
                   cambiarBoton(document.getElementById('dark-mode'), "light");
           }
        }
   });
   
   function cambiarModo(modo){

        if(modo === "light"){
                document.documentElement.style.setProperty('--bg-color', '#f8f9fa');
                document.documentElement.style.setProperty('--color', '#212529');

        }else{
                document.documentElement.style.setProperty('--bg-color', '#212529');
                document.documentElement.style.setProperty('--color', '#f8f9fa');
        }
   }

   function cambiarBoton(button, modo){
       var logo = document.getElementById("mylogo");
       if(modo === "dark"){
            button.classList.remove("btn-outline-dark");
            button.classList.add("btn-outline-light");
            logo.classList.remove("img-dark");
            logo.classList.add("img-light");
            button.innerHTML = "<i class='fas fa-sun mr-1'></i> <span>Light Mode</span>";
        }else {
            button.classList.remove("btn-outline-light");
            button.classList.add("btn-outline-dark");
            logo.classList.remove("img-light");
            logo.classList.add("img-dark");
            button.innerHTML = "<i class='fas fa-moon mr-1'></i> <span>Dark Mode</span>";
        }
   }