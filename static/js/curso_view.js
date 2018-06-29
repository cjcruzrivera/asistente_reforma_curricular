$(document).ready(function () {

    $('#cursos').DataTable({
        "language": {
            "lengthMenu": "Mostrando _MENU_ cursos. Para acceder a la información de alguno de ellos, haga click en el nombre",
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

    $('#competencias').DataTable({
        "language": {
            "lengthMenu": "Mostrando _MENU_ competencias",
            "info": "Página _PAGE_ de _PAGES_",
            "search": "Buscar:",
            "paginate": {
                "first": "Primera",
                "previous": "Pág. Anterior",
                "next": "Siguiente",
                "last": "Última"
            }
        },
        "columns": [
            { "width": "1000px" },
            { "width": "180px" },
          ],
          "autoWidth": false
    });

    $('#resultados').DataTable({
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
        },
        "columnDefs": [
            {"width": "500px", "targets": 1},
            {"width": "130px", "targets": 2},
        ],
        "autoWidth": false
    });

    $('#indicadores').DataTable({
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
        },
        "columnDefs": [
            {"width": "500px", "targets": 1},
            {"width": "130px", "targets": 2},
        ],
        "autoWidth": false
    });

})


$(document).on('click','#guardar-pre', function () {
    var curso = $(this).attr('data-course');
    var pos = $('#prerreq_opc').val();
    if(pos == 0){
        swal({
            title: "Seleccione un curso",
            text: '',
            html: true,
            icon:'warning',
            type: "warning",
            confirmButtonColor: "#d51b23"
        });
        return
    }

    $.ajax({
        type: "POST",
        data: {
            id_curso: curso,
            id_pre: pos,
        },
        url: "/curso/prerrequisito/",
        success: function (msg) {
            swal({
                title: "Almacenado con éxito",
                text: "El curso " + msg.nombre + " ha sido almacenado como prerrequisito con éxito",
                icon: "success",
                buttons: false,
                timer: 1000,
            });
            setTimeout(function () { location.reload(true); }, 1000);

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
        location.href = "/curso/" + pagina + table.cell(table.row(this).index(), 0).data()
        // window.location.replace(pagina + table.cell(table.row(this).index(), 0).data());
    }
});