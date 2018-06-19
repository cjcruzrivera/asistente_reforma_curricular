$(document).on('blur','#horas_magistral', function () {
    h_magistral = $('#horas_magistral').val();
    if(h_magistral <= 0){
        swal({
            title: "Error al registrar horas de clase magistrales",
            text: 'Número de horas no válidas. Deben ser mayores a 0',
            html: true,
            icon: "warning",
            type: "warning",
        })
        $('#horas_magistral').val('');
        return
    }

    h_independiente = $('#horas_independientes').val();
    creditos = $('#creditos').val();

    if(creditos != '' && h_independiente != ''){
        if((Number(h_magistral)+Number(h_independiente)) != (creditos*3)){
            swal({
                title: "Error al registrar horas magistrales",
                text: "Recuerde que el numero de horas de clase magistrales sumadas a las horas de estudio individual deben dar 3 veces el numero de creditos.",
                icon: "warning",
                buttons: false,
                dangerMode: true,
              })
        }
    }

});

$(document).on('blur','#horas_independientes', function () {
    h_independiente = $('#horas_independientes').val();
    if(h_independiente <= 0){
        swal({
            title: "Error al registrar horas de estudio independiente",
            text: 'Número de horas no válidas. Deben ser mayores a 0',
            html: true,
            icon: "warning",
            type: "warning",
        })
        $('#horas_independientes').val('');
        return
    }

    h_magistral = $('#horas_magistral').val();
    creditos = $('#creditos').val();

    if(creditos != '' && h_magistral != ''){
        if((Number(h_independiente)+Number(h_magistral)) != (creditos*3)){
            swal({
                title: "Error al registrar horas de estudio independiente",
                text: "Recuerde que el numero de horas de clase magistrales sumadas a las horas de estudio individual deben dar 3 veces el numero de creditos.",
                html: true,
                icon: "warning",
                type: "warning",
            })
            $('#horas_independientes').val('');
            return
        }
    }

});


$(document).on('blur','#creditos', function () {
    valor = $('#creditos').val();
    if(valor <= 0){
        swal({
            title: "Error al registrar numero de creditos",
            text: "Debe ser mayor a 0",
            html: true,
            icon: "warning",
            type: "warning",
        })
        $('#creditos').val('');
        return
    }

    h_magistral = $('#horas_magistral').val();
    h_independiente = $('#horas_independientes').val();

    if(h_independiente != '' && h-magistral != ''){
        if((Number(h_independiente)+Number(h-magistral)) != (valor*3)){
            swal({
                title: "Error al registrar creditos",
                text: "Recuerde que el numero de horas de clase magistrales sumadas a las horas de estudio individual deben dar 3 veces el numero de creditos.",
                html: true,
                icon: "warning",
                type: "warning",
            })
            $('#creditos').val('');
            return

        }
    }

});