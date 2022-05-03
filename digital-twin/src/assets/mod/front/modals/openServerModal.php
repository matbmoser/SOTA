<div class="modal fade" id="OpenServer" tabindex="-1" aria-labelledby="ModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
        <div id="modalContent" class="modal-content">
        <div class="modal-header d-flex justify-content-between">
          <h5 class="modal-title" id="exampleModalLabel">Admin Servidor</h5>
          <div id="status"><span class="alert-danger">STOPPED</span></div>
          <button type="button" class="btn-close" style="margin: 0!important" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
          <textfield class="w-100 h-100" id="monitor" disable></textfield>
          
          <form class="needs-validation" id="serverData" novalidate>
            <div class="mb-3">
              <label for="ip-pattern" class="col-form-label">IP:</label>
              <input type="text" value="127.0.0.1" class="form-control" id="ip-pattern" disabled required></div>
          <div class="mb-3"><label for="port-pattern" class="col-form-label">PORT:</label>
              <input type="number" id="port-pattern" min="1" max="65535" class="form-control" required>
          </div>
          </form>
          </div>
              <div class="modal-footer"><button id="randomPort" type="button" class="btn btn-secondary">Random Port</button>
              <button id="defaultPort" type="button" class="btn btn-primary">Default Server</button>
              <button type="button" id="open" onclick="openServerByPort()" class="btn btn-success">Open Server</button>
              <button type="button" id="close" onclick="closeServerByPort()" class="hidden btn btn-danger">Close Server</button>
          </div>
        </div>
      </div>
    </div>