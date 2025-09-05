#Jorge Andres Lopez, Jacobo Giraldo Tobon

import random

def generar_bloqueo(n, fila_reina, col_reina):
    """Genera una posición aleatoria de bloqueo distinta a la de la reina."""
    while True:
        fila_bloqueo = random.randint(1, n)
        col_bloqueo = random.randint(1, n)
        if (fila_bloqueo, col_bloqueo) != (fila_reina, col_reina):
            return fila_bloqueo, col_bloqueo

def calcular_movimientos(n, fila_reina, col_reina, fila_bloqueo, col_bloqueo):
    """Calcula los movimientos posibles de la reina considerando el bloqueo."""
    movs = []
    direcciones = [
        (-1, 0), (1, 0), (0, -1), (0, 1),     # Vertical y horizontal
        (-1, -1), (-1, 1), (1, -1), (1, 1)    # Diagonales
    ]
    for df, dc in direcciones:
        f, c = fila_reina + df, col_reina + dc
        while 1 <= f <= n and 1 <= c <= n:
            if (f, c) == (fila_bloqueo, col_bloqueo):
                break
            movs.append((f, c))
            f += df
            c += dc
    return movs

def imprimir_tablero(n, fila_reina, col_reina, fila_bloqueo, col_bloqueo, movs):
    """Imprime el tablero con reina, bloqueo y movimientos posibles."""
    for f in range(1, n + 1):
        linea = ""
        for c in range(1, n + 1):
            if (f, c) == (fila_reina, col_reina):
                linea += " R "
            elif (f, c) == (fila_bloqueo, col_bloqueo):
                linea += " X "
            elif (f, c) in movs:
                linea += " * "
            else:
                linea += " . "
        print(linea)
    print("\nMovimientos posibles:", len(movs))
    print("Bloqueo en:", fila_bloqueo, col_bloqueo)

def main():
    n = int(input("Tamaño del tablero: "))
    fila_reina, col_reina = map(int, input("Coordenadas de la reina (fila columna, separadas por espacio): ").split())
    
    fila_bloqueo, col_bloqueo = generar_bloqueo(n, fila_reina, col_reina)
    movs = calcular_movimientos(n, fila_reina, col_reina, fila_bloqueo, col_bloqueo)
    imprimir_tablero(n, fila_reina, col_reina, fila_bloqueo, col_bloqueo, movs)

main()

