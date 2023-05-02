import random

def gameStart():
    print("Welcome to Tic Tac Toe!!")
    printBoard(board)

def game(board):
    gameStart()
    # youPlayFirst = True 
    playerChoice = input("Which one do you want to play ? X or O\n") 
    computerChoice = "X" if playerChoice == 'O' else 'O'
    
    while boardEmpty(board) :
        playerMove = int(input("Which box do you want to fill now - (1 to 9)\n"))
        if makeMove(board, playerChoice, playerMove):
            printBoard(board)
            if checkWinner(board, playerChoice):
                print("Congratulations! You won!")
                return
        else:
            print("Invalid move, please try again.")
            continue
        
        computerMove = random.choice(choice)
        if makeMove(board, computerChoice, computerMove):
            print("\nCompuer Moved\n")
            printBoard(board)
            if checkWinner(board, computerChoice):
                print("Sorry, you lost!")
                return
        else:
            print("Invalid move, please try again.")
            continue
    
    print("Match Tied")

def makeMove(board, player, move):
    row = (move - 1) // 3
    col = (move - 1) % 3
    if board[row][col] == '?':
        board[row][col] = player
        return True
    else:
        return False

def checkWinner(board, player):
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def cellEmpty(i, j):
    return board[i][j] == "?"

def boardEmpty(board):
    for row in board:
        for col in row:
            if col == "?":
                return True
    return False

def printBoard(board):
    print(" ___________ ")
    print("| {} | {} | {} |".format(board[0][0], board[0][1], board[0][2]))
    print("|___|___|___|")
    print("| {} | {} | {} |".format(board[1][0], board[1][1], board[1][2]))
    print("|___|___|___|")
    print("| {} | {} | {} |".format(board[2][0], board[2][1], board[2][2]))
    print("|___|___|___|")

if __name__ == "__main__":
    choice = list(range(1, 10))
    board = [['?' for i in range(3)] for j in range(3)]
    game(board)
