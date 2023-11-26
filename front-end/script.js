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
                console.log('Status da resposta:', response.status);

                if (response.status === 200) {
                    return response.json();
                } else {
                    throw new Error('Authentication failed');
                }
            })
            .then(user => {
                console.log('Dados do usuário recebidos:', user);


                window.location.href = 'dashboard.html';
            })
            .catch(error => {
                console.error('Erro:', error);
                var errorMessage = document.getElementById("error-message");
                errorMessage.innerText = 'Usuário ou senha incorretos';
                errorMessage.style.display = 'block';
            });
        }

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