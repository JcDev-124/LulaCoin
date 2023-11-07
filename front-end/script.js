function submitForm(event) {
    event.preventDefault(); // Impede o envio do formulário padrão
    
    var username = document.getElementById("floatingInput").value;
    var password = document.getElementById("floatingPassword").value;
    
    var data = {
        login: username,
        password: password
    };

    fetch('http://localhost:5000/users', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.status === 200) {
            window.location.href = 'dashboard.html';
        } else {
            var errorMessage = document.getElementById("error-message");
            errorMessage.innerText = 'Usuário ou senha incorretos';
            errorMessage.style.display = 'block';
        }
    })
    .catch(error => {
        var errorMessage = document.getElementById("error-message");
        errorMessage.innerText = 'Ocorreu um erro na autenticação. Tente novamente mais tarde.';
        errorMessage.style.display = 'block';
    });
}
