"""
Script para converter PDF para Markdown usando Docling
Suporte para conversão dinâmica de arquivos PDF
"""

import os
import sys
import argparse
from pathlib import Path
from docling.document_converter import DocumentConverter

def get_pdf_file_interactive():
    """
    Permite ao usuário escolher um arquivo PDF interativamente
    """
    current_dir = Path(__file__).parent
    
    # Listar todos os arquivos PDF no diretório atual
    pdf_files = list(current_dir.glob("*.pdf"))
    
    if pdf_files:
        print("\n📁 Arquivos PDF encontrados:")
        for i, pdf_file in enumerate(pdf_files, 1):
            size_mb = pdf_file.stat().st_size / (1024 * 1024)
            print(f"  {i}. {pdf_file.name} ({size_mb:.2f} MB)")
        print(f"\n🔢 Escolha um arquivo (1-{len(pdf_files)}) ou digite o caminho completo:")
    else:
        print("\n❌ Nenhum arquivo PDF encontrado no diretório atual.")
        print("💡 Digite o caminho completo para o arquivo PDF:")
    
    while True:
        try:
            choice = input("➤ ").strip()
            
            if not choice:
                print("❌ Por favor, digite uma opção válida.")
                continue
            
            # Verificar se é um número (apenas se há arquivos PDF listados)
            if pdf_files and choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(pdf_files):
                    return pdf_files[index]
                else:
                    print(f"❌ Número inválido. Escolha entre 1 e {len(pdf_files)}.")
                    continue
            
            # Verificar se é um caminho de arquivo
            # Converter caminho do Windows para caminho do container se necessário
            pdf_path = convert_windows_path_to_container(choice)
            
            if pdf_path.exists() and pdf_path.suffix.lower() == '.pdf':
                return pdf_path
            elif pdf_path.exists():
                print("❌ O arquivo especificado não é um PDF.")
                continue
            else:
                # Tentar também o caminho original (caso já esteja no formato correto)
                original_path = Path(choice)
                if original_path.exists() and original_path.suffix.lower() == '.pdf':
                    return original_path
                
                print(f"❌ Arquivo não encontrado: {choice}")
                print("💡 Verifique se o caminho está correto e se o arquivo existe.")
                continue
                
        except KeyboardInterrupt:
            print("\n\n❌ Operação cancelada pelo usuário.")
            return None
        except Exception as e:
            print(f"❌ Erro: {e}")
            continue

def convert_pdf_fallback(pdf_file, output_file):
    """
    Conversão de fallback usando PyMuPDF quando Docling não funciona
    """
    try:
        print("🔄 Usando modo de fallback (PyMuPDF)...")
        import fitz  # PyMuPDF
        
        # Abrir PDF
        doc = fitz.open(pdf_file)
        
        # Extrair texto de todas as páginas
        markdown_lines = []
        markdown_lines.append(f"# {pdf_file.stem}\n\n")
        
        for page_num in range(doc.page_count):
            page = doc[page_num]
            text = page.get_text()
            
            if text.strip():
                markdown_lines.append(f"## Página {page_num + 1}\n\n")
                # Converter texto simples para markdown básico
                lines = text.split('\n')
                for line in lines:
                    line = line.strip()
                    if line:
                        markdown_lines.append(f"{line}\n")
                markdown_lines.append("\n")
        
        doc.close()
        
        # Salvar arquivo markdown
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(markdown_lines)
        
        print(f"✅ Conversão de fallback concluída!")
        print(f"📁 Arquivo salvo em: {output_file}")
        print("💡 Nota: Versão simplificada - para melhor formatação, resolva a conectividade de rede.")
        return True
        
    except Exception as e:
        print(f"❌ Erro no fallback: {e}")
        return False

def convert_windows_path_to_container(windows_path):
    """
    Converte um caminho do Windows para o caminho correspondente no container
    """
    windows_path = windows_path.strip('"\'')  # Remove aspas se houver
    
    # Se é um caminho absoluto do Windows (C:\...)
    if len(windows_path) >= 3 and windows_path[1:3] == ':\\':
        # Converter C:\caminho\arquivo.pdf para /host_c/caminho/arquivo.pdf
        drive_letter = windows_path[0].lower()
        path_without_drive = windows_path[3:].replace('\\', '/')
        container_path = f"/host_{drive_letter}/{path_without_drive}"
        return Path(container_path)
    
    # Se é um caminho relativo ou já está no formato Unix
    return Path(windows_path)

def convert_pdf_to_markdown(pdf_file_path=None):
    """
    Converte um arquivo PDF para formato Markdown
    
    Args:
        pdf_file_path (str|Path, optional): Caminho para o arquivo PDF. 
                                           Se None, será solicitado interativamente.
    """
    # Determinar o arquivo PDF a ser convertido
    if pdf_file_path:
        # Converter caminho do Windows para container se necessário
        pdf_file = convert_windows_path_to_container(str(pdf_file_path))
    else:
        pdf_file = get_pdf_file_interactive()
        if pdf_file is None:
            return False
    
    # Verificar se o arquivo PDF existe
    if not pdf_file.exists():
        print(f"❌ Erro: Arquivo PDF não encontrado em {pdf_file}")
        return False
    
    # Definir arquivo de saída (pasta /out mapeada)
    output_file = Path("/app/out") / f"{pdf_file.stem}.md"
    
    print(f"📄 Arquivo selecionado: {pdf_file.name}")
    print(f"💾 Arquivo de saída: {output_file.name}")
    print(f"🚀 Iniciando conversão...")
    
    try:
        # Inicializar o converter do Docling
        print("🔧 Inicializando Docling...")
        try:
            # Configurar timeout mais baixo para detectar problemas de rede rapidamente
            import os
            os.environ['HF_HUB_OFFLINE'] = '1'  # Forçar modo offline
            
            converter = DocumentConverter()
            print("✅ Docling inicializado com sucesso!")
        except Exception as init_error:
            error_msg = str(init_error)
            
            if "Permission denied" in error_msg:
                print("⚠️  Primeira execução detectada - baixando modelos necessários...")
                print("💡 Isso pode levar alguns minutos na primeira vez.")
                # Tentar novamente após alguns segundos
                import time
                time.sleep(2)
                converter = DocumentConverter()
                print("✅ Modelos baixados e Docling inicializado!")
            elif "Hub" in error_msg or "internet" in error_msg.lower() or "connection" in error_msg.lower():
                print("⚠️  Problema de conectividade detectado!")
                print("🔄 Tentando modo offline/simplificado...")
                
                # Remover modo offline e tentar versão mais simples
                del os.environ['HF_HUB_OFFLINE']
                
                # Fallback para PyMuPDF se disponível
                try:
                    return convert_pdf_fallback(pdf_file, output_file)
                except Exception:
                    print("❌ Modo fallback também falhou.")
                    raise init_error
            else:
                raise init_error
        
        # Converter o PDF
        print("📖 Processando PDF com Docling...")
        try:
            result = converter.convert(pdf_file)
            
            # Exportar para Markdown
            print("📝 Exportando para Markdown...")
            markdown_content = result.document.export_to_markdown()
            
            # Salvar arquivo Markdown
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            print(f"✅ Conversão concluída com sucesso!")
            print(f"📄 Arquivo Markdown salvo como: {output_file.name}")
            print(f"📊 Tamanho do arquivo: {output_file.stat().st_size} bytes")
            
            return True
            
        except Exception as convert_error:
            error_msg = str(convert_error)
            
            if "Hub" in error_msg or "internet" in error_msg.lower() or "connection" in error_msg.lower() or "snapshot" in error_msg.lower():
                print("⚠️  Problema de conectividade durante conversão detectado!")
                print("🔄 Ativando modo fallback com PyMuPDF...")
                
                # Fallback para PyMuPDF
                try:
                    return convert_pdf_fallback(pdf_file, output_file)
                except Exception as fallback_error:
                    print(f"❌ Modo fallback falhou: {fallback_error}")
                    raise convert_error
            else:
                raise convert_error
        
    except Exception as e:
        error_msg = str(e)
        if "Permission denied" in error_msg:
            print("❌ Erro de permissão detectado.")
            print("💡 Solução: Execute o container com privilégios elevados:")
            print("   docker-compose run --user root pdf-converter")
        else:
            print(f"❌ Erro durante a conversão: {error_msg}")
        return False

def main():
    """
    Função principal com suporte a argumentos de linha de comando
    """
    parser = argparse.ArgumentParser(
        description="Converte arquivos PDF para Markdown usando Docling",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  python convert_pdf_to_markdown.py                           # Modo interativo
  python convert_pdf_to_markdown.py arquivo.pdf               # Converter arquivo específico
  python convert_pdf_to_markdown.py /caminho/para/arquivo.pdf  # Caminho completo
        """
    )
    
    parser.add_argument(
        'pdf_file', 
        nargs='?', 
        help='Caminho para o arquivo PDF a ser convertido (opcional - modo interativo se não fornecido)'
    )
    
    parser.add_argument(
        '--output', '-o',
        help='Caminho de saída para o arquivo Markdown (opcional)'
    )
    
    args = parser.parse_args()
    
    print("="*60)
    print("🚀 CONVERSOR PDF PARA MARKDOWN - DOCLING")
    print("� Conversão dinâmica de arquivos PDF")
    print("="*60)
    
    # Determinar o arquivo PDF
    pdf_file_path = args.pdf_file
    
    if pdf_file_path:
        print(f"📋 Modo: Arquivo especificado ({pdf_file_path})")
    else:
        print("📋 Modo: Seleção interativa")
    
    success = convert_pdf_to_markdown(pdf_file_path)
    
    if success:
        print("\n🎉 Processo finalizado com sucesso!")
        print("💡 O arquivo Markdown está pronto para análise.")
    else:
        print("\n⚠️  Processo finalizado com erros.")
        print("🔍 Verifique os logs acima para mais detalhes.")

if __name__ == "__main__":
    main()