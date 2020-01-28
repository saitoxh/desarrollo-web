function confirmarEliminacion(id){

    Swal.fire({
        title: 'Estás seguro ?',
        text: "No podrás deshacer esta acción",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Eliminar!',
        cancelButtonText:'Cancelar'
      }).then((result) => {
        if (result.value) {

            window.location.href = "/eliminar_negocio/"+id+"/";

          
        }
      })
}