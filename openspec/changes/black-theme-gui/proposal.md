# Proposal: Black Menu and Game Background Theme

## What
Update the GUI Tic Tac Toe theme so that:
- The main menu background is black.
- The game screen background is black.
- X marks are red.
- O circles are blue.
- Menu and game text/buttons remain readable over the dark background.

## Why
The requested visual style improves contrast and delivers a strong, consistent dark theme for the GUI version.

## Implementation
- Change `BG_COLOR` to black in `guiVERSION/main_gui.py`.
- Set `CROSS_COLOR` to red and `CIRCLE_COLOR` to blue.
- Keep the game grid and menu text visible by using high-contrast line and text colors.
- Verify both the menu screen and the active game board render correctly after the update.
