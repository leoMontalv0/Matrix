import numpy as np
def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"Ingrese el valor para la posición ({i},{j}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    print("\nMatriz:")
    for fila in matriz:
        print(" ".join(map(str, fila)))

def editar_matriz(matriz):
    try:
        fila = int(input("Ingrese la fila a modificar: "))
        columna = int(input("Ingrese la columna a modificar: "))
        if 0 <= fila < len(matriz) and 0 <= columna < len(matriz[0]):
            nuevo_valor = int(input("Ingrese el nuevo valor: "))
            matriz[fila][columna] = nuevo_valor
        else:
            print("Posición fuera de rango.")
    except ValueError:
        print("Entrada no válida.")

def main():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    
    matriz = crear_matriz(filas, columnas)
    imprimir_matriz(matriz)

    while True:
        opcion = input("\n¿Desea editar un valor? (s/n): ").strip().lower()
        if opcion == 's':
            editar_matriz(matriz)
            imprimir_matriz(matriz)
        else:
            break

#hacer matriz identidad gauss pivot
def gauss_jordan_identidad(matriz):
    n = len(matriz)
    identidad = np.eye(n, dtype=float) 

    for i in range(n):
        max_fila = max(range(i, n), key=lambda r: abs(matriz[r][i]))
        if matriz[max_fila][i] == 0:
            raise ValueError("La matriz es singular y no tiene inversa.")
        
        if max_fila != i:
            matriz[i], matriz[max_fila] = matriz[max_fila], matriz[i]
            identidad[i], identidad[max_fila] = identidad[max_fila], identidad[i]

        pivote = matriz[i][i]
        matriz[i] = [x / pivote for x in matriz[i]]
        identidad[i] = [x / pivote for x in identidad[i]]

        for j in range(n):
            if i != j:
                factor = matriz[j][i]
                matriz[j] = [matriz[j][k] - factor * matriz[i][k] for k in range(n)]
                identidad[j] = [identidad[j][k] - factor * identidad[i][k] for k in range(n)]

    return identidad


if __name__ == "__main__":
    main()
