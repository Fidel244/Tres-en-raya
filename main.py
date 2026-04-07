# Tic Tac Toe (Gato) - Juego CLI
# Tech stack: Python 3.x
# Domain: CLI Juego (Legacy Mode)
# Description: Un juego de Tic Tac Toe que se ejecuta totalmente en la terminal.
# Style: Programación procedimental, sin dependencias externas.
# Constraints:
# - Solo usar caracteres ASCII o UNICODE para el tablero.
# - No utilizar librerías gráficas.
# - La interfaz debe ser mediante print() e input().

# Estructura del tablero: lista de 9 elementos, inicialmente con números 1-9 para posiciones
# 0 1 2
# 3 4 5
# 6 7 8

def dibujar_tablero(tablero):
    """Función dedicada a dibujar el tablero en ASCII."""
    print("\n")
    print(f" {tablero[0]} | {tablero[1]} | {tablero[2]} ")
    print("---|---|---")
    print(f" {tablero[3]} | {tablero[4]} | {tablero[5]} ")
    print("---|---|---")
    print(f" {tablero[6]} | {tablero[7]} | {tablero[8]} ")
    print("\n")

def verificar_estado_juego(tablero):
    """Verifica el estado del juego: 'X' gana, 'O' gana, 'empate', o 'continuar'."""
    # Filas
    for i in range(0, 9, 3):
        if tablero[i] == tablero[i+1] == tablero[i+2] and tablero[i] in ['X', 'O']:
            return tablero[i]

    # Columnas
    for i in range(3):
        if tablero[i] == tablero[i+3] == tablero[i+6] and tablero[i] in ['X', 'O']:
            return tablero[i]

    # Diagonales
    if tablero[0] == tablero[4] == tablero[8] and tablero[0] in ['X', 'O']:
        return tablero[0]
    if tablero[2] == tablero[4] == tablero[6] and tablero[2] in ['X', 'O']:
        return tablero[2]

    # Empate si no hay espacios vacíos
    if all(isinstance(pos, str) and pos in ['X', 'O'] for pos in tablero):
        return 'empate'

    return 'continuar'

def mostrar_menu():
    """Muestra el menú principal y retorna la opción elegida."""
    print("\n=== Tic Tac Toe ===")
    print("1. Iniciar partida")
    print("2. Salir")
    opcion = input("Elige una opción: ")
    return opcion

def jugar():
    """Función que ejecuta una partida completa."""
    tablero = [str(i+1) for i in range(9)]  # Inicializar con '1' a '9'
    jugador_actual = 'X'

    print("\n¡Bienvenido al Tic Tac Toe!")
    print("Jugador X comienza. Ingresa un número del 1 al 9 para colocar tu marca.")

    while True:
        dibujar_tablero(tablero)
        estado = verificar_estado_juego(tablero)

        if estado == 'X':
            print("¡Jugador X gana!")
            return
        elif estado == 'O':
            print("¡Jugador O gana!")
            return
        elif estado == 'empate':
            print("¡Es un empate!")
            return

        try:
            movimiento = int(input(f"Jugador {jugador_actual}, elige una posición (1-9): ")) - 1
            if movimiento < 0 or movimiento > 8:
                print("Posición inválida. Debe ser un número del 1 al 9.")
                continue
            if tablero[movimiento] in ['X', 'O']:
                print("Esa posición ya está ocupada. Elige otra.")
                continue
            tablero[movimiento] = jugador_actual
            jugador_actual = 'O' if jugador_actual == 'X' else 'X'
        except ValueError:
            print("Entrada inválida. Debe ser un número del 1 al 9.")
            continue

def main():
    while True:
        opcion = mostrar_menu()
        match opcion:
            case '1':
                jugar()
            case '2':
                print("¡Hasta luego!")
                break
            case _:
                print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()