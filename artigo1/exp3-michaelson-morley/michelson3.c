#include <stdio.h>
#include <math.h>

double andrews(double t, double x, double lambda, int m){
    // função que calcula o índide de refração do vidro

    double numerador, denominador;
    double phi = x*M_PI/180; // converte graus para radianos

    numerador = (2*t-m*lambda)*(1-cos(phi))+(m*m*lambda*lambda/(4*t));
    denominador = 2*t*(1-cos(phi))-m*lambda;

    printf("numerador: %.14lf \n", numerador);
    printf("denominador: %.14lf \n", denominador);
    printf("refr index: %.14lf \n\n", numerador/denominador);

    return numerador/denominador;
}

int main() {
    FILE* data = fopen("dados.dat", "r"); // abre arquivo com os dados

    if (data == NULL){
        perror("file not found");
        return 1;
    }

    int m; // número de mínimos
    double t = 4*1e-3; // espessura do vidro
    double lambda = 632.8*1e-9; // comprimento de onda
    double x, N, Nmedio;
    int contador = 0;
    double Nsoma = 0;

    // calcula o valor de n para cada linha do arquivo de dados
    while(fscanf(data, "%d %lf", &m, &x) == 2){
        N = andrews(t, x, lambda, m);
        contador += 1;
        Nsoma += N;
    }

    Nmedio = Nsoma/contador;
    printf("average refr index: %.14lf \n", Nmedio);

    fclose(data);

return 0;
}
