# Usa uma imagem base Python enxuta
FROM python:3.10-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instala bibliotecas de sistema que muitos pacotes Python precisam para compilar:
#  - libpq-dev, gcc -> compilar psycopg2 (PostgreSQL)
#  - libjpeg-dev, zlib1g-dev -> Pillow (manipulação de imagens)
#  - libssl-dev, libffi-dev -> cryptography, etc.
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    libjpeg-dev \
    zlib1g-dev \
    libssl-dev \
    libffi-dev

# Copia o arquivo requirements.txt para dentro do contêiner e instala as dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do seu projeto (código Django) para dentro do contêiner
COPY . /app

# (Opcional) Se você servir arquivos estáticos localmente, pode rodar collectstatic aqui:
# RUN python manage.py collectstatic --noinput

# Expondo a porta 8000 (onde o Gunicorn/Django vai rodar)
EXPOSE 8000

# Comando para iniciar seu servidor Django.
# Ajuste "meu_projeto.wsgi" para o nome real do seu arquivo WSGI
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "meu_projeto.wsgi"]
