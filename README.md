# Relatórios experimentais da disciplina de lab5
Esse projeto é apenas uma maneira de registrar os relatórios que eu estou fazendo
para disciplina de Estrutura da Matéria Experimental -- lab5 para os íntimos. Dessa maneira, eu posso contornar
a nessecidade de usar o falecido overleaf (R.I.P.) para salvar projetos latex na nuvem. A pedido da professora,
os relatórias serão em forma de artigo APS, com duas colunas. 

## Estrutura do projeto
O diretório principal contém uma pasta com o template latex e uma pasta para cada artigo.

As pastas de artigo tem os dados experimentais e uma pasta com o nome artigo?_latex. 
Dentro desta, há os arquivos .tex, .bib, e a pasta de imagens. támbém há o aquivo cleanup.sh.
O arquivo principal será chamado main.tex em todos os arquivos.

As sessões do texto são:
- preamble.tex (preâmbulo)
- main.tex (arquivo principal, contém o \maketitle, os \input{}, e o \bibliography{})
- abstract.tex (resumo)
- introduction.tex (introdução e motivação)
- theory.tex (fundamentação teórica)
- methods.tex (metodologia, inlui a tabela de materias)
- results.tex (resultados e discussões)
- conclusion.tex (conclusão)
- thanks.tex (agradecimentos)

## latexmk
Para compilar o código e gerar o pdf, utilize o seguinte comando na pasta contendo main.tex:
> latexmk main.tex
> 
Entre latexmk e main.tex, podemos adicionar as seguintes flags:
- -pdf: garante a utilização de pdflatex, fazendo com que o arquivo de saída seja um pdf;
- -pv: preview, utiliza o visualizador padrão de pdf pra abrir o pdf gerado;
- -pvc: gera e exibe um novo pdf sempre que algum arquivo .tex sofrer alguma alteração. Recomento utilizar um terminal dedicado apenas para isso, especialmente se for utilizado com &.

É importante criar ou editar um arquivo de configuração .latexmkrc na sua pasta pessoal ou no diretório do projeto. nele, escreva
> \# "latexmk" == "latexmk main.tex"
> 
> @default_files = ("main.tex");

> \# "latexmk main.tex" == "latexmk -pdf main.tex"
> 
> $pdf_mode = 1;

> \# Automatically clean auxiliary files after successful compilation
> 
> $cleanup_mode = 2;

> \# Explicitly list files to remove
> 
> $cleanup_extra_files = "*Notes.bib";
> 
> $clean_ext = "aux bbl blg fdb_latexmk fls log ";

Se os arquivos temporário não forem automaticamente deletados, use
> latexmk -c
> 
Se isso não funcionar, a pasta contém um arquivo nomeado cleanup.sh.
Se esse arquivo não existir, crie-o. Seu conteúdo é:
> \# delete generated and curated files
> 
> rm -f *.aux *.log *.bbl *.blg *.fdb_latexmk *.fls *Notes.bib

Então escreva no terminal:
> bash cleanup.sh
>




