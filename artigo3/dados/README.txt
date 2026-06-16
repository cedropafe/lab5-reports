O nome do arquivo contém os parâmetros de temperatura e potencial de retardo(desaceleração, Ud). Ex: T160U1 é 160°C e Ud=1.0V;    T160U05 é 160°C e Ud=0.5V, e assim por diante.

Os dados que estão nos arquivos são os dados brutos de cada experimento.

Analog in 1: corrente (em fundo de escala 0,1 μA). Está negativo pois a polaridade está invertida, então precisa também tirar o módulo.
Analog in 2: potencial de aceleração/2

Usem a correção dos valores conforme o roteiro do experimento.

Eu achei necessário suavizar a coluna do potencial de aceleração, pois ela apresenta um nível significativo de ruído. Sem essa suavização, o ruído é propagado para o gráfico de Corrente x Ua e não dá pra analisar muito bem...
