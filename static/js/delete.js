$(document).on('click', '#delete', function () {
    var mensaje = "";
    var tipo = $(this).attr('data-tipo');

    switch (tipo) {
        case 'escuela':
            var escuela = "";
            escuela = $(this).attr('data-nombre');
            mensaje = 'la escuela ' + escuela;
            break;
        case 'programa':
            var programa = "";
            programa = $(this).attr('data-nombre');
            mensaje = 'el programa ' + programa;
            break;
        case 'usuario':
            var usuario = "";
            usuario = $(this).attr('data-nombre');
            mensaje = 'el usuario ' + usuario;
            break;
        default:
            break;
    }


    id = $(this).attr('data-id');
    swal({
        title: "Advertencia",
        text: "¿Seguro que desea eliminar " + mensaje + "?",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    })
        .then((willDelete) => {
            if (willDelete) {
                borrado = deleteElement(id, tipo);
                if (borrado) {
                    setTimeout(function () { location.reload(true); }, 1500);
                }
            }
        });
});

function deleteElement(id, tipo) {
    switch (tipo) {
        case 'escuela':
            return deleteEscuela(id);
            break;
        case 'programa':
            return deletePrograma(id);
            break;
        case 'usuario':
            return deleteUsuario(id);
            break;
        default:
            break;
    }
}

function deleteUsuario(id) {
    borrado = false;
    $.ajax({
        type: "POST",
        data: {
            id_usuario: id
        },
        url: "/usuario/eliminar/",
        success: function (msg) {
            borrado = true;
            swal({
                title: "Borrado con éxito",
                text: "El usuario " + msg.nombre + " ha sido borrado con éxito",
                icon: "success",
                buttons: false,
                timer: 1500,
            });
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
    return borrado;

}

function deletePrograma(id) {
    borrado = false;
    $.ajax({
        type: "POST",
        data: {
            id_programa: id
        },
        url: "/programa/eliminar/",
        success: function (msg) {
            borrado = true;
            swal({
                title: "Borrado con éxito",
                text: "El programa " + msg.nombre + " ha sido borrado con éxito",
                icon: "success",
                buttons: false,
                timer: 1500,
            });
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
    return borrado;

}

function deleteEscuela(id) {
    borrado = false;

    $.ajax({
        type: "POST",
        data: {
            id_escuela: id
        },
        url: "/escuela/eliminar/",
        success: function (msg) {
            borrado = true;
            swal({
                title: "Borrado con éxito",
                text: "La escuela " + msg.nombre + " ha sido borrado con éxito",
                icon: "success",
                buttons: false,
                timer: 1500,
            });
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
    return borrado;

}

