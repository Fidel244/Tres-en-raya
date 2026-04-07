# Tasks: Add Menu Player Choice

## Implementation Steps

1. **Update mostrar_menu() function**
   - Add a third option: "3. Elegir símbolo"
   - Ensure the function returns the chosen option

2. **Modify main() function**
   - Add handling for option '3'
   - When '3' is chosen, prompt Player 1: "Elige tu símbolo (X/O): "
   - Validate input (only 'X' or 'O', case-insensitive)
   - Set variables: simbolo_jugador1, simbolo_jugador2, jugador_inicial
   - If simbolo_jugador1 == 'X', jugador_inicial = 'X'; else 'O'
   - After setting, return to menu (or directly start game? Design says return to menu)

3. **Refactor jugar() function**
   - Add parameters: simbolo_jugador1='X', simbolo_jugador2='O', jugador_inicial='X'
   - Update the game initialization to use these parameters
   - Change victory messages to use the symbols (e.g., "¡Jugador con {simbolo} gana!")

4. **Update main() to pass parameters to jugar()**
   - If option '1', call jugar() with default parameters
   - If after choosing symbol, call jugar(simbolo_jugador1, simbolo_jugador2, jugador_inicial)

5. **Test the implementation**
   - Test menu navigation
   - Test symbol choice and game start
   - Test victory conditions with chosen symbols
   - Test invalid inputs

## Flow
1. Main menu shows: 1. Iniciar partida, 2. Salir, 3. Elegir símbolo
2. If 3: Ask "Elige tu símbolo (X/O): "
3. If X: Player 1 = X, Player 2 = O, starts first
4. If O: Player 1 = O, Player 2 = X, Player 2 starts first
5. Then proceed to game with chosen setup

## Edge Cases
- Invalid input: Reprompt until valid (X or O)
- After symbol choice, return to menu or directly start game? (Design: return to menu for consistency)</content>
<parameter name="filePath">c:\Users\Fidel\Desktop\newproject\openspec\changes\add-menu-player-choice\design.md