# Design: Implement GUI Tic Tac Toe

## Overview
Create a pygame-based GUI application with a menu screen and game screen. Use object-oriented programming for better structure (classes for Menu, Game, Board).

## Key Components
- **Window Setup**: 600x600 window, title "Tic Tac Toe GUI".
- **Menu Screen**: Central menu with buttons:
  - "Start Game" (default X/O)
  - "Choose Symbol" (select X or O for player 1)
  - "Exit"
- **Game Screen**: 3x3 grid, clickable cells, display current player, win/draw messages.
- **Event Handling**: Mouse clicks for menu buttons and board cells.
- **Drawing**: Use pygame.draw for lines, circles, and text rendering.

## Flow
1. Start with menu screen.
2. On "Start Game": Switch to game screen with default symbols.
3. On "Choose Symbol": Sub-menu to select symbol, then start game.
4. During game: Click cells to place symbols, check for win/draw after each move.
5. After game end: Show message and "Play Again" button to return to menu.

## Technical Details
- **Board Representation**: List of 9 elements, same as console version.
- **Symbol Choice**: Store player symbols, alternate turns.
- **Validation**: Prevent clicks on occupied cells, check wins after moves.
- **Modern Pygame**: Use pygame 2.x features, event loop, font rendering, color constants.

## Edge Cases
- Invalid clicks: Ignore or show feedback.
- Window close: Properly quit pygame.
- Symbol choice: Ensure player 1 gets chosen symbol, player 2 the other.</content>
<parameter name="filePath">c:\Users\Fidel\Desktop\newproject\openspec\changes\implement-gui-tic-tac-toe\proposal.md