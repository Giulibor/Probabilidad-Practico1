import random

def simular_X():
    X = 0

    # Simula las 10 monedas
    for i in range(1, 11):
        moneda = random.randint(0, 1)  # 0 = número, 1 = cara
        X += moneda / (2 ** i)

    return X


# Ejecutar archivo para que se corra automaticamente la funcoión.
resultado = simular_X()

print("Resultado de la variable aleatoria X:", resultado)