$(document).ready(function () {
    var texto_habilidad = $('select[id="habilidad_form"] option:selected').text()
    if(texto_habilidad != '---------'){
        $('#habilidad').text(texto_habilidad.toUpperCase())
    }
    var texto_contenido = $('#contenido_form').val()

    if(texto_contenido != ''){
        $('#contenido').text(texto_contenido.toUpperCase())
    }
    var texto_contexto = $('#contexto_form').val()

    if(texto_contexto != ''){
        $('#contexto').text(texto_contexto.toUpperCase())
    }

})

$(document).on('change', '#habilidad_form', function () {
    var texto_habilidad = $('select[id="habilidad_form"] option:selected').text()
    if(texto_habilidad === '---------'){
        texto_habilidad = "habilidad";
    }
    $('#habilidad').text(texto_habilidad.toUpperCase())
})

$(document).on('keyup', '#contenido_form', function () {
    var texto_contenido = $(this).val()
    if(texto_contenido === ''){
        texto_contenido = "CONTENIDO"
    }
    $('#contenido').text(texto_contenido.toUpperCase())
})

$(document).on('keyup', '#contexto_form', function () {
    var texto_contexto = $(this).val()
    if(texto_contexto === ''){
        texto_contexto = "contexto"
    }
    $('#contexto').text(texto_contexto.toUpperCase())
})


$(document).on('keypress', '.letras', function (e) {

    tecla = (document.all) ? e.keyCode : e.which;

    //backspace to delete always allows it
    if (tecla == 8) {
        return true;
    }
    // entry pattern, just accept numbers
    patron = /[0-9]/;
    tecla_final = String.fromCharCode(tecla);
    return !patron.test(tecla_final);
});