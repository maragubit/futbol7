$(document).ready( function () {
    $('#partidos').DataTable(
    {
    "scrollX": true,
    "aaSorting": [],
    "pageLength": 50,
    
    "language": {
                "lengthMenu": "Mostrar _MENU_ filas por página",
                "zeroRecords": "No se ha encontrado nada - disculpe",
                "info": "Mostrando página _PAGE_ de _PAGES_",
                "infoEmpty": "No hay datos disponibles",
                "infoFiltered": "(filtrado de _MAX_ filas disponibles)",
                "search": "Buscar:",
                "paginate": {
                      "previous": "anterior",
                      "next": "siguiente"
                    }
            }}

                            );
} );

