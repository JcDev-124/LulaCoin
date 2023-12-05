//Variáveis Globais
var allTransactions = [];
var transactionsSelected =[];

//Requests
function Login(event) {
    event.preventDefault(); 

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
            return response.json();
        } else {
            throw new Error('Authentication failed');
        }
    })
    .then(user => {
        let dados = JSON.parse(user);
        sessionStorage.setItem('cpf', dados.cpf);
        sessionStorage.setItem('saldo', dados.saldo);
        sessionStorage.setItem('public', dados.public_key);
        sessionStorage.setItem('private', dados.private_key);
        sessionStorage.setItem('username', username);
        sessionStorage.setItem('pass', password);
        window.location.href = 'dashboard.html';
    })
    .catch(error => {
        console.error('Erro:', error);
        var errorMessage = document.getElementById("error-message");
        errorMessage.innerText = 'Incorrect username or password';
        errorMessage.style.display = 'block';

        setTimeout(function () {
            errorMessage.style.display = 'none';
        }, 3000);
    });
}

function NewUser(event) {
    event.preventDefault(); 
        
    var username = document.getElementById("NewLogin").value;
    var password = document.getElementById("NewPassword").value;
    var cpf = document.getElementById("NewCpf").value;
        
    var data = {
        login: username,
        password: password,
        cpf: cpf,
        saldo: 1000
    };
        
    fetch('http://localhost:5000/registerUser', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.status === 201) {
            return response.json();
        } else {
            throw new Error('Ocorreu um erro no cadastro');
        }
    })
    .then(user => {
        var successMessage = document.getElementById("success-message");
        successMessage.innerText = 'Registration successfully Complete!';
        successMessage.style.display = 'block';

        setTimeout(function () {
            successMessage.style.display = 'none';
        }, 3000);
                
    })
    .catch(error => {
        console.error('Erro:', error);
        var errorMessage = document.getElementById("error-message");
        errorMessage.innerText = 'An error occurred during registration.';
        errorMessage.style.display = 'block';

        setTimeout(function () {
            errorMessage.style.display = 'none';
        }, 3000);
    });
}

function NewTransfer(event) {
    event.preventDefault(); 
        
    var receiverKey = document.getElementById("ReceiverKey").value;
    var password = sessionStorage.getItem('private');
    var value = document.getElementById("TransValor").value;
    var taxa = 0.01;
        
    var data = {
        public_key: receiverKey,
        private_key: password,
        taxa: taxa,
        valor: value
    };
    console.log(data);
        
    fetch('http://localhost:5000/transaction', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.status === 201) {
            return response.json();
        } else {
            throw new Error('Ocorreu um erro no cadastro');
        }
    })
    .then(user => {
        var successMessage = document.getElementById("success-message");
        successMessage.innerText = 'Transfer made, wait for validation!';
        successMessage.style.display = 'block';
        var block = document.getElementById("formularioModal");
        block.style.display = 'none';

        setTimeout(function () {
            successMessage.style.display = 'none';
        }, 3000);
                
    })
    .catch(error => {
        console.error('Erro:', error);
        var errorMessage = document.getElementById("error-message");
        errorMessage.innerText = 'Transfer Failed';
        errorMessage.style.display = 'block';

        setTimeout(function () {
            errorMessage.style.display = 'none';
        }, 3000);
    });
}

function GetTransfer(event) {
    event.preventDefault();

    fetch('http://localhost:5000/transaction', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (response.status === 200) {
            return response.json();
        } else {
            throw new Error('Ocorreu um erro na transferência');
        }
    })
    .then(transactions => {
        allTransactions = transactions;
        renderTransactions(transactions);
    })
    .catch(error => {
        console.error('Erro:', error);
        var errorMessage = document.getElementById("error-message");
        errorMessage.innerText = 'Failed to load';
        errorMessage.style.display = 'block';

        setTimeout(function () {
            errorMessage.style.display = 'none';
        }, 3000);
    });
}

//Requests
function Reload() {

    var username = sessionStorage.getItem('username');
    var password = sessionStorage.getItem('pass');

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
            return response.json();
        } else {
            throw new Error('Authentication failed');
        }
    })
    .then(user => {
        let dados = JSON.parse(user);
        sessionStorage.setItem('saldo', dados.saldo);
        window.location.href = 'dashboard.html';
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}

function Mine(event) {
    event.preventDefault();

    var transactions = transactionsSelected;
    var publicData = sessionStorage.getItem('public');

    var data = {
        transacoes: transactions,
        key_minerador: publicData
    };

    console.log(JSON.stringify(data));

    fetch('http://localhost:5000/block', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data),
    })
    .then(response => {
        if (response.status == 201) {
            var successMessage = document.getElementById("success-message");
            successMessage.innerText = 'Mining done successfully!';
            successMessage.style.display = 'block';
            setTimeout(function () {
                successMessage.style.display = 'none';
            }, 3000);
            return response.json();
        } else {
            throw new Error('Falha');
        }
    })
    .then(user => {
        var successMessage = document.getElementById("success-message");
        successMessage.innerText = 'Mining done successfully!';
        successMessage.style.display = 'block';

        setTimeout(function () {
            successMessage.style.display = 'none';
        }, 3000);
        Reload();
    })
    .catch(error => {
        console.error('Erro:', error);
        var errorMessage = document.getElementById("error-message");
        errorMessage.innerText = 'Mining Failed';
        errorMessage.style.display = 'block';

        setTimeout(function () {
            errorMessage.style.display = 'none';
        }, 3000);
    });
}

//Funções de interface
        document.getElementById('abrirFormulario').addEventListener('click', function() {
            document.getElementById('formularioModal').style.display = 'block';
          });
          
          document.getElementById('fecharFormulario').addEventListener('click', function() {
            document.getElementById('formularioModal').style.display = 'none';
          });
          
          // Fechar o formulário se o usuário clicar fora dele
          window.addEventListener('click', function(event) {
            if (event.target == document.getElementById('formularioModal')) {
              document.getElementById('formularioModal').style.display = 'none';
            }
          });

document.addEventListener('DOMContentLoaded', function() {
    var saldo = sessionStorage.getItem('saldo');
    var sald= document.getElementById('sald');
    sald.innerHTML = `<p class="saldo">LC ${saldo}</p>`;

    var user = sessionStorage.getItem('username');
    var Muser= document.getElementById('user');
    Muser.innerHTML = `<p class="usuario">${user}</p>`;
        
            /* Limpe os dados da sessionStorage se necessário
            sessionStorage.removeItem('cpf');
            sessionStorage.removeItem('saldo');
            sessionStorage.removeItem('public');
            sessionStorage.removeItem('private');*/
    });
        
//Botões
var btnTransfer = document.getElementById("btnReload");
btnTransfer.addEventListener("click", GetTransfer);

var btnMine = document.getElementById("mine-button");
btnMine.addEventListener("click", Mine);



function renderTransactions(transactions) {
    // Obtenha o contêiner onde as transações serão exibidas
    var transactionContainer = document.getElementById("transactionList");
    transactionContainer.innerHTML = '';
    
    transactions.forEach(transaction => {
        var transactionElement = document.createElement("div");
        transactionElement.classList.add("transaction");
        // Ajuste no ID do checkbox para usar transaction.cod
        transactionElement.innerHTML = `
            <input type="checkbox" id="transaction-${transaction.cod}" class="transactionCheckbox" onchange="handleCheckboxChange(${transaction.cod})">
            <p>ID: ${transaction.cod} Reward: ${transaction.taxa * transaction.valor}</p>
        `;
        
        transactionContainer.appendChild(transactionElement);
    });
}

function handleCheckboxChange(transactionId) {
    var checkbox = document.getElementById(`transaction-${transactionId}`);
    
    if (checkbox.checked) {
        // Ajuste para procurar a transação usando transaction.cod
        var selectedTransaction = allTransactions.find(transaction => transaction.cod === transactionId);
        
        // Adiciona a transação ao array global 'transactionsSelected'
        transactionsSelected.push(selectedTransaction);
        
        // Exibe as transações selecionadas no console (você pode personalizar conforme necessário)
        console.log("Transações Selecionadas:", transactionsSelected);
    } else {
        // Se o checkbox foi desmarcado, remove a transação do array 'transactionsSelected'
        transactionsSelected = transactionsSelected.filter(transaction => transaction.cod !== transactionId);
        
        // Exibe as transações selecionadas no console (você pode personalizar conforme necessário)
        console.log("Transações Selecionadas:", transactionsSelected);
    }
}

document.getElementById('key').addEventListener('click', function() {
    // Variável que você quer copiar
    var variavelDoSistema = sessionStorage.getItem('public');

    // Criando um elemento de texto temporário para armazenar o conteúdo
    var tempInput = document.createElement('input');
    tempInput.value = variavelDoSistema;
    document.body.appendChild(tempInput);

    // Selecionando o conteúdo do elemento de texto temporário
    tempInput.select();
    tempInput.setSelectionRange(0, 99999); // Para dispositivos móveis

    // Copiando o conteúdo para a área de transferência
    document.execCommand('copy');

    // Removendo o elemento de texto temporário
    document.body.removeChild(tempInput);

    var successMessage = document.getElementById("success-message");
    successMessage.innerText = 'Your key has been copied';
    successMessage.style.display = 'block';

    setTimeout(function () {
        successMessage.style.display = 'none';
    }, 3000);
});
