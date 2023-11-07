console.log('ok');
function submitForm(event) {
    event.preventDefault(); // Impede o envio do formulário padrão
    
    var username = document.getElementById("floatingInput").value;
    var password = document.getElementById("floatingPassword").value;
    
    // Construa o objeto de dados para enviar ao servidor
    var data = {
        login: username,
        password: password
    };

    // Faça a solicitação POST para a URL de autenticação
    fetch('http://localhost:8080/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro na solicitação.');
        }
        return response.json();
    })
    .then(data => {
        // Manipule a resposta do servidor, que contém o token
        var token = data.token;
        // Você pode agora usar o token para autenticação ou armazená-lo onde for necessário
        console.log('Token recebido:', token);

        // Agora que você tem o token, você pode usá-lo em outras solicitações
        fetch('http://localhost:8080/ola', {
            method: 'GET', // ou 'POST' ou qualquer outro método necessário
            headers: {
                'Authorization': 'Bearer ' + token, // Adicione o token ao cabeçalho de autorização
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
if (!response.ok) {
throw new Error('Erro na solicitação para /ola.');
}
return response.text(); // Altere para response.text() para tratar a resposta como uma string
})
.then(olaData => {
// Faça algo com a string recebida de 'http://localhost:8080/ola'
console.log('Resposta de /ola:', olaData);
// Você pode manipular a string aqui
})
.catch(error => {
console.error('Ocorreu um erro ao acessar /ola:', error);
// Lide com erros aqui
});
    })
    .catch(error => {
        console.error('Ocorreu um erro na autenticação:', error);
        // Lide com erros de autenticação aqui
    });
}