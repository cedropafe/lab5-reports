import sys
import os
import glob
import re

def normalize_decimal(number_str):
    """Converte vírgula para ponto em um número"""
    return number_str.replace(',', '.')

def extract_numbers(line):
    """Extrai números de uma linha, independentemente do separador"""
    # Divide a linha por espaços e tabulações
    tokens = re.split(r'[\s\t]+', line.strip())

    numbers = []
    for token in tokens:
        if token:  # Ignora tokens vazios
            # Verifica se é um número (contém dígitos e opcionalmente -,+,. ou ,)
            if re.match(r'^[+-]?[\d.,]+$', token):
                normalized = normalize_decimal(token)
                numbers.append(normalized)

    return numbers

def process_file(input_file, output_file):
    """Processa um arquivo de entrada e gera saída formatada"""

    abs_path = os.path.abspath(input_file)
    print(f"Procurando em: {abs_path}")
    print(f"Repr do caminho: {repr(input_file)}")  # Mostra caracteres invisíveis
    print(f"os.path.exists(): {os.path.exists(input_file)}")
    print(f"os.path.isfile(): {os.path.isfile(input_file)}")
    print(f"Permissões (os.access): {os.access(input_file, os.R_OK)}")

    if not os.path.isfile(input_file):
        print(f"Erro: Arquivo não encontrado no início")
        return

    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()

        # Ignorar as 2 primeiras linhas
        data_lines = lines[2:]

        # Encontrar e pular a primeira linha vazia
        first_empty_found = False
        with open('./formated/'+output_file, 'w', encoding='utf-8') as outfile:
            for line in data_lines:
                # Verificar se é linha vazia
                if line.strip() == '':
                    if not first_empty_found:
                        first_empty_found = True
                        continue

                # Extrair números da linha
                numbers = extract_numbers(line)

                # Escrever números no arquivo de saída
                if numbers:
                    outfile.write(' '.join(numbers) + '\n')

        print(f"Arquivo processado: {input_file} -> {output_file}\n")

    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado - {input_file}", file=sys.stderr)
    except Exception as e:
        print(f"Erro ao processar {input_file}: {type(e).__name__}: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()

def generate_output_filename(input_file):
    """Gera nome do arquivo de saída"""
    # Extrai apenas o nome do arquivo (sem diretório)
    filename = os.path.basename(input_file)

    # Remove a extensão .txt se existir
    if input_file.endswith('.TXT'):
        base = filename[:-4]
    else:
        base = filename

    return f"{base}.dat"

def main():

    print(f"Diretório atual: {os.getcwd()}\n")  # DEBUG
    print(f"sys.argv: {sys.argv}\n")  # DEBUG

    if len(sys.argv) < 2:
        print(f"Use: {sys.argv[0]} <arquivo1.txt> [arquivo2.txt] ...")
        sys.exit(1)

    # Usar os arquivos diretamente dos argumentos
    for input_file in sys.argv[1:]:
        if os.path.isfile(input_file):
            output_file = generate_output_filename(input_file)
            process_file(input_file, output_file)
        else:
            print(f"✗ Arquivo não encontrado: {input_file}")

if __name__ == '__main__':
    main()

