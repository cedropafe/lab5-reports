#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){

FILE* data = fopen("data.dat", "r");

if (data == NULL) {
    perror("Error opening file!");
    return 1;
}

int n;
double x0, x1, dx, LAMBDA;
double Slambda, Mlambda;
double lambda[5];
double error, Serror, Merror, incert;

for (int j=0; j<5; j++){
fscanf(data, "%d %lf %lf", &n, &x0, &x1);

dx = x1 - x0;
LAMBDA = dx*2./10./1000.*1e9;
lambda[j] = LAMBDA/60.;
Slambda += lambda[j];

printf("%.2lf & %.2lf & %.2lf & %.2lf \n", x0, x1, LAMBDA, lambda[j]);
}

fclose(data);

Mlambda = Slambda/n;
printf("comprimento de onda medio: %.2lf \n", Mlambda);

for (int j=0; j<5; j++){
error = abs(lambda[j] - Mlambda );
Serror += error;
}

Merror = Serror/n;
incert = Merror / Mlambda *100 ;
printf("desvio médio: %.2lf \n", Merror);
printf("incerteza: %.2lf%% \n", incert);

return 0;
}
