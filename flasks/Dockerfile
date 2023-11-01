# Use a imagem oficial do Python como base
FROM python:3.8-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos necessários para o contêiner
COPY app.py .
COPY requirements.txt .

# Instalando as dependências
RUN pip install -r requirements.txt

# Exponha a porta em que o aplicativo Flask será executado
EXPOSE 5000

# Inicie o aplicativo Flask quando o contêiner for executado
CMD ["python", "app.py"]


