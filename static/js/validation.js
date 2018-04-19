$(document).on('blur','#horas_magistral', function () {
    valor = $('#horas_magistral').val();
    if(valor <= 0){
        alert('Número de horas no válidas. Deben ser mayores a 0')
    }

    valor2 = $('#horas_independientes').val();
    valor3 = $('#creditos').val();

    if(valor3 != '' && valor2 != ''){
        if((valor+valor2) != (valor3*3)){
            alert('Número de horas de clase magistral invalidas.')
        }
    }

});