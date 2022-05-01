<?php
return array(

"barreras" =>

'<div class="modal-header">
<h5 class="modal-title" id="exampleModalLabel">Manejar Barrera</h5>
<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button></div>
<div class="modal-body">
    <textfield class="w-100 h-100" id="monitor" disable></textfield>
</div>
<div class="modal-footer">
<div class="form-check">
  <input class="form-check-input" type="radio" name="flexRadioDefault" id="barreraEntrada" checked>
  <label class="form-check-label" for="flexRadioDefault1">
    Entrada
  </label>
</div>
<div class="form-check">
  <input class="form-check-input" type="radio" name="flexRadioDefault" id="barreraSalida">
  <label class="form-check-label" for="flexRadioDefault2">
    Salida
  </label>
</div>
<button class="btn btn-danger" id="cerrarBarrera" type="submit" name="button">Cerrar Barrera</button>
<button class="btn btn-success"id="abrirBarrera" type="submit" name="button">Abrir Barrera</button>
</div></div>'


);