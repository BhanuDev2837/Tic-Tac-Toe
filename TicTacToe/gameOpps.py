import random

class TicTacToe:
    def __init__(self):
        self.choice = list(range(1, 10))
        self.board = [['?' for i in range(3)] for j in range(3)]

    def gameStart(self):
        print("Welcome to Tic Tac Toe!!")
        self.printBoard()

    def game(self):
        self.gameStart()
        playerChoice = input("Which one do you want to play ? X or O\n") 
        computerChoice = "X" if playerChoice == 'O' else 'O'

        while self.boardEmpty() :
            playerMove = int(input("Which box do you want to fill now - (1 to 9)\n"))
            if self.makeMove(playerChoice, playerMove):
                self.printBoard()
                if self.checkWinner(playerChoice):
                    print("Congratulations! You won!")
                    return
            else:
                print("Invalid move, please try again.")
                continue

            computerMove = random.choice(self.choice)
            if self.makeMove(computerChoice, computerMove):
                print("\nCompuer Moved\n")
                self.printBoard()
                if self.checkWinner(computerChoice):
                    print("Sorry, you lost!")
                    return
            else:
                print("Invalid move, please try again.")
                continue

        print("Match Tied")

    def makeMove(self, player, move):
        row = (move - 1) // 3
        col = (move - 1) % 3
        if self.board[row][col] == '?':
            self.board[row][col] = player
            return True
        else:
            return False

    def checkWinner(self, player):
        for i in range(3):
            # Check rows
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            # Check columns
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

    def cellEmpty(self, i, j):
        return self.board[i][j] == "?"

    def boardEmpty(self):
        for row in self.board:
            for col in row:
                if col == "?":
                    return True
        return False

    def printBoard(self):
        print(" ___________ ")
        print("| {} | {} | {} |".format(self.board[0][0], self.board[0][1], self.board[0][2]))
        print("|___|___|___|")
        print("| {} | {} | {} |".format(self.board[1][0], self.board[1][1], self.board[1][2]))
        print("|___|___|___|")
        print("| {} | {} | {} |".format(self.board[2][0], self.board[2][1], self.board[2][2]))
        print("|___|___|___|")
    
if __name__ == "__main__":
    tictactoe = TicTacToe()
    tictactoe.game()
