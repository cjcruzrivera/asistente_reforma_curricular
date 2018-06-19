$(document).ready(function () {

    var seleccion = "<option value='' selected>---------</option><option>SELECCIONE ESCUELA </option>"
    if ($('#dir_programa').val() == 0) {
        $('#dir_programa').html('');
        $('#dir_programa').append(seleccion)
    }
})

$(document).on('change', '#escuela', function () {
    var id = $(this).val();
    $.ajax({
        type: "POST",
        data: {
            id_escuela: id
        },
        url: "/programa/lista_dir/",
        success: function (msg) {
            // console.log(msg)
            // console.log(typeof(msg))
            var selector = "<option value='' selected>---------</option>";
            // 
            if (msg.vacio == 'vacio') {
                selector += "<option>SELECCIONE ESCUELA </option>";
                $('#dir_programa').html('');
                $('#dir_programa').append(selector);
                return;
            }
            if (msg === '[]') {
                selector += "<option>La escuela seleccionada no registra usuarios. Seleccionar otra </option>";
                $('#dir_programa').html('');
                $('#dir_programa').append(selector);
                return;
            }
            var data = JSON.parse(msg);
            for (var i in data) {
                selector += "<option value = '" + data[i].pk + "'>" + data[i].fields.first_name + " " + data[i].fields.last_name + " </option>";
                $('#dir_programa').html('');
                $('#dir_programa').append(selector);
                console.log(data[i]);  // (o el campo que necesites)
            }
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

$(document).on('keypress', '.number', function (e) {

    tecla = (document.all) ? e.keyCode : e.which;

    //backspace to delete always allows it
    if (tecla == 8) {
        return true;
    }
    // entry pattern, just accept numbers
    patron = /[0-9]/;
    tecla_final = String.fromCharCode(tecla);
    return patron.test(tecla_final);
});