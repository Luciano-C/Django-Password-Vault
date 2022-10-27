const togglePassword = (id) => {
    targetInput = document.getElementById(`input${id}`)
    targetEye = document.getElementById(`eye${id}`)
    if (targetInput.type === 'password') {
        targetInput.type = 'text';
        targetEye.classList.add('fa-eye-slash')
        targetEye.classList.remove('fa-eye')
    }
    else {
        targetInput.type = 'password';
        targetEye.classList.add('fa-eye')
        targetEye.classList.remove('fa-eye-slash')
    }


}
