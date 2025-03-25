document.getElementById('form-criar-profissional').addEventListener('submit', function (e) {
    e.preventDefault();  

    const form = this;
    const formData = new FormData(form);  

    // Validação local simples (exemplo: verificar se o nome está preenchido)
    if (!formData.get('nome')) {
        alert('Por favor, preencha o campo Nome.');
        return;
    }

    const submitButton = form.querySelector('button[type="submit"]');
    submitButton.disabled = true;
    submitButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Salvando...';

    fetch(form.action, {  // URL dinâmica definida no template
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',  
            'X-CSRFToken': formData.get('csrfmiddlewaretoken')  
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert('Profissional criado com sucesso!');
            form.reset();  // Limpa o formulário
        } else if (data.errors) {
            let errorMessages = Object.values(data.errors).join('\n');
            alert(`Erro ao criar profissional:\n${errorMessages}`);
        } else {
            alert('Erro desconhecido ao criar profissional.');
        }
    })
    .catch(error => console.error('Erro:', error))
    .finally(() => {
        submitButton.disabled = false;
        submitButton.innerHTML = 'Salvar';
    });
});

