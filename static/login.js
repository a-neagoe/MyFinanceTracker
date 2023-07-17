addEventListener('DOMContentLoaded', (event) => {
    // Example starter JavaScript for disabling form submissions if there are invalid fields
    (() => {
        'use strict'

        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        const forms = document.querySelectorAll('.needs-validation')

        // Loop over them and prevent submission
        Array.from(forms).forEach(form => {
          form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                // Stop the submit event and the propagation of submit!!
                event.preventDefault()
                event.stopPropagation()
            }

            form.classList.add('was-validated')
          }, false)
        })
    })()
});