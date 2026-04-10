#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double andrews(double t, double x, double lambda, int m){
    // função que calcula o índide de refração do vidro

    double numerador, denominador;
    double phi = x*M_PI/180; // converte graus para radianos

    numerador = (2*t-m*lambda)*(1-cos(phi))+(m*m*lambda*lambda/(4*t));
    denominador = 2*t*(1-cos(phi))-m*lambda;

    return numerador/denominador;
}

int main() {
    FILE* data = fopen("dados60.dat", "r"); // abre arquivo com os dados

    if (data == NULL){
        perror("file not found");
        return 1;
    }

    int m[9]; // número de mínimos
    double t = 4*1e-3; // espessura do vidro
    double lambda = 633*1e-9; // comprimento de onda
    double x[9], N[9], Nmedio;
    double Nsoma = 0;
    double error, Merror;
    double Serror = 0;

    // calcula o valor de n para cada linha do arquivo de dados
    int j = 0;
    while(fscanf(data, "%d %lf", &m[j], &x[j]) == 2){
        N[j] = andrews(t, x[j], lambda, m[j]);
        Nsoma += N[j];
        j++;
    }

    fclose(data);

    // calula a média de N
    Nmedio = Nsoma/j;

    // calcula os desvios e imprie tabela formatada em latex
    for(int i=0; i<j; i++){
        error = fabs( N[i]-Nmedio);
        Serror += error;

        printf("%d & %.1lf & %.4lf \\\\ \n", m[i], x[i], N[i]);
    }
    Merror = Serror/j;

    printf("average refr index: %.4lf \n", Nmedio);
    printf("average error: %.13lf \n", Merror);
return 0;
}
