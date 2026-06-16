import glob
import os
import re
import numpy as np

# --- CONFIGURAÇÕES ---
diretorio_dados = os.getcwd()
diretorio_formated = os.path.join(diretorio_dados, "formated")
diretorio_treated = os.path.join(diretorio_dados, "treated")

# Garante que a pasta "treated" exista
os.makedirs(diretorio_treated, exist_ok=True)

# Buscar todos os arquivos .dat na pasta formated
caminho_busca = os.path.join(diretorio_formated, "*.dat")
arquivos = glob.glob(caminho_busca)

# Dicionário para agrupar e decidir qual arquivo usar para cada "nome base"
arquivos_selecionados = {}

# REGEX ATUALIZADA:
# (T\d{3})  -> Captura "T" seguido de 3 dígitos
# (U\d+\.?\d*) -> Captura "U" seguido de um ou mais dígitos, permitindo pontos e decimais (ex: U1, U05, U1.5)
# ([bB])?   -> Captura a letra B (maiúscula ou minúscula) de forma opcional no final
padrao_nome = re.compile(r"(T\d{3}U\d+\.?\d*)([bB])?\.dat")

# 1. Triagem: Decidir qual arquivo manter (prioridade para o terminado em 'b' / 'B')
for caminho_completo in arquivos:
    nome_arquivo = os.path.basename(caminho_completo)
    match = padrao_nome.match(nome_arquivo)

    if match:
        nome_base = match.group(1)  # Ex: "T160U05" ou "T160U1"
        sufixo_b = match.group(2)  # Será "b", "B" ou None

        if nome_base not in arquivos_selecionados:
            arquivos_selecionados[nome_base] = caminho_completo
        else:
            # Se o arquivo atual do loop possui o 'B' no final, ele substitui o anterior
            if sufixo_b is not None:
                arquivos_selecionados[nome_base] = caminho_completo

# 2. Processar, modificar dados e inverter as colunas
for nome_base, caminho in arquivos_selecionados.items():
    nome_arquivo_original = os.path.basename(caminho)
    print(f"Processando: {nome_arquivo_original} -> Salvando como: {nome_base}.dat")

    try:
        # Ler os dados do arquivo escolhido
        dados = np.loadtxt(caminho)
        if dados.ndim == 1:
            dados = np.array([dados])

        # Isolar as colunas originais (0: primeira, 1: segunda, 2: terceira)
        antiga_col2 = dados[:, 1]
        antiga_col3 = dados[:, 2]

        # Aplicar valor absoluto na antiga segunda coluna
        antiga_col2_absoluto = np.abs(antiga_col2)

        # Montar a nova estrutura com 2 colunas e invertidas:
        # Nova coluna 1 (índice 0) = antiga_col3
        # Nova coluna 2 (índice 1) = antiga_col2 (em módulo)
        dados_finais = np.column_stack((2*antiga_col3, antiga_col2_absoluto))

        # Definir o caminho de saída na pasta "treated"
        nome_saida = f"{nome_base}.dat"
        caminho_saida = os.path.join(diretorio_treated, nome_saida)

        # Salvar o arquivo tratado com as colunas reorganizadas
        np.savetxt(caminho_saida, dados_finais, fmt="%f", delimiter="\t")

    except Exception as e:
        print(f"  -> Erro ao processar o arquivo {nome_arquivo_original}: {e}")

print("\nProcessamento de formated -> treated concluído com sucesso!")
