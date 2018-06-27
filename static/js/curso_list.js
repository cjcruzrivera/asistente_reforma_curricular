
$(document).ready(function () {

    $('#cursos').DataTable({
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

$(document).on('click', '#detail', function () {
    id = $(this).attr('data-id');
    $.ajax({
        type: "POST",
        data: {
            id_curso: id
        },
        url: "/curso/detail/",
        success: function (msg) {
            swal({
                title: "El curso se encuentra " + msg.estado,
                text: msg.competencias + '\n' + msg.resultados + '\n' + msg.indicadores,
                type: "info",
                icon: 'info'
            })
        },
        async: false,
        dataType: "json",
        cache: "false",
        error: function (msg) {
            swal({
                title: "Error AJAX",
                text: msg.responseText,
                html: true,
                type: "warning",
                confirmButtonColor: "#d51b23"
            });
            console.log("AJAXerror");
            console.log(msg);

        },
    });
})

$(document).on('click', '#cursos tbody tr td', function() {
    var pagina = "view/";
    var table = $("#cursos").DataTable();
    var colIndex = table.cell(this).index().column;
    
    if (colIndex <= 2) {
       location.href = pagina + table.cell(table.row(this).index(), 0).data();
    }
});
