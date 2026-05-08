import random

# Función de la Parte 2.1
def simular_X():
    X = 0
    for i in range(1, 11):
        moneda = random.randint(0, 1)
        X += moneda / (2 ** i)
    return X


def generar_muestra(n):
    muestra = []

    for _ in range(n):
        muestra.append(simular_X())

    return muestra


# Valores pedidos
valores_n = [10**3, 10**4, 10**5, 10**6]


# Generar muestras
for n in valores_n:
    muestra = generar_muestra(n)

    print(f"\nMuestra para n = {n}")
    print("Primeros 10 valores:", muestra[:10])
    print("Cantidad de elementos generados:", len(muestra))