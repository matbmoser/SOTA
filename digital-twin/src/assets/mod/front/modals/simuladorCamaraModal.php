<!-- Entrada Vehiculo Añadir Matricula-->
<div class="modal fade" id="EntradaVehiculo" tabindex="-1" aria-labelledby="ModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
    <div id="modalContent" class="modal-content">
    <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Cámara Entrada E1</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" onclick="clean('monitorEntrada')" aria-label="Close"></button></div>
    <div class="modal-body">
        <input type="text" class="form-control" id="matriculaEntrada" name="matriculaEntrada" maxlength = "12" placeholder="Matricula" required/>
        <textfield class="w-100 h-100" id="monitorEntrada" disable></textfield>
    </div>
    <div class="modal-footer">
        <button class="btn btn-success" id="addVehiculo" onclick="addVehiculo()" type="submit">Enviar Matricula</button>
    </div>
    </div>
    </div>
</div>

<!-- Salida Vehiculo Borrar Matricula-->
<div class="modal fade" id="SalidaVehiculo" tabindex="-1" aria-labelledby="ModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
    <div id="modalContent" class="modal-content">
    <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Cámara Salida S1</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" onclick="clean('monitorSalida')" aria-label="Close"></button></div>
    <div class="modal-body">
        <input type="text" class="form-control" id="matriculaSalida" name="matriculaSalida" maxlength = "12" placeholder="Matricula" required/>
        <textfield class="w-100 h-100" id="monitorSalida" disable></textfield>
    </div>
    <div class="modal-footer">
        <button class="btn btn-success" id="deleteVehiculo" onclick="deleteVehiculo()" type="submit">Enviar Matricula</button>
    </div>
    </div>
    </div>
</div>