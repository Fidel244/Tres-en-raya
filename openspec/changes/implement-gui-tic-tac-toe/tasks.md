# Tasks: Implement GUI Tic Tac Toe

## Implementation Steps

1. **Set up pygame environment**
   - Install pygame if not already installed: `pip install pygame`
   - Create main.py in guiVERSION/ folder

2. **Create basic pygame window**
   - Initialize pygame, set up 600x600 window with title
   - Implement main event loop

3. **Implement Menu Screen**
   - Create a Menu class with buttons for "Start Game", "Choose Symbol", "Exit"
   - Handle mouse clicks on buttons
   - Draw central menu layout

4. **Implement Symbol Choice**
   - Add sub-menu for choosing X or O
   - Store chosen symbols for players

5. **Implement Game Board**
   - Create Board class to represent 3x3 grid
   - Draw grid lines and clickable areas
   - Handle cell clicks to place symbols

6. **Implement Game Logic**
   - Integrate win/draw checking from console version
   - Alternate player turns
   - Display current player and game status

7. **Add Visual Feedback**
   - Draw X and O symbols in cells
   - Show win/draw messages
   - Highlight winning lines if possible

8. **Add Play Again functionality**
   - Button to return to menu after game end
   - Reset board state

9. **Polish and Test**
   - Ensure proper pygame quit on window close
   - Test all menu options and game scenarios
   - Use modern Python practices (type hints, etc.)