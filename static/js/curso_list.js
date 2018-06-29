
$(document).ready(function () {

    $('#cursos').DataTable({
        "language": {
            "lengthMenu": "Mostrando _MENU_ cursos",
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
    nombre = $(this).attr('data-nombre');
    $.ajax({
        type: "POST",
        data: {
            id_curso: id
        },
        url: "/curso/detail/",
        success: function (msg) {
            swal({
                title: "El curso "+nombre+" se encuentra " + msg.estado,
                text: msg.competencias + '\n' + msg.resultados + '\n' + msg.indicadores,
                html: true,
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

