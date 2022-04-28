<?php
return array(

"openServer" =>

'<div class="modal-header">
<h5 class="modal-title" id="exampleModalLabel">Abrir Servidor</h5>
<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
</div>
<div class="modal-body"><form class="needs-validation" novalidate><div class="mb-3">
    <label for="ip-pattern" class="col-form-label">IP:</label>
    <input type="text" value="127.0.0.1" class="form-control" id="ip-pattern" disabled required></div>
<div class="mb-3"><label for="port-pattern" class="col-form-label">PORT:</label>
    <input type="number" id="port-pattern" min="1" max="65535" class="form-control" required>
</div>
</form>
</div>
    <div class="modal-footer"><button id="randomPort" type="button" class="btn btn-secondary">Random Port</button>
    <button id="defaultPort" type="button" class="btn btn-primary">Default Server</button>
    <button type="button" id="open" class="btn btn-success">Open</button>
</div>',

"inCoche" =>

'<div class="modal-header">
<h5 class="modal-title" id="exampleModalLabel">Añadir Coche</h5>
<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
</button></div><div class="modal-body">
<form>
<div class="mb-3">
<label for="recipient-name" class="col-form-label">Matricula:</label>
<input type="text" class="form-control" id="recipient-name">
</div><div class="mb-3">
<label for="message-text" class="col-form-label">Message:</label>
<textarea class="form-control" id="message-text"></textarea>
</div></form></div>
<div class="modal-footer">
<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
<button type="button" class="btn btn-primary">Send message</button></div>',

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