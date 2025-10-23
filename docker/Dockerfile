# Usar Python 3.11 slim como base para melhor performance
FROM python:3.11-slim

# Definir informações do mantenedor
LABEL maintainer="PDF-to-Markdown Converter"
LABEL description="PDF to Markdown Converter using Docling"
LABEL version="1.0.0"

# Definir diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema necessárias para o Docling
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1-mesa-dev \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    libgcc-s1 \
    && rm -rf /var/lib/apt/lists/*

# Copiar arquivo de dependências
COPY ../src/requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Criar diretórios necessários primeiro
RUN mkdir -p /app/pdfs /app/out

# Criar script de pré-carregamento
COPY ../src/preload_models.py .

# Pré-carregar modelos do Docling e RapidOCR (resolver problema de primeira execução)
RUN python preload_models.py || echo "Aviso: Alguns modelos podem ser baixados na primeira execução"

# Copiar código da aplicação
COPY ../src/convert_pdf_to_markdown.py .

# Garantir permissões para o diretório de modelos
RUN chmod -R 755 /usr/local/lib/python3.11/site-packages/ || true

# Definir variáveis de ambiente
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Criar usuário não-root para segurança
RUN useradd --create-home --shell /bin/bash appuser && \
    chown -R appuser:appuser /app
USER appuser

# Definir volumes para arquivos PDF e saída
VOLUME ["/app/pdfs", "/app/out"]

# Ponto de entrada da aplicação
CMD ["python", "convert_pdf_to_markdown.py"]