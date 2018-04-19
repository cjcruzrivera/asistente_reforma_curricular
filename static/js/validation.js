$(document).on('blur','#horas_magistral', function () {
    valor = $('#horas_magistral').val();
    if(valor <= 0){
        alert('Número de horas no válidas. Deben ser mayores a 0')
    }

    valor2 = $('#horas_independientes').val();
    valor3 = $('#creditos').val();

    if(valor3 != '' && valor2 != ''){
        if((Number(valor)+Number(valor2)) != (valor3*3)){
            console.log(valor+valor2)
            console.log("")
            console.log(valor3*3)
            alert('Número de horas de clase magistral invalidas.')
        }
    }

});

$(document).on('blur','#horas_independientes', function () {
    valor = $('#horas_independientes').val();
    if(valor <= 0){
        alert('Número de horas no válidas. Deben ser mayores a 0')
    }

    valor2 = $('#horas_magistral').val();
    valor3 = $('#creditos').val();

    if(valor3 != '' && valor2 != ''){
        if((Number(valor)+Number(valor2)) != (valor3*3)){
            console.log(valor+valor2)
            console.log("")
            console.log(valor3*3)
            alert('Número de horas de clase magistral invalidas.')
        }
    }

});


$(document).on('blur','#creditos', function () {
    valor = $('#creditos').val();
    if(valor <= 0){
        alert('Número de horas no válidas. Deben ser mayores a 0')
    }

    valor2 = $('#horas_magistral').val();
    valor3 = $('#horas_independientes').val();

    if(valor3 != '' && valor2 != ''){
        if((Number(valor3)+Number(valor2)) != (valor*3)){
            console.log(valor+valor2)
            console.log("")
            console.log(valor3*3)
            alert('Número de horas de clase magistral invalidas.')
        }
    }

});