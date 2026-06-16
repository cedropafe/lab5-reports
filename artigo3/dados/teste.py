import glob
import re
import os
import matplotlib.pyplot as plt
import numpy as np

# 1. Definir os caminhos dos diretórios relativos ao local do script (diretório "dados")
diretorio_dados = os.getcwd()  # Onde o script está executando ("dados")
diretorio_formated = os.path.join(diretorio_dados, "treated")  # Subdiretório "formated"

# Buscar os arquivos dentro da pasta "formated" que seguem o padrão T???U?.dat
# O caminho completo ficará algo como: dados/formated/T160U2.dat
caminho_busca = os.path.join(diretorio_formated, "T[0-9][0-9][0-9]U[0-9].dat")
arquivos = glob.glob(caminho_busca)

# Criar a figura com dois subplots (1 linha, 2 colunas)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Expressão regular para extrair os números do padrão T(3 dígitos) e U(1 dígito)
padrao_nome = re.compile(r"T(\d{3})U(\d)\.dat")

# 2. Processar cada arquivo encontrado
for caminho_arquivo in arquivos:
    # os.path.basename extrai apenas o nome do arquivo (ex: "T160U2.dat") descartando as pastas do caminho
    nome_arquivo = os.path.basename(caminho_arquivo)

    match = padrao_nome.match(nome_arquivo)
    if match:
        num_T = match.group(1)  # Os 3 dígitos após o T
        num_U = match.group(2)  # O dígito após o U

        try:
            # Carrega os dados usando o caminho completo do arquivo
            dados = np.loadtxt(caminho_arquivo)

            if dados.ndim == 1:
                dados = np.array([dados])

            segunda_coluna = dados[:, 1]
            terceira_coluna = dados[:, 2]

            # SUBPLOT 1: Arquivos que terminam com U2.dat
            if nome_arquivo.endswith("U2.dat"):
                ax1.plot(terceira_coluna, segunda_coluna, label=f"T = {num_T} °C")

            # SUBPLOT 2: Arquivos que começam com T160
            if nome_arquivo.startswith("T160"):
                ax2.plot(terceira_coluna, segunda_coluna, label=f"U = {num_U} V")

        except Exception as e:
            print(f"Erro ao ler o arquivo {nome_arquivo}: {e}")

# 3. Configurações de layout e exibição do Subplot 1
ax1.set_title("Arquivos terminados em U2")
ax1.set_xlabel("Terceira Coluna")
ax1.set_ylabel("Segunda Coluna")
ax1.grid(True)
handles1, labels1 = ax1.get_legend_handles_labels()
if labels1:
    labels1, handles1 = zip(*sorted(zip(labels1, handles1)))
    ax1.legend(handles1, labels1)

# 4. Configurações de layout e exibição do Subplot 2
ax2.set_title("Arquivos iniciados com T160")
ax2.set_xlabel("Terceira Coluna")
ax2.set_ylabel("Segunda Coluna")
ax2.grid(True)
handles2, labels2 = ax2.get_legend_handles_labels()
if labels2:
    labels2, handles2 = zip(*sorted(zip(labels2, handles2)))
    ax2.legend(handles2, labels2)

# Ajusta o espaçamento para evitar sobreposições
plt.tight_layout()

# 5. Salvar o gráfico como "teste.png" no diretório atual ("dados")
caminho_saida = os.path.join(diretorio_dados, "teste3.png")
# dpi=300 garante uma boa resolução para a imagem salva
plt.savefig(caminho_saida, dpi=300)

# Fecha a figura para liberar memória (boa prática já que não vamos exibir na tela)
plt.close()

print(f"Gráfico gerado e salvo com sucesso em: {caminho_saida}")
