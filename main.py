class TicTacToe:

    def __init__(self) -> None:
        """
            Init
        """
        self.moves = {}  # hold moves of both player
        self.symbols = {
            "player1": "X", # X symbol used to mark for player1
            "player2": "O" # O symbol used to mark for player2
        }
        self.size = 3 # Default grid size is 3
        self.grid = [[" "," " ," "], [" "," " ," "], [" "," " ," "]]
        self.total_cells = (3 * 3) - 1

    def show_info(self) -> None:
        """
            Print Basic information of the game and it's input requirement
        """
        print("Welcome to the tic tac toe game")
        print("--------------------------------")
        print("Symbol of player1 is X ")
        print("Symbol of player2 is O ")
        self.show_default_board()
        print("Note- Input will be considered invalid if the input value is not 0 between 8")
        print("")
        print("Enter ctrl + c key to quit the game")
        print("")
    
    def show_default_board(self) -> None:
        """
            Prints Board along with its cell number
        """
        print("Game Board")
        print("+---+---+---+")
        print("| 0 | 1 | 2 |")
        print("+---+---+---+")
        print("| 3 | 4 | 5 |")
        print("+---+---+---+")
        print("| 6 | 7 | 8 |")
        print("+---+---+---+")

    def show_board(self) -> None:
        """
            Prints Lastest Board with players movement marks
        """
        print("+---+---+---+")
        print("| {0} | {1} | {2} |".format(self.grid[0][0], self.grid[0][1], self.grid[0][2]))
        print("+---+---+---+")
        print("| {0} | {1} | {2} |".format(self.grid[1][0], self.grid[1][1], self.grid[1][2]))
        print("+---+---+---+")
        print("| {0} | {1} | {2} |".format(self.grid[2][0], self.grid[2][1], self.grid[2][2]))
        print("+---+---+---+")

    def get_input(self, inp_message: str) -> int:
        """
            Get valid input from users
            Args:
                inp_message: Input's info prompt
            Returns:
                int: User's choice
        """
        while True:
            position = input(inp_message)
            try:
                position = int(position.strip())
                if position > -1 and position <= self.total_cells:
                    if self.grid[position//3][position%3] not in self.symbols.values():
                        return position
                    else:
                        print("Invalid Input")
                else:
                    print("Invalid Input")
            except BaseException:
                print("Given input is invalid")
        
    def start_game(self) -> None:
        """
            starts the game
            Get input from user until the game board fills
            Check game status on each player's turn
        """
        moves_taken = 0
        while True:
            # First player's turn    
            position = self.get_input("player1 ==> Enter the position: ")
            self.mark_moves(self.symbols["player1"], position)
            won = self.game_status(self.symbols["player1"])
            if won:
                print("Player1 X has won the game")
                break

            moves_taken += 1

            if moves_taken >= 8:
                print("Match Tie")
                break

            #Second Player's turn        
            position = self.get_input("player2 ==> Enter the position: ")
            self.mark_moves(self.symbols["player2"], position)
            won = self.game_status(self.symbols["player2"])
        
            if won:
                print("Player2 O has won the game")
                break
                
            moves_taken += 1

    def mark_moves(self, symbol: str, position: int) -> None:
        """
            Mark the player's position in the board
            Args:
                symbol: Player's Mark (Sign) should be X or O
                position: User's choice in the board
        """
        self.grid[position // 3][position % 3] = symbol
        self.show_board()
    
    def game_status(self, symbol: str) -> bool:
        """ 
            Check whether the player's marked position can be connected as a straight line
            straight line can be connected either by 
            row wise, column wise and diagnal wise of the board
            Args:
                symbol: Player's Mark (Sign) should be X or O
            Returns:
                Bool: Status of the Game - Either win or not win

        """
        diag_counter = 0 # diagonal counter
        for row in range(self.size):
            row_counter = col_counter = 0 #row & column wise counter
            for col in range(self.size):
                #row wise check
                if self.grid[row][col] == symbol:
                    row_counter = row_counter + 1
                #col wise check
                if self.grid[col][row] == symbol:
                    col_counter = col_counter + 1
            # diagonal wise check
            if self.grid[row][row] == symbol:
                diag_counter = diag_counter + 1

            if row_counter == self.size or col_counter == self.size or diag_counter == self.size:
                    return True
        return False


if __name__ == "__main__":
    game = TicTacToe()
    game.show_info()
    game.start_game()
