"""Script interactivo para multiplicar dos matrices cuadradas usando una función lambda.

El usuario ingresa el orden de las matrices y cada fila con valores separados por espacio.
"""
from typing import List

Matrix = List[List[float]]

leer_matriz = lambda n, nombre: [
    [
        float(valor)
        for valor in input(f"Fila {indice + 1} de la matriz {nombre} (separa con espacios): ").split()
    ]
    for indice in range(n)
]

multiplicar = lambda a, b: [
    [sum(x * y for x, y in zip(fila_a, columna_b)) for columna_b in zip(*b)]
    for fila_a in a
]


def main() -> None:
    orden = int(input("Ingresa el orden de las matrices cuadradas: "))
    print("\nIntroduce los valores de la primera matriz:")
    matriz_a = leer_matriz(orden, "A")

    print("\nIntroduce los valores de la segunda matriz:")
    matriz_b = leer_matriz(orden, "B")

    if any(len(fila) != orden for fila in matriz_a + matriz_b):
        raise ValueError("Todas las filas deben tener la misma longitud que el orden indicado")

    resultado = multiplicar(matriz_a, matriz_b)

    print("\nResultado de la multiplicación:")
    for fila in resultado:
        print(" ".join(f"{valor:.2f}" for valor in fila))


if __name__ == "__main__":
    main()
