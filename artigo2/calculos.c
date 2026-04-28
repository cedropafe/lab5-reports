#include <stdio.h>
#include <stdlib.h>

int main(){

    // abrir os arquivos de dados
    FILE* dados1 = fopen("video1.dat", "r");
    FILE* dados2 = fopen("video2.dat", "r");

    // verificar se foram corretamente abertos
    if (dados1 == NULL || dados2 == NULL){
        perror("arquivo(s) não encontrado(s)\n");
        return 1;
    }

    double s0, s1, Ds, d0, d1, Dd;

    FILE* output = fopen("output.dat", "w");

    // cálculos da bolha 1
    fprintf(output,"BOLHA 1\n");
    while(fscanf(dados1, "%lf %lf %lf %lf", &s0, &s1, &d0, &d1) == 4) {
        Ds = (s1 - s0)/1000;
        Dd = (d1 - d0)/1000;

        fprintf(output, "%.3lf %.3lf\n", Ds, Dd);
    }

    // cálculos da bolha 2
    fprintf(output, "\nBOLHA 2\n");
    while(fscanf(dados2, "%lf %lf %lf %lf", &s0, &s1, &d0, &d1) == 4) {
        Ds = (s1 - s0)/1000;
        Dd = (d1 - d0)/1000;

        fprintf(output, "%.3lf %.3lf\n", Ds, Dd);
    }

    fclose(output);

    return 0;
}
