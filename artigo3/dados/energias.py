import math

V = [13.1, 18.0, 23.1, 28.3, 33.6]
E = []
Soma = 0
for i in range(1, 5):
    dE = V[i] - V[i-1]
    E.append(dE)
    Soma += dE

Media = Soma / 4

print(E)
print(f"Soma: {Soma} V")
print(f"Média: {Media} V")

Erro = 0
for e in E:
    Erro += math.fabs(e - Media)

ErroMedio = Erro / 4
Incerteza = ErroMedio / Media *100
Desvio = math.fabs(Media-4.9) / 4.9 *100

print(f"Erro médio: {ErroMedio} V")
print(f"Incerteza: {Incerteza}%")
print(f"Desvio percentual: {Desvio}%")
