# Usa a imagem base do Python (versão 3.10-slim)
FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Instala bibliotecas de sistema necessárias.
# Ajuste conforme precisar (ex.: mysqlclient -> libmysqlclient-dev, etc.)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    libjpeg-dev \
    zlib1g-dev \
    libssl-dev \
    libffi-dev

# Copia o arquivo requirements.txt para dentro do contêiner
COPY requirements.txt .

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o restante do seu código (Django)
COPY . /app

# (Opcional) Se você quiser fazer collectstatic
# RUN python manage.py collectstatic --noinput

# Expõe a porta 8000
EXPOSE 8000

# Ajuste "meu_projeto.wsgi" para o nome real do wsgi do seu projeto
CMD ["bash", "-c", "python manage.py migrate && gunicorn --bind 0.0.0.0:8000 meu_projeto.wsgi"]

