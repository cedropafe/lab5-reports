import glob
import os
import numpy as np


def suavizar_curva(dados_y, janela=5):
    """Suaviza os dados usando uma média móvel."""
    if len(dados_y) < janela:
        return dados_y  # Não suaviza se os dados forem menores que a janela
    box = np.ones(janela) / janela
    return np.convolve(dados_y, box, mode="same")


# --- CONFIGURAÇÕES ---
JANELA_SUAVIZACAO = 5  # Ajuste para mais (ex: 7) ou menos (ex: 3) suavização
diretorio_dados = os.getcwd()
diretorio_treated = os.path.join(diretorio_dados, "treated")

# Buscar todos os arquivos .dat na pasta treated
caminho_busca = os.path.join(diretorio_treated, "*.dat")
arquivos = glob.glob(caminho_busca)

if not arquivos:
    print(
        f"Nenhum arquivo .dat encontrado em: {diretorio_treated}. Execute o script de inversão primeiro!"
    )

# Processar cada arquivo de 2 colunas na pasta treated
for caminho_completo in arquivos:
    nome_arquivo = os.path.basename(caminho_completo)

    try:
        # 1. Ler os dados do arquivo (que agora possui apenas 2 colunas)
        dados = np.loadtxt(caminho_completo)
        if dados.ndim == 1:
            dados = np.array([dados])

        if dados.size == 0:
            print(f"Arquivo vazio ou inválido: {nome_arquivo}")
            continue

        # Mapeamento atual das colunas:
        # dados[:, 0] -> Eixo X (Antiga 3ª coluna)
        # dados[:, 1] -> Eixo Y (Antiga 2ª coluna com valor absoluto)

        # 2. Filtrar as linhas: REMOVER pontos onde a atual segunda coluna (índice 1) é MAIOR que 6.5
        # Ou seja, vamos MANTER apenas onde for menor ou igual a 6.5
        mascara_filtro = dados[:, 1] <= 7
        dados_filtrados = dados[mascara_filtro]

        if dados_filtrados.size == 0:
            print(
                f"Aviso: O arquivo {nome_arquivo} não possui dados com a segunda coluna <= 6.5. Pulado."
            )
            continue

        col_x = dados_filtrados[:, 0]
        col_y = dados_filtrados[:, 1]

        # 3. Ordenar os dados com base na primeira coluna (Eixo X)
        # Garante a sequência correta de pontos antes da suavização
        idx_ordenado = np.argsort(col_x)
        col_x_ordenada = col_x[idx_ordenado]
        col_y_ordenada = col_y[idx_ordenado]

        # 4. Suavizar a atual segunda coluna (Eixo Y)
        col_y_suavizada = suavizar_curva(
            col_y_ordenada, janela=JANELA_SUAVIZACAO
        )

        # Reestruturar as 2 colunas mantendo a nova ordem (X, Y_suavizado)
        dados_finais = np.column_stack((col_x_ordenada, col_y_suavizada))

        # 5. Salvar de volta na pasta "treated"
        np.savetxt(caminho_completo, dados_finais, fmt="%f", delimiter="\t")
        print(f"Filtrado (<= 6.5) e suavizado com sucesso: {nome_arquivo}")

    except Exception as e:
        print(f"Erro ao processar o arquivo {nome_arquivo}: {e}")

print("\nFiltragem e suavização concluídas!")
