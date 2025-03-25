# 1) Escolhe a imagem base com Python
FROM python:3.10-slim

# 2) Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# 3) Copia o requirements.txt e instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4) Copia todo o resto do código (seu projeto) para dentro do contêiner
COPY . /app

# 5) (Opcional) se você quiser já rodar collectstatic
# RUN python manage.py collectstatic --noinput

# 6) Expõe a porta em que o servidor vai rodar
EXPOSE 8000

# 7) Comando para iniciar o Django
# - Aqui usamos gunicorn (melhor que runserver em prod).
# - Substitua "meu_projeto.wsgi" pelo nome real do seu projeto e do arquivo wsgi.py.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "meu_projeto.wsgi"]
