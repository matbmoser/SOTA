function adminBarreras(){
  localStorage.setItem("barreraSelected", "ENTRADA");
  var barreraEntrada = document.getElementById("barreraEntrada");
  var barreraSalida = document.getElementById("barreraSalida");
  barreraEntrada.addEventListener('change', function() {
    if (this.checked) {
      localStorage.setItem("barreraSelected", "ENTRADA");
    }
  });
  barreraSalida.addEventListener('change', function() {
    if (this.checked) {
      localStorage.setItem("barreraSelected", "SALIDA");
    }
  });

  let cerrar = document.getElementById("cerrarBarrera");
  let abrir = document.getElementById("abrirBarrera");
  let monitor = document.getElementById("monitor");
  localStorage.setItem("barrera", "CERRADA");
  var selected = localStorage.getItem("barreraSelected");
  monitor.innerHTML  =`<span style="color:red">Barrera de la `+selected+` CERRADA</span>`
  abrir.addEventListener('click', function() {
    if(localStorage.getItem("barrera") == "CERRADA"){
      localStorage.setItem("barrera", "ABIERTA");
      selected = localStorage.getItem("barreraSelected");
      let timeleft = 10;
      monitor.innerHTML =`
      <span style="color:green">Barrera de la `+selected+` ABIERTA</span> Cerrando en 10s:
      <progress value="0" max="10" id="progressBar"></progress>
      `;
      const downloadTimer = setInterval(function(){
        if(timeleft <= 0){
          clearInterval(downloadTimer);
          document.getElementById("progressBar").value = 0;
        }
        document.getElementById("progressBar").value = 10 - timeleft;
        timeleft -= 1;
      }, 435);
      setTimeout(function(){
        let monitor = document.getElementById("monitor");
        clearInterval(downloadTimer);
        if(localStorage.getItem("barrera") == "ABIERTA"){
          selected = localStorage.getItem("barreraSelected");
          localStorage.setItem("barrera", "CERRADA");
          monitor.innerHTML  =`<span style="color:red">Barrera de la `+selected+` CERRADA</span>`
        }
      }, 5000);

    }else{
      monitor.appendChild = `<span style="color:green">La barrera ya esta abierta</span>`;
    }
  });
  cerrar.addEventListener('click', function() {
    if(localStorage.getItem("barrera") == "CERRADA"){
      selected = localStorage.getItem("barreraSelected");
      monitor.innerHTML = `<span style="color:green">La barrera de la `+selected+` ya esta cerrada!</span>`;
      setTimeout(function(){
        selected = localStorage.getItem("barreraSelected");
        monitor.innerHTML  =`<span style="color:red">Barrera de la `+selected+` CERRADA</span>`
      }, 2000);
    }else{
      selected = localStorage.getItem("barreraSelected");
      monitor.innerHTML = `<span style="color:green">Cerrando barrera de la `+selected+`...</span>`;
      setTimeout(function(){
        clearInterval(downloadTimer);
        selected = localStorage.getItem("barreraSelected");
        localStorage.setItem("barrera", "CERRADA");
        monitor.innerHTML  =`<span style="color:red">Barrera de la `+selected+` CERRADA</span>`
      }, 2000);
    }
  });
}