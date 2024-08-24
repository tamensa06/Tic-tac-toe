*Tic Tac Toe Game*

*Description*

A simple implementation of the classic Tic Tac Toe game in Python. The game allows two players, X and O, to play against each other. The game also features a computer player that makes random moves.

*Features*

- Simple command-line interface
- Two-player mode
- Computer player mode
- Automatic winner detection
- Tie detection

*How to Play*

1. Run the script
2. Enter a number from 1-9 to make a move
3. Enter Q to quit
4. The computer player will make random moves

*Code Structure*

The code is organized into several functions:

- `printBoard(board)`: Prints the current state of the board
- `playerInput(board)`: Handles user input and updates the board
- `checkHorizontal(board)`, `checkRows(board)`, `checkDiagonal(board)`: Check for wins in each direction
- `checkTie(board)`: Checks for a tie
- `checkWins()`: Checks for a win and updates the game state
- `switchPlayer()`: Switches the current player
- `computerMove(board)`: Makes a random move for the computer player

*To-Do*

- Implement a more intelligent computer player
- Add additional features, such as scorekeeping or game history
