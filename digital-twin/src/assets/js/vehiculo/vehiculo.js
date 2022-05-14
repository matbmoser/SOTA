function addVehiculo() {
    let cameraid = localStorage.getItem("cameraid");
    if (cameraid != null && cameraid != undefined && cameraid != "") {
        var matriculaEntrada = document.getElementById("matriculaEntrada").value;
        if (matriculaEntrada == "" || matriculaEntrada == null) {
            overwrite("monitorEntrada", "<span style='color:red'>[ERROR] ¡La matricula no puede estar vacía!</span>");
            return;
        }
        camera.sendPlateToServer(matriculaEntrada, "IN");
        overwrite("monitorEntrada", "<span style='color:#0d6efd'>[INFO] ¡Plate [" + matriculaEntrada.toString() + "] sent!<span>");
    } else {
        overwrite("monitorEntrada", "<span style='color:red'>[ERROR] ¡Ninguna cámara conectada!</span>");
    }
}
function deleteVehiculo() {
    let cameraid = localStorage.getItem("cameraid");
    if (cameraid != null && cameraid != undefined && cameraid != "") {
        var matriculaSalida = document.getElementById("matriculaSalida").value;
        if (matriculaSalida == "" || matriculaSalida == null) {
            overwrite("monitorSalida", "<span style='color:red'>[ERROR] ¡La matricula no puede estar vacía!</span>");
            return;
        }
        camera.sendPlateToServer(matriculaSalida, "OUT");
        overwrite("monitorSalida", "<span style='color:#0d6efd'>[INFO] ¡Plate [" + matriculaSalida.toString() + "] sent!<span>");
    } else {
        overwrite("monitorSalida", "<span style='color:red'>[ERROR] ¡Ninguna cámara conectada!</span>");
    }
}
