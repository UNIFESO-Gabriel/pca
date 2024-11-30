import shutil
from os import stat_result
from pathlib import Path
from datetime import datetime


EXTENSAO = ".txt"


def main() -> None:
    print("=== MANIPULAÇÃO DE CAMINHOS ===")
    caminho_atual = Path.cwd()
    print(f"Caminho atual do projeto: {caminho_atual}")
    
    home = Path.home()
    print(f"Caminho da pasta home: {home}")
    
    # Criando um novo caminho de exemplo
    arquivo = Path("exemplo.txt")
    # Criando uma nova pasta e arquivo de exemplos
    caminho_arquivo_pdf = Path("dados/documentos/arquivo.pdf")
    
    print(f"Caminho do arquivo: {arquivo}")
    print(f"Caminho da subpasta: {caminho_arquivo_pdf}")
    print(f"Arquivo sem a extensão: {arquivo.stem}")
    print(f"Somente a extensão do arquivo: {arquivo.suffix}")
    
    print("Pasta pai do arquivo PDF: ", caminho_arquivo_pdf.parent)
    print("Caminhos do arquivo PDF: ", caminho_arquivo_pdf.parts[:-1])
    
    print("\n=== OPERAÇÕES COM ARQUIVOS E DIRETÓRIOS ===\n")
    
    # Criando uma pasta de teste.
    nova_pasta: Path = Path(Path.cwd() / "nova_pasta")
    
    if not nova_pasta.exists():
        nova_pasta.mkdir()
        print("Pasta criada com sucesso!")
    else:
        print("A pasta já existe!")
    
    # Criando um arquivo de teste.
    arquivo_teste: Path = Path(nova_pasta / "teste.txt")
    
    if not arquivo_teste.exists():    
        arquivo_teste.touch()
        arquivo_teste.write_text("Olá, mundo!")
        print("Arquivo criado com sucesso!")
    else:
        # incluir novo texto no arquivo, mantendo o conteúdo anterior
        arquivo_teste.write_text(f"Olá, mundo!\nNovo texto escrito no arquivo em {datetime.now()}!")
        print("Arquivo modificado!")
        
    # Lendo o conteúdo do arquivo
    conteudo_arquivo: str = arquivo_teste.read_text()
    print(f"Conteúdo do arquivo: {conteudo_arquivo}")
    
    # Obternedo informações do arquivo.
    print(f"Nome do arquivo: {arquivo_teste.name}")
    stats: stat_result = arquivo_teste.stat()
    print(f"Tamanho do arquivo: {stats.st_size} bytes.")
    print(f"Data de criação: {datetime.fromtimestamp(stats.st_ctime)}")
    print(f"Data de modificação: {datetime.fromtimestamp(stats.st_mtime)}")
    
    # Listar arquivos e pastas de um diretório.
    print("\n=== LISTANDO ARQUIVOS E PASTAS ===\n")
    for item in Path.cwd().iterdir():
        tipo = "Pasta" if item.is_dir() else "Arquivo"
        print(f"{tipo}: {item.name}")
        
    # Pegar o caminho absoluto de um arquivo.
    print(f"Caminho absoluto do arquivo teste.txt: {arquivo_teste.resolve()}")
    
    # Listar arquivos de um diretório com uma extensão específica.
    print(f"\n=== LISTANDO ARQUIVOS COM EXTENSÃO {EXTENSAO.upper()} ===\n")
    print(f"Arquivos encontrados: {[arquivo.name for arquivo in Path.cwd().glob(f'**/*{EXTENSAO}')]}")
    
    # Removendo os arquivos e pastas criados.
    # if arquivo_teste.exists():
    #     arquivo_teste.unlink() # remove o arquivo.
    if nova_pasta.exists():
        try:
            nova_pasta.rmdir() # remove a pasta se estiver vazia.
        except OSError:
            shutil.rmtree(nova_pasta) # se tiver algo, removo tudo, inclusive a propria pasta.
        finally:
            print("Arquivo e pasta removidos com sucesso!") # por fim, imprimo a mensagem.
    else:
        print("Os arquivos e pasta não existem.")
    
if __name__ == "__main__":
    main()