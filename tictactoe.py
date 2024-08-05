import random

board = ["-","-","-",
        "-","-","-",
        "-","-","-"]
currentPlayer = "X"
winner = None
gameRunning = True

print("Enter Q to quit")

def printBoard(board):
    print(board[0] +" |" + board[1] + " |" + board[2] )
    print("---------")
    print(board[3] +" |" + board[4] + " |" + board[5] )
    print("---------")
    print(board[6] +" |" + board[7] + " |" + board[8] )

def playerInput(board):
    global gameRunning
    user_input = input("Enter a number from [1-9] :")
    if user_input.lower() == "q":
        gameRunning = False
    elif user_input.isdigit():
        user_input = int(user_input)
        if 1 <= user_input <= 9 and board[user_input-1] == "-":
            board[user_input - 1] = currentPlayer
        else:
            print("Invalid move. Try again.")
    else:
        print("Entered value is not a digit")
        gameRunning = False

def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRows(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie")
        gameRunning = False

def checkWins():
    global gameRunning
    if checkHorizontal(board) or checkRows(board) or checkDiagonal(board):
        gameRunning = False
        return True
    return False

def switchPlayer():
    global currentPlayer
    currentPlayer = "O" if currentPlayer == "X" else "X"

def computerMove(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

while gameRunning:
    printBoard(board)
    playerInput(board)
    if not gameRunning:
        break
    if checkWins():
        printBoard(board)
        print(f"The winner is {winner}")
        break
    checkTie(board)
    switchPlayer()
    computerMove(board)
    if checkWins():
        printBoard(board)
        print(f"The winner is {winner}")
        break
    checkTie(board)

print("Game Over")