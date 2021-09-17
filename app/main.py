from app.players.bot_player import BotPlayer
from app.players.human_player import HumanPlayer
from .board import Board


class TicTacToe(Board):
    def __init__(self) -> None:
        super().__init__()
        self.player_marks = {
            "0": "X",
            "1": "O"
        }
        self.players = {}

    def print_game_info(self) -> None:
        """
            Print Basic information of the game and it's input requirement
        """
        print("Welcome to the tic tac toe game")
        print("--------------------------------")
        print("Movement of Player1 will be shown as X in the board")
        print("Movement of Player2 will be shown as O in the board")
        print("Note- Input will be considered invalid if the input value is not between 1 to 9")
        print("Enter ctrl + c key to quit the game")

    def get_opponent_option(self) -> None:
        """
            Get player options of opponent, It should be either Bot or Human
        """
        while True:
            is_bot = input("Play with bot ? (yes or no): ")
            try:
                if is_bot == "yes":
                    return "bot"
                elif is_bot == "no":
                    return "human"
                else:
                    raise Exception("Invalid Input")
                break
            except BaseException:
                print("Invalid Input")

    def is_won(self, mark: str) -> bool:
        """
            Check whether the player's marked position can be connected as a straight line
            straight line can be connected either by
            row wise, column wise and diagnal wise of the board
            Args:
                symbol: Player's Mark (Sign) should be X or O
            Returns:
                Bool: Status of the Game - Either win or not win

        """
        board_size = self.size
        board = self.board
        left_diag_counter = right_diag_counter = 0  # diagonal counter
        for row in range(board_size):
            row_counter = col_counter = 0  # row & column wise counter
            for col in range(board_size):
                # row wise check
                if board[row][col] == mark:
                    row_counter = row_counter + 1
                # col wise check
                if board[col][row] == mark:
                    col_counter = col_counter + 1
            # diagonal wise check
            if board[row][row] == mark:
                left_diag_counter = left_diag_counter + 1

            if board[row][board_size - 1 - row] == mark:
                right_diag_counter = right_diag_counter + 1

            if row_counter == board_size or col_counter == board_size \
                    or left_diag_counter == board_size or right_diag_counter == board_size:
                return True
        return False

    def print_winner_info(self, opponent_player: str, player: object) -> None:
        """
            Prints the winner
            Args:
                opponent_player: Should be either bot or human
                player: players of the game
        """
        if (opponent_player != "bot"):
            print(f"Congratulations! {player.name} won the game.")
        elif (opponent_player == "bot" and player.mark == "O"):
            print(f"Oops! {self.players['0'].name} loose the game.")
            print("Best of luck, Next Time!!")

    def initialize_first_player(self) -> None:
        """Initialization of First player"""
        self.players["0"] = HumanPlayer(self.player_marks["0"])
        self.players["0"].set_player_info("First Player")

    def initialize_second_player(self, option):
        """Initialization of Second player
        Args:
            option: Second player's option, either bot or human
        Returns:
        """
        if option is "bot":
            self.players["1"] = BotPlayer(self.player_marks["1"])
            self.players["1"].set_player_info("Bot Player")
        else:
            self.players["1"] = HumanPlayer(self.player_marks["1"])
            self.players["1"].set_player_info("Second Player")

    def start(self) -> None:
        """
            Start of the game and it executes until any player wins or tie
        """
        move = 0
        option = self.get_opponent_option()
        self.initialize_first_player()
        self.initialize_second_player(option)
        current_turn = "0"
        while True and move < 9 :
            choice = self.players[current_turn].getChoice(self)
            self.mark_moves(
                self.player_marks[current_turn],
                choice
            )
            self.print_current_board()
            if self.is_won(self.player_marks[current_turn]):
                self.print_winner_info(option, self.players[current_turn])
                break
            if current_turn == "0":
                current_turn = "1"
            else:
                current_turn = "0"
            move += 1
        if move == 9:
            print("Game Tie!!")