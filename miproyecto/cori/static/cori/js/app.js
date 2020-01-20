$("#formulario").validate({
    errorClass:"is-invalid",
    rules:{
        nombre:{
            required:true
        },
        email:{
            required:true,
            email:true
        },
        comuna:{
            required:true,

        },
        lugar:{
            required:true
        },
        descripcion:{
            required:true
        }
    },
    messages:{
        nombre:{
            required:"este campo es requerido"
        },
        email:{
            required:"este campo es requerido",
            email:"debes ingresar un email valido"
        },
        comuna:{
            required:"este campo es requerido"
        },
        lugar:{
            required:"este campo es requerido"
        },
        descripcion:{
            required:"este campo es requerido"
    }
}
})