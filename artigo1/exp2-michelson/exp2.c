#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main() {

    FILE *dados = fopen("dados.dat", "r");
    FILE *output = fopen("output.dat", "w");

    if(dados == NULL){
        perror("File not found");
        return 1;
    }

    fprintf(output, "@TYPE xydx\n");

    int n;
    double p[10], media[5], erro[5];

    for(int i=0; i<5; i++){
        fscanf(dados, "%d %lf %lf %lf %lf %lf %lf %lf %lf %lf %lf", &n, &p[0], &p[1], &p[2], &p[3], &p[4], &p[5], &p[6], &p[7], &p[8], &p[9]);

        for(int j=0; j<10; j++){
            media[i] +=p[j];
        }

        media[i] /= 10.;

        for(int j=0; j<10; j++){
            erro[i] += fabs(media[i]-p[j]);
        }

        erro[i] /= 10.;

        fprintf(output, "%.0lf %d %.1lf\n", media[i], n, erro[i]);
    }

    fclose(dados);
    fclose(output);
    return 0;
}
