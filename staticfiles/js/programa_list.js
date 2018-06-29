
$(document).ready(function () {

    $('#programas').DataTable({
        "language": {
            "lengthMenu": "Mostrando _MENU_ registros",
            "info": "Página _PAGE_ de _PAGES_",
            "search": "Buscar:",
            "paginate": {
                "first": "Primera",
                "previous": "Pág. Anterior",
                "next": "Siguiente",
                "last": "Última"
            }
        }
    });
})

$(document).on('click', '#programas tbody tr td', function() {
    var pagina = "view/";
    var table = $("#programas").DataTable();
    var colIndex = table.cell(this).index().column;
    
    if (colIndex <= 5) {
       location.href = pagina + table.cell(table.row(this).index(), 0).data();
    }
});


