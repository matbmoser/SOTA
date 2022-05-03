<div class="modal fade" id="ConnectCamera" tabindex="-1" aria-labelledby="ModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
        <div id="modalContent" class="modal-content">
        <div class="modal-header d-flex justify-content-between">
          <h5 class="modal-title" id="exampleModalLabel">Admin Camera</h5>
          <div id="statusCamera"><span class="alert-danger">DISCONNECTED</span></div>
          <button type="button" class="btn-close" style="margin: 0!important" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
          <textfield class="w-100 h-100" id="cameraMonitor" disable></textfield>
          
          <form class="needs-validation" id="serverData" novalidate>
            <h2>Connected to Running Server:</h2>
            <div class="mb-3">
              <label for="ip-pattern" class="col-form-label">Server IP:</label>
              <input type="text" value="127.0.0.1" class="form-control" id="ip-pattern" disabled required></div>
              <div class="mb-3"><label for="cameraServerPort" class="col-form-label">Server PORT:</label>
              <input type="number" id="cameraServerPort" class="form-control" disabled required>
          </div>
          </form>
          </div>
              <button type="button" id="openCamera" onclick="connectToServer()" class="btn btn-success">Connect Camera</button>
              <button type="button" id="closeCamera" onclick="disconnectFromServer()" class="hidden btn btn-danger">Disconnect Camera</button>
          </div>
        </div>
      </div>
    </div>