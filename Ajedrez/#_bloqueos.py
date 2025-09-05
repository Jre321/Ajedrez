#Jorge Andres Lopez, Jacobo Giraldo Tobon

import random

def crear_tablero(tamano):
    """Crea un tablero vacío con '.' """
    return [["." for _ in range(tamano)] for _ in range(tamano)]

def colocar_reina(tablero, x, y):
    """Coloca la reina en el tablero"""
    tablero[y-1][x-1] = "R"

def colocar_bloqueos(tablero, tamano, reina_x, reina_y, num_bloqueos):
    """Coloca bloqueos aleatorios en el tablero"""
    bloqueos = set()
    while len(bloqueos) < num_bloqueos:
        bx, by = random.randint(1, tamano), random.randint(1, tamano)
        if (bx, by) != (reina_x, reina_y) and (bx, by) not in bloqueos:
            bloqueos.add((bx, by))
            tablero[by-1][bx-1] = "X"
    return bloqueos

def marcar_movimientos(tablero, tamano, reina_x, reina_y):
    """Marca los movimientos posibles de la reina"""
    direcciones = [
        (1, 0), (-1, 0),   # Horizontal
        (0, 1), (0, -1),   # Vertical
        (1, 1), (-1, -1),  # Diagonal principal
        (1, -1), (-1, 1)   # Diagonal secundaria
    ]
    for dx, dy in direcciones:
        x, y = reina_x, reina_y
        while True:
            x += dx
            y += dy
            if 1 <= x <= tamano and 1 <= y <= tamano:
                if tablero[y-1][x-1] == "X":
                    break
                if tablero[y-1][x-1] == ".":
                    tablero[y-1][x-1] = "*"
            else:
                break

def imprimir_tablero(tablero):
    """Muestra el tablero en consola"""
    for fila in reversed(tablero):
        print(" ".join(fila))

tamano = int(input("Tamaño del tablero: "))
reina_x = int(input(f"Coordenada X de la reina (1 a {tamano}): "))
reina_y = int(input(f"Coordenada Y de la reina (1 a {tamano}): "))
num_bloqueos = int(input("Número de bloqueos aleatorios: "))

tablero = crear_tablero(tamano)
colocar_reina(tablero, reina_x, reina_y)
colocar_bloqueos(tablero, tamano, reina_x, reina_y, num_bloqueos)
marcar_movimientos(tablero, tamano, reina_x, reina_y)
imprimir_tablero(tablero)
