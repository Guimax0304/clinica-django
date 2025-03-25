// pacientes/static/pacientes/js/crud_pacientes.js

document.addEventListener('DOMContentLoaded', function() {
    // Carregar lista de pacientes ao carregar a página
    carregarPacientes();

    // Adicionar evento ao formulário de criação
    const formCriar = document.getElementById('form-criar');
    if (formCriar) {
        formCriar.addEventListener('submit', function(event) {
            event.preventDefault();
            enviarRequisicaoAPI('/pacientes/api/criar/', 'POST', new FormData(formCriar), () => {
                alert('Paciente criado com sucesso!');
                carregarPacientes();
                formCriar.reset();
            });
        });
    }
});

// Centralização de URLs de API
const API_URLS = {
    listar: '/pacientes/api/listar/',
    criar: '/pacientes/api/criar/',
    obter: (id) => `/pacientes/api/obter/${id}/`,
    editar: (id) => `/pacientes/api/editar/${id}/`,
    deletar: (id) => `/pacientes/api/deletar/${id}/`
};

// Função para carregar pacientes
function carregarPacientes() {
    enviarRequisicaoAPI(API_URLS.listar, 'GET', null, (data) => {
        const tabelaPacientes = document.getElementById('tabela-pacientes');
        tabelaPacientes.innerHTML = '';

        data.pacientes.forEach(paciente => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${paciente.id}</td>
                <td>${paciente.nome}</td>
                <td>${paciente.telefone}</td>
                <td>${paciente.data_nascimento}</td>
                <td>${paciente.endereco}</td>
                <td>
                    <button class="btn btn-sm btn-warning" onclick="abrirFormularioEdicao(${paciente.id})">Editar</button>
                    <button class="btn btn-sm btn-danger" onclick="deletarPaciente(${paciente.id})">Deletar</button>
                </td>
            `;
            tabelaPacientes.appendChild(row);
        });
    });
}

// Função para abrir o formulário de edição
function abrirFormularioEdicao(id) {
    enviarRequisicaoAPI(API_URLS.obter(id), 'GET', null, (data) => {
        const formEditar = document.getElementById('form-editar');
        if (formEditar) {
            formEditar.elements['nome'].value = data.paciente.nome;
            // Preencher outros campos do formulário
            formEditar.onsubmit = function(event) {
                event.preventDefault();
                editarPaciente(id);
            };
        }
        $('#modal-editar').modal('show');
    });
}

// Função para editar paciente
function editarPaciente(id) {
    const formEditar = document.getElementById('form-editar');
    enviarRequisicaoAPI(API_URLS.editar(id), 'POST', new FormData(formEditar), () => {
        alert('Paciente editado com sucesso!');
        carregarPacientes();
        $('#modal-editar').modal('hide');
    });
}

// Função para deletar paciente
function deletarPaciente(id) {
    if (confirm('Tem certeza de que deseja deletar este paciente?')) {
        enviarRequisicaoAPI(API_URLS.deletar(id), 'POST', null, () => {
            alert('Paciente deletado com sucesso!');
            carregarPacientes();
        });
    }
}

// Função utilitária para enviar requisições de API
function enviarRequisicaoAPI(url, method, body = null, onSuccess = () => {}, onError = (error) => console.error(error)) {
    fetch(url, {
        method: method,
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Accept': 'application/json'
        },
        body: body
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            onSuccess(data);
        } else {
            alert('Erro: ' + (data.message || 'Erro desconhecido.'));
            onError(data.errors || data);
        }
    })
    .catch(onError);
}

// Função para obter o token CSRF
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
