import random

def simular_X(cantidad_monedas):
    X = 0

    for i in range(1, cantidad_monedas + 1):
        moneda = random.randint(0, 1)
        X += moneda / (2 ** i)

    return X


def generar_muestra(n, cantidad_monedas):
    muestra = []

    for _ in range(n):
        muestra.append(simular_X(cantidad_monedas))

    return muestra


def frecuencia_relativa_evento(muestra):
    contador = 0

    for x in muestra:
        if 2/7 <= x <= 6/7:
            contador += 1

    return contador / len(muestra)


probabilidad_teorica = 4/7
valores_monedas = [10, 15, 20, 25, 30]
valores_n = [10**3, 10**4, 10**5, 10**6]

print("Probabilidad teórica:", probabilidad_teorica)

for monedas in valores_monedas:
    print("\nCantidad de monedas:", monedas)

    for n in valores_n:
        muestra = generar_muestra(n, monedas)
        frecuencia = frecuencia_relativa_evento(muestra)
        error = abs(frecuencia - probabilidad_teorica)

        print("n =", n)
        print("Frecuencia relativa:", frecuencia)
        print("Error absoluto:", error)
        print()