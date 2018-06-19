$(document).on('click','#program', function(){
    var id_dir = $(this).attr('data-id');
    $.ajax({
        type: "POST",
        data: {
            id_usuario: id_dir
        },
        url: "/usuario/consulta_programa/",
        success: function (msg) {
            location.href = "programa/view/" + msg.programa
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
} )