$(document).ready(function () {
    var texto_verbo = $('select[id="verbo_form"] option:selected').text()
    if(texto_verbo != '---------'){
        $('#verbo').text(texto_verbo.toUpperCase())
    }
    var texto_contenido = $('#contenido_form').val()

    if(texto_contenido != ''){
        $('#contenido').text(texto_contenido.toUpperCase())
    }
    var texto_contexto = $('#contexto_form').val()

    if(texto_contexto != ''){
        $('#contexto').text(texto_contexto.toUpperCase())
    }
    var texto_proposito = $('#proposito_form').val()

    if(texto_proposito != ''){
        $('#proposito').text(texto_proposito.toUpperCase())
    }
})

$(document).on('change', '#verbo_form', function () {
    var texto_verbo = $('select[id="verbo_form"] option:selected').text()
    if(texto_verbo === '---------'){
        texto_verbo = "VERBO";
    }
    $('#verbo').text(texto_verbo.toUpperCase())
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

$(document).on('keyup', '#proposito_form', function () {
    var texto_proposito = $(this).val()
    if(texto_proposito === ''){
        texto_proposito = "proposito"
    }
    $('#proposito').text(texto_proposito.toUpperCase())
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