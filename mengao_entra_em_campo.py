import os
from src.tradutor import traduzir_mengaolang_para_python

ENTRADA_DIR = "examples"
EXT_MENGAO = ".mng"
EXT_PYTHON = ".py"

def traduz_todos_os_arquivos():
    arquivos = [f for f in os.listdir(ENTRADA_DIR) if f.endswith(EXT_MENGAO)]
    
    if not arquivos:
        print("# Nenhum arquivo .mng encontrado na pasta 'examples'.")
        return

    for arquivo_mng in arquivos:
        caminho_mng = os.path.join(ENTRADA_DIR, arquivo_mng)
        nome_base = os.path.splitext(arquivo_mng)[0]
        caminho_py = os.path.join(ENTRADA_DIR, nome_base + EXT_PYTHON)

        try:
            with open(caminho_mng, 'r', encoding='utf-8') as f:
                codigo_mng = f.read()
        except FileNotFoundError:
            print(f"# Erro: Não foi possível abrir {arquivo_mng}")
            continue

        codigo_py = traduzir_mengaolang_para_python(codigo_mng)

        with open(caminho_py, 'w', encoding='utf-8') as f:
            f.write(codigo_py)

        print(f"# {arquivo_mng} traduzido para {nome_base + EXT_PYTHON}")

if __name__ == "__main__":
    traduz_todos_os_arquivos()
