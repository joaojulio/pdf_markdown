# 📄 PDF to Markdown Converter

Ferramenta profissional para conversão de arquivos PDF para formato Markdown usando [Docling](https://github.com/DS4SD/docling). Projeto 100% containerizado com Docker para execução em qualquer máquina com experiência de primeira classe.

## 🚀 Características

- ✅ **Conversão PDF → Markdown** usando Docling (OCR + AI)
- ✅ **Seleção dinâmica** de arquivos (interativa, lista, ou caminho manual)
- ✅ **Containerizado com Docker** - funciona em qualquer máquina
- ✅ **Acesso a arquivos externos** - suporte completo ao sistema de arquivos
- ✅ **Primeira execução otimizada** - modelos pré-carregados, sem erros de permissão
- ✅ **Interface amigável** com emojis, progress bars e feedback visual
- ✅ **Scripts de automação** PowerShell para facilitar o uso
- ✅ **Sistema de fallback resiliente** - sempre funciona, mesmo sem internet
- ✅ **Diretório /out organizado** - arquivos de saída separados com Git ignore
- ✅ **Compatível com ambientes corporativos** - funciona mesmo com firewall restritivo

## ⚡ Quick Start (Execução Rápida)

### � Executar em 3 Comandos

```powershell
# 1. Clone o repositório
git clone https://github.com/seu-usuario/pdf_markdown.git
cd pdf_markdown

# 2. Build automático
.\build.ps1 build

# Executar modo interativo
.\build.ps1 interactive
```

**Pronto!** 🎉 Agora você pode converter qualquer PDF para Markdown.

> 🛡️ **Sistema Resiliente**: Funciona mesmo em ambientes corporativos com firewall. Usa fallback automático (PyMuPDF) quando Docling não consegue acessar modelos online.

## 🆕 Atualizações Recentes (v2.0)

### 🎯 Principais Melhorias Implementadas

**🛡️ Sistema de Fallback Automático**
- ✅ Detecta automaticamente problemas de conectividade
- ✅ Ativa PyMuPDF como fallback quando Docling falha
- ✅ **Sempre funciona**, mesmo sem internet ou com firewall corporativo
- ✅ Mensagens informativas sobre qual método está sendo usado

**📁 Organização de Arquivos**
- ✅ Diretório `/out/` dedicado para arquivos .md gerados
- ✅ Git ignore configurado automaticamente
- ✅ Separação clara entre código fonte e arquivos de saída
- ✅ Estrutura preservada no repositório com `.gitkeep`

**🔧 Modelos Pré-carregados**
- ✅ RapidOCR models baixados durante o build
- ✅ Primeira execução instantânea
- ✅ Sem downloads surpresa durante o uso
- ✅ Performance consistente

**🌐 Compatibilidade Corporativa**
- ✅ Funciona com firewall restritivo
- ✅ Não depende de acesso à Hugging Face Hub
- ✅ Fallback transparente para o usuário
- ✅ Experiência confiável em qualquer ambiente

---

## �📋 Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/) instalado e funcionando
- [Docker Compose](https://docs.docker.com/compose/install/) (incluído no Docker Desktop)
- PowerShell (Windows) ou Shell compatível (Linux/Mac)
- Pelo menos 8GB RAM e 10GB espaço em disco (para modelos AI)

## 🛠️ Como Rodar na Sua Máquina (Após Clone)

### 📥 Passo 1: Clone do Repositório

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/pdf_markdown.git
cd pdf_markdown
```

### 🚀 Passo 2: Execução Rápida (Recomendado)

**Windows (PowerShell):**
```powershell
# Build automático + primeira execução
.\build.ps1 build

# Inicializar modelos (opcional, mas recomendado)
.\build.ps1 init

# Rodar em modo interativo
.\build.ps1 interactive
```

**Linux/Mac:**
```bash
# Build da imagem
docker-compose build

# Executar
docker-compose run --rm pdf-converter
```

### 🎯 Passo 3: Teste Rápido

```powershell
# Coloque um PDF no diretório e execute
.\build.ps1 interactive
# OU
.\build.ps1 run meu-arquivo.pdf
```

### ⚡ Scripts de Automação Disponíveis

O projeto inclui um script PowerShell (`build.ps1`) que facilita todas as operações:

```powershell
# Ver todas as opções disponíveis
.\build.ps1

# Build da imagem (com modelos pré-carregados)
.\build.ps1 build

# Primeira execução (inicializar modelos)
.\build.ps1 init

# Modo interativo (escolher arquivo)
.\build.ps1 interactive

# Conversão direta de um arquivo
.\build.ps1 run documento.pdf

# Ver arquivos de saída gerados
ls .\out\*.md

# Limpeza completa
.\build.ps1 clean
```

### 🐳 Opções de Build Manuais

#### Opção 1: Docker Compose (Recomendado)

```powershell
docker-compose build
```

#### Opção 2: Docker Direto

```powershell
docker build -t pdf-to-markdown .
```

## 🎯 Como Usar

### 🖥️ Modo Interativo (Recomendado)

```powershell
# Usando script PowerShell (mais fácil)
.\build.ps1 interactive

# OU com Docker Compose direto
docker-compose run --rm pdf-converter

# OU com Docker direto
docker run -it --rm -v "${PWD}:/app/pdfs" -v "${PWD}:/app/output" -v "C:\:/host_c" pdf-to-markdown
```

### 📁 Converter Arquivo Específico

```powershell
# Arquivo no diretório atual
.\build.ps1 run documento.pdf

# OU com Docker Compose
docker-compose run --rm pdf-converter documento.pdf

# OU com Docker direto
docker run --rm -v "${PWD}:/app/pdfs" -v "${PWD}:/app/output" -v "C:\:/host_c" pdf-to-markdown documento.pdf
```

### � Arquivos de Saída Organizados (✅ NOVO)

**Todos os arquivos .md são salvos no diretório `/out/`:**

```powershell
# Estrutura após conversão
pdf_markdown/
├── out/
│   ├── .gitkeep              # Mantém estrutura no Git
│   ├── documento1.md         # Arquivo convertido 1
│   ├── documento2.md         # Arquivo convertido 2
│   └── relatorio-sesa.md     # Arquivo convertido 3
├── documento1.pdf            # PDF original (opcional)
└── ...

# Ver todos os arquivos convertidos
ls .\out\*.md

# Abrir arquivo específico
code .\out\documento1.md
```

**Características:**
- ✅ **Separação clara**: Código fonte vs arquivos gerados
- ✅ **Git ignore configurado**: Arquivos .md não vão para o repositório
- ✅ **Estrutura preservada**: `.gitkeep` mantém o diretório /out no Git
- ✅ **Acesso direto**: Arquivos prontos para análise e edição

### �🗂️ Acessar Arquivos Externos

O sistema suporta acesso completo ao sistema de arquivos:

```powershell
# No modo interativo, digite o caminho completo quando solicitado
.\build.ps1 interactive
# Digite: C:\Users\SeuUsuario\Documents\arquivo.pdf

# OU execute diretamente com caminho completo
.\build.ps1 run "C:\Users\SeuUsuario\Documents\arquivo.pdf"
```

### 📚 Exemplos Práticos

#### Exemplo 1: Primeiro Uso (Setup Completo)
```powershell
# 1. Clone e acesse o diretório
git clone https://github.com/seu-usuario/pdf_markdown.git
cd pdf_markdown

# 2. Build com modelos pré-carregados
.\build.ps1 build

# 3. Inicializar (recomendado para primeira execução)
.\build.ps1 init

# 4. Executar modo interativo
.\build.ps1 interactive
```

#### Exemplo 2: Converter Arquivo Local
```powershell
# Colocar o PDF no diretório do projeto
cp "C:\caminho\para\meu-documento.pdf" .

# Executar conversão
.\build.ps1 run meu-documento.pdf
```

#### Exemplo 3: Converter Arquivo Externo (OneDrive, etc.)
```powershell
# Executar modo interativo
.\build.ps1 interactive

# Quando solicitado, digite o caminho completo:
# ➤ C:\Users\SeuUsuario\OneDrive\Documents\relatorio.pdf
```

#### Exemplo 4: Processamento em Lote
```powershell
# Converter múltiplos arquivos no diretório atual
foreach ($pdf in Get-ChildItem *.pdf) {
    .\build.ps1 run $pdf.Name
}

# OU processar de um diretório específico
$arquivos = @(
    "C:\Documentos\arquivo1.pdf",
    "C:\Documentos\arquivo2.pdf"
)
foreach ($arquivo in $arquivos) {
    .\build.ps1 run $arquivo
}
```

#### Exemplo 5: Interface Interativa Típica
```powershell
.\build.ps1 interactive

# Saída esperada:
# ============================================================
# 🚀 CONVERSOR PDF PARA MARKDOWN - DOCLING
# 📄 Conversão dinâmica de arquivos PDF
# ============================================================
# 📋 Modo: Seleção interativa
# 
# 📁 Arquivos PDF encontrados:
#   1. documento1.pdf (2.34 MB)
#   2. documento2.pdf (1.87 MB)
# 🔢 Escolha um arquivo (1-2) ou digite o caminho completo:
```

#### Exemplo 6: Sistema de Fallback em Ação (✅ NOVO)
```powershell
.\build.ps1 interactive

# Quando digite caminho para arquivo externo:
# ➤ C:\Users\usuario\OneDrive\documento-sesa.pdf
# 
# Saída com fallback automático:
# 📄 Arquivo selecionado: documento-sesa.pdf
# 💾 Arquivo de saída: documento-sesa.md
# 🚀 Iniciando conversão...
# 🔧 Inicializando Docling...
# ✅ Docling inicializado com sucesso!
# 📖 Processando PDF com Docling...
# ⚠️  Problema de conectividade durante conversão detectado!
# 🔄 Ativando modo fallback com PyMuPDF...
# ✅ Conversão de fallback concluída!
# 📁 Arquivo salvo em: /app/out/documento-sesa.md
# 💡 Nota: Versão simplificada - para melhor formatação, resolva a conectividade de rede.
# 
# 🎉 Processo finalizado com sucesso!
```

## 📁 Estrutura do Projeto

```
pdf_markdown/
├── 📄 convert_pdf_to_markdown.py  # Script principal de conversão (com fallback resiliente)
├── � preload_models.py           # Script de pré-carregamento de modelos
├── �🐳 Dockerfile                  # Definição da imagem Docker (com pré-carregamento)
├── 🐳 docker-compose.yml          # Configuração Docker Compose
├── 📦 requirements.txt            # Dependências Python (Docling, PyMuPDF, etc.)
├── 🚫 .dockerignore              # Arquivos ignorados no build
├── 🚫 .gitignore                 # Git ignore (inclui out/*.md)
├── ⚡️ build.ps1                   # Script PowerShell de automação
├──  README.md                   # Documentação completa (este arquivo)
├── 🔧 SOLUCAO_PRIMEIRA_EXECUCAO.md # Detalhes técnicos das melhorias
├── � out/                       # Diretório de saída dos arquivos .md
│   ├── .gitkeep                  # Mantém estrutura no Git
│   └── *.md                      # Arquivos Markdown gerados (ignorados pelo Git)
└── 📄 *.pdf                      # Arquivos PDF de entrada (opcional)
```

### 🏗️ Arquitetura da Solução

- **Dockerfile Multi-Stage**: Build otimizado com pré-carregamento de modelos
- **Volume Mapping**: Acesso completo ao sistema de arquivos do host
- **Permission Management**: Execução como root quando necessário
- **Error Handling**: Tratamento robusto de erros com fallbacks automáticos
- **User Experience**: Interface interativa com feedback visual
- **Sistema Resiliente**: Fallback PyMuPDF para ambientes sem conectividade
- **Organização de Arquivos**: Diretório `/out` dedicado com Git ignore configurado
- **Network Detection**: Detecção automática de problemas de conectividade

## 🛡️ Sistema de Fallback Resiliente

### 📡 Funcionamento Automático

O sistema detecta automaticamente problemas de conectividade e ativa o fallback:

```
🔧 Inicializando Docling...
✅ Docling inicializado com sucesso!
📖 Processando PDF com Docling...
⚠️  Problema de conectividade durante conversão detectado!
🔄 Ativando modo fallback com PyMuPDF...
✅ Conversão de fallback concluída!
💡 Nota: Versão simplificada - para melhor formatação, resolva a conectividade de rede.
```

### 🎯 Cenários de Ativação

**Fallback ativado quando:**
- ❌ Firewall corporativo bloqueia Hugging Face Hub
- ❌ Sem conectividade com internet  
- ❌ Modelos do Docling não podem ser baixados
- ❌ Timeouts de rede durante download de modelos

**Docling usado quando:**
- ✅ Conectividade total com Hugging Face Hub
- ✅ Modelos já baixados e disponíveis
- ✅ Rede corporativa permite acesso aos repositórios

### 📊 Qualidade de Conversão

| Método | Qualidade | Características | Uso |
|--------|-----------|----------------|-----|
| **Docling** | ⭐⭐⭐⭐⭐ | OCR avançado, AI, estruturas complexas | Ideal (requer internet) |
| **PyMuPDF** | ⭐⭐⭐ | Extração de texto básica, sempre funciona | Fallback (offline) |

### 🔍 Detecção de Problemas

O sistema detecta erros relacionados a:
- `"Hub"` - Problemas com Hugging Face Hub
- `"internet"` - Conectividade geral
- `"connection"` - Falhas de conexão
- `"snapshot"` - Download de modelos
- `"timeout"` - Timeouts de rede

## ⚙️ Configuração Avançada

### 🎛️ Scripts PowerShell Personalizados

O `build.ps1` oferece opções avançadas:

```powershell
# Ver ajuda completa
.\build.ps1 help

# Build forçado (ignore cache)
.\build.ps1 build --no-cache

# Modo debug (verbose)
.\build.ps1 interactive --debug

# Usar imagem específica
.\build.ps1 run arquivo.pdf --image minha-imagem:tag
```

### 🗂️ Volumes Personalizados

```powershell
# Usar diretórios específicos para entrada e saída
docker run --rm \
  -v "C:\meus-pdfs:/app/pdfs" \
  -v "C:\saida-markdown:/app/output" \
  -v "C:\:/host_c" \
  pdf-to-markdown documento.pdf
```

### 🌐 Variáveis de Ambiente

```powershell
# Configurações personalizadas
docker run --rm \
  -e PYTHONUNBUFFERED=1 \
  -e DOCLING_DEBUG=1 \
  -v "${PWD}:/app/pdfs" \
  -v "${PWD}:/app/output" \
  -v "C:\:/host_c" \
  pdf-to-markdown
```

### 🔧 Modo Desenvolvimento

```powershell
# Executar com código local (desenvolvimento)
docker run --rm -it \
  -v "${PWD}:/app" \
  -v "C:\:/host_c" \
  pdf-to-markdown:latest bash
```

## 🔧 Desenvolvimento

### Executar localmente (sem Docker)

```powershell
# Instalar dependências
pip install -r requirements.txt

# Executar
python convert_pdf_to_markdown.py
```

### Fazer mudanças no código

1. Editar `convert_pdf_to_markdown.py`
2. Fazer rebuild da imagem:
   ```powershell
   docker-compose build
   ```

## 📊 Performance e Características Técnicas

### 🔢 Métricas de Performance
- **Tamanho da imagem**: ~4.5GB (inclui modelos pré-carregados)
- **Tempo de build inicial**: ~15-20 minutos (download de modelos)
- **Builds subsequentes**: ~2-3 minutos (cache do Docker)
- **Primeira execução**: Instantânea (modelos já carregados)
- **Velocidade de conversão**: 
  - Documentos pequenos (1-10 páginas): 30s - 2min
  - Documentos médios (10-50 páginas): 2-15min
  - Documentos grandes (50+ páginas): 15min - 2h
- **Memória**: ~500MB - 2GB (depende da complexidade do PDF)
- **CPU**: Suporta multi-threading, beneficia de múltiplos cores

### ⚡ Otimizações Implementadas
- ✅ **Modelos pré-carregados** no build
- ✅ **Cache de Docker** para builds rápidos
- ✅ **Primeira execução sem downloads**
- ✅ **Volume mapping otimizado** para acesso ao sistema de arquivos
- ✅ **Permissões automáticas** sem intervenção do usuário

## 🐛 Solução de Problemas

### ❌ Erro: "No such file or directory"
```powershell
# Verificar se o arquivo existe
ls *.pdf

# Usar o modo interativo (mais seguro)
.\build.ps1 interactive

# Ou usar caminho completo no Windows
.\build.ps1 run "C:\Users\SeuUsuario\Documents\arquivo.pdf"
```

### ❌ Erro: "Permission denied" (✅ RESOLVIDO)
Este problema foi completamente eliminado nas versões atuais:
```powershell
# Solução automática - executar inicialização
.\build.ps1 init

# Se persistir, rebuild com modelos
.\build.ps1 build
```

### 🔄 Sistema de Fallback Automático (✅ NOVO)
**Problema**: Firewall corporativo bloqueia Hugging Face Hub
**Solução**: Sistema detecta automaticamente e usa PyMuPDF como fallback

```
✅ Sempre funciona, mesmo sem internet!
🔄 Fallback automático transparente
💡 Usuário informado sobre qual método está sendo usado
```

### 📁 Arquivos de Saída (✅ NOVO)
**Localização**: Todos os arquivos .md são salvos em `/out/`
**Organização**: Separados do código fonte
**Git**: Automaticamente ignorados pelo .gitignore

### ❌ Erro: "Docker not found"
```powershell
# Verificar se o Docker está rodando
docker --version
docker-compose --version

# Reiniciar o Docker Desktop se necessário
```

### ❌ Problemas de encoding
```powershell
# O container usa UTF-8 por padrão
# Arquivos de saída sempre em UTF-8
# Se necessário, converter localmente
```

### ❌ Container muito lento
```powershell
# Alocar mais recursos ao Docker Desktop
# Configurações → Resources → Advanced
# RAM: mínimo 4GB, recomendado 8GB
# CPU: mínimo 2 cores, recomendado 4+
```

### ❌ Build falha por timeout
```powershell
# Aumentar timeout do Docker
$env:DOCKER_CLIENT_TIMEOUT="300"
$env:COMPOSE_HTTP_TIMEOUT="300"

# Rebuild
.\build.ps1 build
```

### 🆘 Reset Completo
Se nada funcionar, reset completo:
```powershell
# Limpar tudo
.\build.ps1 clean

# Rebuild do zero
.\build.ps1 build

# Inicializar
.\build.ps1 init
```

## 🚀 Roadmap e Melhorias

### ✅ Implementado
- [x] Conversão PDF → Markdown com Docling
- [x] Interface interativa completa
- [x] Dockerização com modelos pré-carregados
- [x] Acesso a arquivos externos (sistema completo)
- [x] Scripts de automação PowerShell
- [x] Primeira execução sem erros de permissão
- [x] Suporte a caminhos Windows e mapeamento de volumes
- [x] Tratamento robusto de erros com fallbacks automáticos
- [x] **Sistema de fallback resiliente** (PyMuPDF quando Docling falha)
- [x] **Diretório /out organizado** com Git ignore configurado
- [x] **Detecção automática de conectividade** e ativação de fallback
- [x] **Compatibilidade com ambientes corporativos** (firewall-friendly)
- [x] **Modelos RapidOCR pré-carregados** (sem downloads na execução)

### 🔮 Próximas Features
- [ ] Interface web (gradio/streamlit)
- [ ] Suporte a múltiplos formatos de saída (HTML, DOCX)
- [ ] API REST para integração
- [ ] Processamento em paralelo (batch)
- [ ] Configurações avançadas de OCR
- [ ] Suporte a idiomas específicos
- [ ] Integração com cloud storage (Google Drive, OneDrive API)

### 🎯 Contribuições

Contribuições são muito bem-vindas! 

**Como contribuir:**
1. 🍴 Fork o projeto
2. 🌿 Crie uma branch: `git checkout -b minha-feature`
3. ✅ Commit suas mudanças: `git commit -m 'Add: nova feature'`
4. 📤 Push: `git push origin minha-feature`
5. 🔄 Abra um Pull Request

**Áreas que precisam de ajuda:**
- 🐧 Scripts para Linux/Mac (equivalentes ao build.ps1)
- 🌐 Interface web
- 📚 Mais exemplos e documentação
- 🧪 Testes automatizados
- 🔧 Otimizações de performance

## 📞 Suporte e Comunidade

### 🆘 Onde Buscar Ajuda
1. **README.md** - Documentação completa (este arquivo)
2. **Issues do GitHub** - Para bugs e feature requests
3. **Discussões do GitHub** - Para perguntas gerais
4. **[Documentação do Docling](https://github.com/DS4SD/docling)** - Para detalhes técnicos

### 🐛 Reportar Bugs
Ao reportar bugs, inclua:
- Sistema operacional e versão
- Versão do Docker
- Comando executado
- Mensagem de erro completa
- Arquivo PDF de exemplo (se possível)

### 💡 Sugerir Melhorias
- Use GitHub Issues com label "enhancement"
- Descreva o caso de uso
- Propose a solução se tiver ideias

---

## 🙏 Agradecimentos

- **[Docling Team](https://github.com/DS4SD/docling)** - Pela excelente biblioteca de conversão PDF
- **Docker Community** - Pela plataforma de containerização
- **Python Community** - Pelas ferramentas e bibliotecas
