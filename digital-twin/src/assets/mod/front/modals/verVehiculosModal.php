<!-- Ver Vehiculos-->
<div class="modal fade" id="VerPlazas" tabindex="-1" aria-labelledby="ModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-fullscreen modal-dialog-scrollable">
    <div id="modalContent" class="modal-content" style="background: white!important;
    color: black!important;">
    <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Ver Plazas</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button></div>
    <div class="modal-body">
        <div class="container-fluid mt-4 d-flex justify-content-center table-responsive">
            <div class="row mt-5">    
            <div class="col-12">
            <h2 class="text-center">
            Plazas Ocupadas<strong style="color:green"></strong>
            </h2>
            </div>
            <table class="table m-2 table-striped table-hovertext-nowrap">
                <thead>
                <tr>
                    <th>idPlaza</th>
                    <th>Matrícula</th>
                    <th>Segmento</th>
                    <th>Tamaño</th>
                    <th>Fecha Entrada</th>
                </tr>
                </thead>
                <tbody id="verPlazasTable">
                
                </tbody>
            </table>
        </div>
        </div>
    </div>
    <div class="modal-footer d-flex justify-content-between">
        <button class="btn btn-warning" id="refreshModal">Refresh</button>
        <button class="btn btn-danger" data-bs-dismiss="modal" type="button">Cerrar</button>
    </div>
    </div>
    </div>
</div>