# Usa Python 3.10 slim como base
FROM python:3.10-slim

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Instala bibliotecas de sistema necessárias
# (libpq-dev e gcc para psycopg2, libssl-dev e libffi-dev se precisar de cryptography, etc.)
# Se também usar Pillow, pode adicionar libjpeg-dev, zlib1g-dev
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    libssl-dev libffi-dev \
    libjpeg-dev zlib1g-dev

# Copia o requirements.txt e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código (Django)
COPY . /app

# Expondo a porta 8000, onde o Gunicorn vai rodar
EXPOSE 8000

# Rodar as migrações antes de iniciar o Gunicorn
CMD ["bash", "-c", "python manage.py migrate && gunicorn --bind 0.0.0.0:8000 meu_projeto.wsgi"]
