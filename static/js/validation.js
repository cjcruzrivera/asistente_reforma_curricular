$(document).on('blur','#horas_magistral', function () {
    h_magistral = $('#horas_magistral').val();
    if(h_magistral <= 0){
        alert('Número de horas no válidas. Deben ser mayores a 0')
    }

    h_independiente = $('#horas_independientes').val();
    creditos = $('#creditos').val();

    if(creditos != '' && h_independiente != ''){
        if((Number(h_magistral)+Number(h_independiente)) != (creditos*3)){
            alert('Número de horas de clase magistral invalidas.')
        }
    }

});

$(document).on('blur','#horas_independientes', function () {
    h_independiente = $('#horas_independientes').val();
    if(h_independiente <= 0){
        alert('Número de horas no válidas. Deben ser mayores a 0')
    }

    h_magistral = $('#horas_magistral').val();
    creditos = $('#creditos').val();

    if(creditos != '' && h_magistral != ''){
        if((Number(h_independiente)+Number(h_magistral)) != (creditos*3)){
            alert('Número de horas de clase magistral invalidas.')
        }
    }

});


$(document).on('blur','#creditos', function () {
    valor = $('#creditos').val();
    if(valor <= 0){
        alert('Número de horas no válidas. Deben ser mayores a 0')
    }

    h_magistral = $('#horas_magistral').val();
    h_independiente = $('#horas_independientes').val();

    if(h_independiente != '' && h-magistral != ''){
        if((Number(h_independiente)+Number(h-magistral)) != (valor*3)){
            alert('Número de horas de clase magistral invalidas.')
        }
    }

});