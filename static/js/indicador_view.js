$(document).ready(function() {

    $('#actividades').DataTable({
        "language": {
            "lengthMenu": "Mostrando _MENU_ programas academicos",
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

});

$(document).on('click','#nuevo', function () {
    $('#actualizar').attr('hidden', true);;
    $('#guardar').attr('hidden', false);;
})

$(document).on('click', '#actualizar', function () {
    var tipo_act = $('#tipo').val();
    if(tipo_act == 0){
        swal({
            title: "Seleccione el tipo de actividad",
            text: '',
            html: true,
            icon:'warning',
            type: "warning",
            confirmButtonColor: "#d51b23"
        });
        return
    }

    var descripcion_act = $('#descripcion').val();
    if(descripcion_act === ''){
        swal({
            title: "Ingrese la descripcion de la actividad",
            text: '',
            html: true,
            icon:'warning',
            type: "warning",
            confirmButtonColor: "#d51b23"
        });
        return
    }

    var actividad = $(this).attr('data-id');
    $.ajax({
        type: "POST",
        data: {
            id_actividad: actividad,
            tipo: tipo_act,
            descripcion: descripcion_act,
        },
        url: "/actividad/editar/",
        success: function (msg) {
            swal({
                title: "Almacenado con éxito",
                text: "La actividad ha sido modificada correctamente",
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
});

$(document).on('click','#editar', function () {
    
    var actividad = $(this).attr('data-id')
    var tipo = $('#type'+actividad).attr('data-tipo')
    var descripcion = $('#description'+actividad).text()
    $('#actualizar').attr('data-id', actividad)
    $('#descripcion').val(descripcion)
    $("#tipo").val(tipo)
    $('#guardar').attr('hidden', true);
    $('#actualizar').attr('hidden', false);

})

$(document).on('click', '#guardar', function () {
    var tipo_act = $('#tipo').val();
    if(tipo_act == 0){
        swal({
            title: "Seleccione el tipo de actividad",
            text: '',
            html: true,
            icon:'warning',
            type: "warning",
            confirmButtonColor: "#d51b23"
        });
        return
    }

    var descripcion_act = $('#descripcion').val();
    if(descripcion == ''){
        swal({
            title: "Ingrese la descripcion de la actividad",
            text: '',
            html: true,
            icon:'warning',
            type: "warning",
            confirmButtonColor: "#d51b23"
        });
        return
    }

    var indicador = $(this).attr('data-indicador')

    $.ajax({
        type: "POST",
        data: {
            id_indicador: indicador,
            tipo: tipo_act,
            descripcion: descripcion_act,
        },
        url: "/indicador/actividad/",
        success: function (msg) {
            swal({
                title: "Almacenado con éxito",
                text: "La actividad ha sido registrada correctamente",
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