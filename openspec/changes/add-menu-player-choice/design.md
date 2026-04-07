# Design: Add Menu Player Choice

## Overview
Modify the main menu to include a third option for symbol selection. When selected, prompt Player 1 to choose 'X' or 'O'. Based on the choice, set the starting player and symbols accordingly.

## Changes Required
- **mostrar_menu()**: Add option "3. Elegir símbolo"
- **main()**: Handle option '3' by prompting for symbol choice and setting variables (e.g., simbolo_jugador1, simbolo_jugador2, jugador_inicial)
- **jugar()**: Accept parameters for starting player and symbols, update the game logic to use them
- Update victory messages to reflect the chosen symbols

## Flow
1. Main menu shows: 1. Iniciar partida, 2. Salir, 3. Elegir símbolo
2. If 3: Ask "Elige tu símbolo (X/O): "
3. If X: Player 1 = X, Player 2 = O, starts first
4. If O: Player 1 = O, Player 2 = X, Player 2 starts first
5. Then proceed to game with chosen setup

## Edge Cases
- Invalid input: Reprompt until valid (X or O)
- After symbol choice, return to menu for consistency