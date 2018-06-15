$(document).ready(function () {
    $('#escuelas').DataTable()
})

$(document).on('click', '#delete', function () {
    var escuela = "";
    escuela = $(this).attr('data-nombre');
    id_escuela = $(this).attr('data-id');
    swal({
        title: "Advertencia",
        text: "¿Seguro que desea eliminar la escuela " + escuela + "?",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    })
        .then((willDelete) => {
            if (willDelete) {
                borrado = deleteEscuela(id_escuela);
                if (borrado) {
                    swal({
                        title: "Borrado con éxito",
                        text: "La escuela " + escuela + " ha sido borrado con éxito",
                        icon: "success",
                        buttons: false,
                        timer: 1500,
                    });

                    setTimeout(function () { location.reload(true); }, 1500);
                }
            }
        });
});

function deleteEscuela(id) {
    borrado = false;

    $.ajax({
        type: "POST",
        data: {
            id_escuela: id
        },
        url: "/escuela/eliminar/",
        success: function (msg) {
            borrado = true;
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
    return borrado;

}

// function deleteProducto(id) {

//     $.ajax({
//         type: "POST",
//         data: {
//             id_producto: id
//         },
//         url: "/productos/eliminar/",
//         success: function (msg) {
//             borrado = "SI";
//         },
//         async: false,
//         dataType: "json",
//         cache: "false",
//         error: function (msg) {
//             swal({
//                 title: "Error AJAX",
//                 text: msg.responseText,
//                 html: true,
//                 type: "warning",
//                 confirmButtonColor: "#d51b23"
//             });
//             console.log("AJAXerror");
//             console.log(msg);
//             borrado = "NO";
//         },
//     });
//     return borrado;
// }