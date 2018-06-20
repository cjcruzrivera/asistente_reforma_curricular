$(document).ready(function () {

    if ($('#programa').val() == 0 || $('#programa').val() ==  undefined) {
        var seleccion = "<option value='' selected>---------</option><option>SELECCIONE PROGRAMA </option>"
        $('#semestre').html('');
        $('#semestre').append(seleccion)
    }
});


$(document).on('change', '#programa', function () {
    
});