class Board:

    def __init__(self) -> None:
        self.size = 3
        self.board = [[1, 2, 3], [4, 5, 6],
                      [7, 8, 9]]  # 3 rows and 3 columns
        self.total_cells = self.size * 3

    def print_board_info(self) -> None:
        """
            Prints Board along with its cell number
        """
        print("Game Board")
        print("+---+---+---+")
        print("| 1 | 2 | 3 |")
        print("+---+---+---+")
        print("| 4 | 5 | 6 |")
        print("+---+---+---+")
        print("| 7 | 8 | 9 |")
        print("+---+---+---+")

    def mark_moves(self, mark: str, choice: str) -> None:
        """
            Marks the player's mark in the board
            Args:
                mark: Player's Mark Either X or O
        """
        position = choice - 1
        self.board[position // 3][position % 3] = mark

    def print_current_board(self) -> None:
        """
            Prints Lastest Board with players movement marks
        """
        print("+---+---+---+")
        print(
            "| {0} | {1} | {2} |".format(
                self.board[0][0],
                self.board[0][1],
                self.board[0][2]))
        print("+---+---+---+")
        print(
            "| {0} | {1} | {2} |".format(
                self.board[1][0],
                self.board[1][1],
                self.board[1][2]))
        print("+---+---+---+")
        print(
            "| {0} | {1} | {2} |".format(
                self.board[2][0],
                self.board[2][1],
                self.board[2][2]))
        print("+---+---+---+")

    def is_valid_cell_no(self, position: int) -> bool:
        """
            Validate Cell number
            Args:
                position: position of the board
            Returns:
                bool: True if valid
        """
        if position > 0 and position <= self.total_cells:
            return True
        return False

    def is_cell_available(self, choice: str) -> str:
        """
            Checks whether the position is available to mark in the board
            Args:
                choice: Choice ie Cell no entered by the user
        """
        position = choice - 1
        if self.board[position // 3][position % 3] not in ["X", "O"]:
            return choice

    def get_empty_cells(self) -> list:
        """
            Get all the empty cells of the board
            Returns:
                list: All the empty cells in the board
        """
        cells = []
        for x, row in enumerate(self.board):
            for y, cell in enumerate(row):
                if cell not in ["X", "O"]:
                    cells.append([x, y])
        return cells
