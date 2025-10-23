# Script PowerShell para PDF to Markdown Converter - Ponto de Entrada Principal
param(
    [string]$Command = "help",
    [string]$PdfFile = "",
    [switch]$Force
)

# Redirecionar para o script real na pasta scripts
$ScriptPath = Join-Path $PSScriptRoot "scripts\build.ps1"

if (Test-Path $ScriptPath) {
    & $ScriptPath $Command $PdfFile -Force:$Force
} else {
    Write-Host "Script nao encontrado em: $ScriptPath" -ForegroundColor Red
    Write-Host "Estrutura do projeto pode estar incorreta." -ForegroundColor Yellow
}