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

    $('#curso').DataTable({
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


$(document).on('click','#guardar', function () {
    var curso = $(this).attr('data-course');
    var pos = $('#prerreq').val();
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
                timer: 1500,
            });
            setTimeout(function () { location.reload(true); }, 1500);

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