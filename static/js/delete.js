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
        case 'curso':
            var curso = "";
            curso = $(this).attr('data-nombre');
            mensaje = 'el curso ' + curso;
            break;
        case 'competencia':
            var competencia = "";
            competencia = $(this).attr('data-nombre');
            mensaje = 'la competencia ' + competencia;
            break;
        case 'resultado':
            var resultado = "";
            resultado = $(this).attr('data-id');
            mensaje = 'el resultado de aprendizaje número ' + resultado;
            break;
        case 'indicador':
            var indicador = "";
            indicador = $(this).attr('data-id');
            mensaje = 'el indicador de logro número ' + indicador;
            break;
        case 'actividad':
            var actividad = "";
            actividad = $(this).attr('data-id');
            mensaje = 'la actividad de logro número ' + actividad;
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
        case 'curso':
            return deleteCurso(id);
            break;
        case 'competencia':
            return deleteCompetencia(id);
            break;
        case 'resultado':
            return deleteResultado(id);
            break;
        case 'indicador':
            return deleteIndicador(id);
            break;
        case 'Actividad':
            return deleteActividad(id);
            break;
        default:
            break;
    }
}

function deleteActividad(id) {
    borrado = false;
    $.ajax({
        type: "POST",
        data: {
            id_actividad: id
        },
        url: "/actividad/eliminar/",
        success: function (msg) {
            borrado = true;
            swal({
                title: "Borrado con éxito",
                text: "La actividad de logro ha sido borrado con éxito",
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

function deleteIndicador(id) {
    borrado = false;
    $.ajax({
        type: "POST",
        data: {
            id_indicador: id
        },
        url: "/indicador/eliminar/",
        success: function (msg) {
            borrado = true;
            swal({
                title: "Borrado con éxito",
                text: "El indicador de logro ha sido borrado con éxito",
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

function deleteResultado(id) {
    borrado = false;
    $.ajax({
        type: "POST",
        data: {
            id_resultado: id
        },
        url: "/resultado/eliminar/",
        success: function (msg) {
            borrado = true;
            swal({
                title: "Borrado con éxito",
                text: "El resultado de aprendizaje ha sido borrado con éxito",
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

function deleteCompetencia(id) {
    borrado = false;
    $.ajax({
        type: "POST",
        data: {
            id_competencia: id
        },
        url: "/competencia/eliminar/",
        success: function (msg) {
            borrado = true;
            swal({
                title: "Borrado con éxito",
                text: "La competencia " + msg.nombre + " ha sido borrada con éxito",
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

function deleteCurso(id) {
    borrado = false;
    $.ajax({
        type: "POST",
        data: {
            id_curso: id
        },
        url: "/curso/eliminar/",
        success: function (msg) {
            borrado = true;
            swal({
                title: "Borrado con éxito",
                text: "El curso " + msg.nombre + " ha sido borrado con éxito",
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

