import random

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


def frecuencia_relativa_evento(muestra):
    contador = 0

    for x in muestra:
        if 2/7 <= x <= 6/7:
            contador += 1

    return contador / len(muestra)


valores_n = [10**3, 10**4, 10**5, 10**6]

probabilidad_teorica = 4/7

print("Probabilidad teórica P(2/7 <= U <= 6/7):", probabilidad_teorica)

for n in valores_n:
    muestra = generar_muestra(n)
    frecuencia = frecuencia_relativa_evento(muestra)
    error = abs(frecuencia - probabilidad_teorica)

    print("\nTamaño de muestra n =", n)
    print("Frecuencia relativa:", frecuencia)
    print("Probabilidad teórica:", probabilidad_teorica)
    print("Error absoluto:", error)