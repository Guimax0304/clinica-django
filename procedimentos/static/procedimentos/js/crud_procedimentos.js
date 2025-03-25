document.addEventListener('DOMContentLoaded', function () {
    const formCriarProcedimento = document.getElementById('form-criar-procedimento');
    const mensagemSucesso = document.getElementById('mensagem-sucesso');
    const mensagemErro = document.getElementById('mensagem-erro');

    if (formCriarProcedimento) {
        formCriarProcedimento.addEventListener('submit', function (e) {
            e.preventDefault(); // Previne o envio padrão do formulário

            const formData = new FormData(formCriarProcedimento); // Captura os dados do formulário

            // Envia os dados para o endpoint de criação via AJAX
            fetch('/procedimentos/api/criar/', { // Ajuste a URL conforme o seu backend
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest', // Indica que é uma requisição AJAX
                    'X-CSRFToken': getCookie('csrftoken') // Adiciona o token CSRF para segurança
                }
            })
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'success') {
                        // Exibe mensagem de sucesso
                        mensagemSucesso.classList.remove('d-none');
                        mensagemErro.classList.add('d-none');
                        formCriarProcedimento.reset(); // Limpa o formulário
                    } else {
                        // Exibe mensagem de erro
                        mensagemSucesso.classList.add('d-none');
                        mensagemErro.classList.remove('d-none');
                        mensagemErro.textContent = `Erro: ${data.message || 'Verifique os dados e tente novamente.'}`;
                    }
                })
                .catch(error => {
                    // Lida com erros na comunicação
                    console.error('Erro na requisição:', error);
                    mensagemSucesso.classList.add('d-none');
                    mensagemErro.classList.remove('d-none');
                    mensagemErro.textContent = 'Erro ao se comunicar com o servidor.';
                });
        });
    }
});

// Função utilitária para obter o token CSRF
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
