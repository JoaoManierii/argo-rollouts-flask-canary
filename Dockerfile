# Usa a imagem base oficial do Python 3.10 (versão leve)
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos da pasta local "app/" para dentro da imagem
COPY app/ ./app/

# Copia o arquivo de dependências
COPY app/requirements.txt .

# Instala as dependências da aplicação
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta que o Flask usará
EXPOSE 5000

# Define o comando de inicialização da aplicação
CMD ["python3", "app/main.py"]
