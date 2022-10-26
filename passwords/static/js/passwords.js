const togglePassword = (id) => {
    targetInput = document.getElementById(`input${id}`)
    if (targetInput.type === 'password') {
        targetInput.type = 'text';
    }
    else {
        targetInput.type = 'password';
    }
}

const toggleAll = () => {
    inputs = document.getElementsByTagName('input');
    for (input of inputs) {
        if (input.type === 'password') {
            input.type = 'text';
        }
        else {
            input.type = 'password';
        }
    }
}