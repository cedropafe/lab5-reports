#include <stdio.h>
#include <math.h>

int main(){

FILE* data = fopen("data.dat", "r");

if (data == NULL) {
    perror("Error opening file!");
    return 1;
}

int n;
double x0, x1, dx, lambda;
double Slambda = 0;

for (int j=1; j<=5; j++){
int read = fscanf(data, "%d %lf %lf", &n, &x0, &x1);

dx = x1 - x0;
lambda = dx*2./10./1000./60.*1e9;
Slambda += lambda;
printf("comprimento de onda: %.15lf \n", lambda);
}

printf("comprimento de onda medio: %.15lf \n", Slambda/n);

fclose(data);

return 0;
}
