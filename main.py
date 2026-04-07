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
    print("3. Elegir símbolo")
    opcion = input("Elige una opción: ")
    return opcion

def jugar(simbolo_jugador1='X', simbolo_jugador2='O', jugador_inicial='X'):
    """Función que ejecuta una partida completa."""
    tablero = [str(i+1) for i in range(9)]  # Inicializar con '1' a '9'
    current_player = 1 if simbolo_jugador1 == jugador_inicial else 2

    print(f"\n¡Bienvenido al Tic Tac Toe!")
    print(f"Jugador {current_player} ({jugador_inicial}) comienza. Ingresa un número del 1 al 9 para colocar tu marca.")

    while True:
        dibujar_tablero(tablero)
        estado = verificar_estado_juego(tablero)

        if estado == simbolo_jugador1:
            print("¡Jugador 1 (x) gana!")
            return
        elif estado == simbolo_jugador2:
            print("¡Jugador 2 (o)gana!")
            return
        elif estado == 'empate':
            print("¡Es un empate!")
            return

        simbolo_actual = simbolo_jugador1 if current_player == 1 else simbolo_jugador2
        try:
            movimiento = int(input(f"Jugador {current_player} ({simbolo_actual}), elige una posición (1-9): ")) - 1
            if movimiento < 0 or movimiento > 8:
                print("Posición inválida. Debe ser un número del 1 al 9.")
                continue
            if tablero[movimiento] in ['X', 'O']:
                print("Esa posición ya está ocupada. Elige otra.")
                continue
            tablero[movimiento] = simbolo_actual
            current_player = 2 if current_player == 1 else 1
        except ValueError:
            print("Entrada inválida. Debe ser un número del 1 al 9.")
            continue

def elegir_simbolo():
    """Permite al jugador 1 elegir su símbolo."""
    while True:
        simbolo = input("Elige tu símbolo (X/O): ").strip().upper()
        if simbolo in ['X', 'O']:
            return simbolo
        print("Símbolo inválido. Elige X o O.")

def main():
    while True:
        opcion = mostrar_menu()
        match opcion:
            case '1':
                jugar('X', 'O', 'X')
            case '2':
                print("¡Hasta luego!")
                break
            case '3':
                simbolo_jugador1 = elegir_simbolo()
                simbolo_jugador2 = 'O' if simbolo_jugador1 == 'X' else 'X'
                jugador_inicial = simbolo_jugador1
                jugar(simbolo_jugador1, simbolo_jugador2, jugador_inicial)
            case _:
                print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()