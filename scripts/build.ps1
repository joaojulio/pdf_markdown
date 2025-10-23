# Script PowerShell para PDF to Markdown Converter
param(
    [string]$Command = "help",
    [string]$PdfFile = "",
    [switch]$Force
)

$ImageName = "pdf-to-markdown"

function Show-Help {
    Write-Host "============================================================" -ForegroundColor Cyan
    Write-Host "PDF TO MARKDOWN CONVERTER - DOCKER" -ForegroundColor Green  
    Write-Host "============================================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "COMANDOS DISPONIVEIS:" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "BUILD:" -ForegroundColor Green
    Write-Host "  .\build.ps1 build                    # Fazer build da imagem"
    Write-Host ""
    Write-Host "EXECUCAO:" -ForegroundColor Green
    Write-Host "  .\build.ps1 interactive              # Modo interativo"
    Write-Host "  .\build.ps1 run arquivo.pdf          # Converter arquivo"
    Write-Host "  .\build.ps1 init                     # Primeira execucao (baixar modelos)"
    Write-Host ""
    Write-Host "MANUTENCAO:" -ForegroundColor Green
    Write-Host "  .\build.ps1 clean                    # Limpar containers"
    Write-Host ""
    Write-Host "EXEMPLOS:" -ForegroundColor Yellow
    Write-Host "  .\build.ps1 build"
    Write-Host "  .\build.ps1 interactive"
    Write-Host "  .\build.ps1 run documento.pdf"
    Write-Host ""
}

switch ($Command.ToLower()) {
    "build" {
        Write-Host "Fazendo build da imagem Docker..." -ForegroundColor Yellow
        $RootDir = Split-Path $PSScriptRoot -Parent
        $DockerDir = Join-Path $RootDir "docker"
        
        if (Test-Path "$DockerDir/docker-compose.yml") {
            Set-Location $DockerDir
            docker-compose build
            Set-Location $PSScriptRoot
        } else {
            Set-Location $DockerDir
            docker build -t $ImageName .
            Set-Location $PSScriptRoot
        }
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Build concluido com sucesso!" -ForegroundColor Green
        } else {
            Write-Host "Erro durante o build!" -ForegroundColor Red
        }
    }
    
    "interactive" {
        Write-Host "Executando modo interativo..." -ForegroundColor Yellow
        $RootDir = Split-Path $PSScriptRoot -Parent
        $DockerDir = Join-Path $RootDir "docker"
        
        if (Test-Path "$DockerDir/docker-compose.yml") {
            Set-Location $DockerDir
            docker-compose run --rm --user root pdf-converter
            Set-Location $PSScriptRoot
        } else {
            docker run -it --rm --user root -v "${RootDir}:/app/pdfs" -v "${RootDir}/out:/app/out" $ImageName
        }
    }
    
    "run" {
        if ([string]::IsNullOrEmpty($PdfFile)) {
            Write-Host "Especifique o arquivo PDF!" -ForegroundColor Red
            Write-Host "Uso: .\build.ps1 run arquivo.pdf" -ForegroundColor Yellow
            return
        }
        
        Write-Host "Convertendo arquivo: $PdfFile" -ForegroundColor Yellow
        $RootDir = Split-Path $PSScriptRoot -Parent
        $DockerDir = Join-Path $RootDir "docker"
        
        if (Test-Path "$DockerDir/docker-compose.yml") {
            Set-Location $DockerDir
            docker-compose run --rm --user root pdf-converter $PdfFile
            Set-Location $PSScriptRoot
        } else {
            docker run --rm --user root -v "${RootDir}:/app/pdfs" -v "${RootDir}/out:/app/out" $ImageName "/app/pdfs/$PdfFile"
        }
    }
    
    "init" {
        Write-Host "Inicializando modelos do Docling (primeira execucao)..." -ForegroundColor Yellow
        $RootDir = Split-Path $PSScriptRoot -Parent
        $DockerDir = Join-Path $RootDir "docker"
        
        if (Test-Path "$DockerDir/docker-compose.yml") {
            Set-Location $DockerDir
            docker-compose run --rm --user root pdf-converter python -c "from docling.document_converter import DocumentConverter; DocumentConverter(); print('Modelos inicializados com sucesso!')"
            Set-Location $PSScriptRoot
        } else {
            docker run --rm --user root -v "${RootDir}:/app/pdfs" -v "${RootDir}/out:/app/out" $ImageName python -c "from docling.document_converter import DocumentConverter; DocumentConverter(); print('Modelos inicializados com sucesso!')"
        }
        Write-Host "Inicializacao concluida! Agora voce pode usar os outros comandos." -ForegroundColor Green
    }
    
    "clean" {
        Write-Host "Limpando recursos Docker..." -ForegroundColor Yellow
        docker system prune -f
        if ($Force) {
            docker rmi $ImageName -f 2>$null
        }
        Write-Host "Limpeza concluida!" -ForegroundColor Green
    }
    
    default {
        Show-Help
    }
}