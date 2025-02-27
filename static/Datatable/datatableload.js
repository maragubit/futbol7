$(document).ready( function () {
    $('#tabla_jugadores').DataTable(
      {
      "scrollX": true,
      "aaSorting": [],
      "pageLength": 50,
      "order": [[ 1, "desc" ], [ 8, "desc" ],[ 6, "desc" ]],
      
      "language": {
                  "lengthMenu": "Mostrar _MENU_ jugadores por página",
                  "zeroRecords": "No se ha encontrado nada - disculpe",
                  "info": "Mostrando página _PAGE_ de _PAGES_",
                  "infoEmpty": "No hay datos disponibles",
                  "infoFiltered": "(filtrado de _MAX_ jugadores disponibles)",
                  "search": "Buscar:",
                  "paginate": {
                        "previous": "anterior",
                        "next": "siguiente"
                      }
              }}

                             );


    $('#partidos').DataTable(
    {
    "scrollX": true,
    "aaSorting": [],
    "pageLength": 50,
    
    "language": {
                "lengthMenu": "Mostrar _MENU_ partidos por página",
                "zeroRecords": "No se ha encontrado nada - disculpe",
                "info": "Mostrando página _PAGE_ de _PAGES_",
                "infoEmpty": "No hay datos disponibles",
                "infoFiltered": "(filtrado de _MAX_ partidos disponibles)",
                "search": "Buscar:",
                "paginate": {
                      "previous": "anterior",
                      "next": "siguiente"
                    }
            }}

                            );
} );

