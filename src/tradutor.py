# -*- coding: utf-8 -*-
import sys
import re

def traduzir_mengaolang_para_python(codigo_mng):
    """
    Traduz uma string contendo código MengãoLang para código Python.
    Mantém o controle da indentação para blocos de código.
    """
    linhas_python = []
    indentacao_nivel = 0
    indentacao_str = "    " # 4 espaços por nível

    # Dicionário de substituições diretas e simples
    comandos_simples = {
        r'\bfla é campeão\b': 'def main():',
        r'\bfla fim\b': 'if __name__ == "__main__":\n    main()',
    }

    linhas_mng = codigo_mng.split('\n')
    bloco_aberto = False

    for i, linha in enumerate(linhas_mng):
        linha_strip = linha.strip()
        
        # Ignora linhas em branco
        if not linha_strip:
            linhas_python.append("")
            continue

        linha_traduzida = None
        
        # Dedentação: se a linha atual tem menos indentação que a anterior,
        # e um bloco estava aberto, diminui o nível.
        # Esta é uma lógica simples para linguagens sem marcadores de fim de bloco.
        if i > 0 and bloco_aberto:
            indentacao_anterior = len(linhas_mng[i-1]) - len(linhas_mng[i-1].lstrip(' '))
            indentacao_atual = len(linha) - len(linha.lstrip(' '))
            if indentacao_atual < indentacao_anterior:
                indentacao_nivel = max(0, indentacao_nivel - 1)
                bloco_aberto = False


        prefixo_indentacao = indentacao_str * indentacao_nivel

        # --- Regras de Tradução com Regex ---

        # 0. Início e Fim do programa
        if re.search(r'\bfla é campeão\b', linha_strip):
            linhas_python.append(comandos_simples[r'\bfla é campeão\b'])
            indentacao_nivel += 1
            continue
        if re.search(r'\bfla fim\b', linha_strip):
            indentacao_nivel = 0 # Reseta a indentação para o bloco final
            linhas_python.append(comandos_simples[r'\bfla fim\b'])
            continue

        # 1. Atribuição de variável: <var> é <tipo> <valor>
        match = re.match(r'^(.*?)\s+é\s+(craque|torcida|camisa10)\s+(.*)', linha_strip)
        if match:
            var_name, var_type, value = match.groups()
            var_name = var_name.strip()
            
            if "torcida canta" in value:
                # Entrada de dados
                if var_type == "craque":
                    linha_traduzida = f'{var_name} = int(input())'
                else: # Assume string para outros tipos
                    linha_traduzida = f'{var_name} = input()'
            else:
                # Atribuição normal
                if var_type == "craque":
                    linha_traduzida = f'{var_name} = int({value})'
                elif var_type == "torcida":
                    linha_traduzida = f'{var_name} = {value}'
                elif var_type == "camisa10":
                    py_value = "True" if value.lower() == "verdadeiro" else "False"
                    linha_traduzida = f'{var_name} = {py_value}'
        
        # 2. Imprimir: fla imprime <coisa>
        if not linha_traduzida:
            match = re.match(r'fla imprime\s+(.*)', linha_strip)
            if match:
                value_to_print = match.group(1)
                linha_traduzida = f'print({value_to_print})'

        # 3. Condicional: arrasca se <condicao>
        if not linha_traduzida:
            match = re.match(r'arrasca se\s+(.*)', linha_strip)
            if match:
                condition = match.group(1)
                linha_traduzida = f'if {condition}:'
                indentacao_nivel += 1
                bloco_aberto = True

        # 4. Loop While: jogo tenso <condicao>
        if not linha_traduzida:
            match = re.match(r'jogo tenso\s+(.*)', linha_strip)
            if match:
                condition = match.group(1)
                linha_traduzida = f'while {condition}:'
                indentacao_nivel += 1
                bloco_aberto = True
        
        # 5. Incremento: gol <var>
        if not linha_traduzida:
            match = re.match(r'gol\s+(.*)', linha_strip)
            if match:
                var_name = match.group(1).strip()
                linha_traduzida = f'{var_name} += 1'
        
        # 6. Decremento: vai pra cima <var>
        if not linha_traduzida:
            match = re.match(r'vai pra cima\s+(.*)', linha_strip)
            if match:
                var_name = match.group(1).strip()
                linha_traduzida = f'{var_name} -= 1'

        if linha_traduzida is None:
            linha_traduzida = f'# Erro de sintaxe: Linha não reconhecida -> {linha_strip}'

        linhas_python.append(prefixo_indentacao + linha_traduzida)

    return '\n'.join(linhas_python)

def main():
    """
    Função principal para executar o tradutor a partir da linha de comando.
    """
    if len(sys.argv) != 3:
        print("Uso: python tradutor.py <arquivo_entrada.mng> <arquivo_saida.py>")
        sys.exit(1)

    arquivo_entrada = sys.argv[1]
    arquivo_saida = sys.argv[2]

    try:
        with open(arquivo_entrada, 'r', encoding='utf-8') as f:
            codigo_mng = f.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo de entrada '{arquivo_entrada}' não encontrado.")
        sys.exit(1)

    codigo_py = traduzir_mengaolang_para_python(codigo_mng)

    with open(arquivo_saida, 'w', encoding='utf-8') as f:
        f.write(codigo_py)

    print(f"✔️ Tradução concluída com sucesso! Arquivo '{arquivo_saida}' gerado.")

if __name__ == "__main__":
    main()
