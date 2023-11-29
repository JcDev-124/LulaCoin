//Variáveis Globais
var allTransactions = [];
var transactionsSelected =[];

//Requisições
function submitForm(event) {
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
        console.log('Status da resposta:', response.status);
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
        console.log(dados);
        window.location.href = 'dashboard.html';
    })
    .catch(error => {
        console.error('Erro:', error);
        var errorMessage = document.getElementById("error-message");
        errorMessage.innerText = 'Usuário ou senha incorretos';
        errorMessage.style.display = 'block';
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
        successMessage.innerText = 'Cadastro efetuado com sucesso!';
        successMessage.style.display = 'block';
                
    })
    .catch(error => {
        console.error('Erro:', error);
        var errorMessage = document.getElementById("error-message");
        errorMessage.innerText = 'Ocorreu um erro no cadastro.';
        errorMessage.style.display = 'block';
    });
}

function NewTransfer(event) {
    event.preventDefault(); 
        
    var receiverKey = document.getElementById("ReceiverKey").value;
    var password = document.getElementById("TransPassword").value;
    var value = document.getElementById("TransValor").value;
    var taxa = 0.01;
        
    var data = {
        public_key: receiverKey,
        private_key: password,
        taxa: taxa,
        valor: value
    };
        
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
        successMessage.innerText = 'Transferência efetuada aguarde a validação!';
        successMessage.style.display = 'block';
                
    })
    .catch(error => {
        console.error('Erro:', error);
        var errorMessage = document.getElementById("error-message");
        errorMessage.innerText = 'Transferência Falhou';
        errorMessage.style.display = 'block';
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
        errorMessage.innerText = 'Falha ao carregar as transferências';
        errorMessage.style.display = 'block';
    });
}

function Mine(event) {
    event.preventDefault();

    var transactions = transactionsSelected;
    console.log(transactions);
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
        if (response.status === 201) {
            return response.json();
        } else {
            throw new Error('Falha');
        }
    })
    .then(user => {
        var successMessage = document.getElementById("success-message");
        successMessage.innerText = 'Mineração feita com Sucesso!';
        successMessage.style.display = 'block';
    })
    .catch(error => {
        console.error('Erro:', error);
        var errorMessage = document.getElementById("error-message");
        errorMessage.innerText = 'Mineração Falhou';
        errorMessage.style.display = 'block';
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
            // Recupere os dados da sessionStorage
            var cpf = sessionStorage.getItem('cpf');
            var saldo = sessionStorage.getItem('saldo');
            var sald= document.getElementById('sald');
            sald.innerText = 'LC ' + saldo;
            var publicData = sessionStorage.getItem('public');
            var privateData = sessionStorage.getItem('private');
            var pass = document.getElementById('TransPassword');
            pass.value = privateData;
        
            // Faça o que for necessário com os dados recuperados
            console.log('CPF:', cpf);
            console.log('Saldo:', saldo);
            console.log('Public:', publicData);
            console.log('Private:', privateData);
        
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

