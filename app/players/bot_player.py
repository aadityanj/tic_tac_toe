from app.utils import is_valid_name
import math
from random import choice

class BotPlayer:

    def __init__(self, mark) -> None:
        self.mark = mark

    def set_player_info(self, meta_str) -> None:
        while True:
            name = input(f'Enter a {meta_str} Name - {self.mark}: ')
            try:
                if is_valid_name(name):
                    self.name = name
                    return True
                else:
                    print("Invalid Name")
            except BaseException:
                print("Given input is invalid")

    def getChoice(self, game_object):
        depth = len(game_object.get_empty_cells())
        if depth == 0 or (game_object.is_won("X") \
            or game_object.is_won("O")):
            return
        if depth == 9:
            x = choice([0, 1, 2])
            y = choice([0, 1, 2])
        else:
            move = self._minimax(game_object.board, depth, game_object, True)
            x, y = move[0], move[1]
        bots_choice =  (x * 3) + y
        bots_choice += 1
        print(f"{self.name}'s choice: {bots_choice}")
        return bots_choice

    def _minimax(self, board: dict, depth: int, game_object, bot=True) -> int:
        """
            Algorithm: MiniMax
            Virtually simulate the game and take the best position for bot's movement to win
            Args:
                grid: Game board with player occupied marks
                depth: No of cells available for next move
                bot: True if it is bot 
            Returns:
                int: Returns the best choice
        """
        #best = [row, col, least no]
        if bot:
            best = [-1, -1, -math.inf]
        else:
            best = [-1, -1, math.inf]

        if depth == 0 or (game_object.is_won("X") or game_object.is_won("O")):
            score = 0
            if game_object.is_won("X"):
                score = -1 # indicates chance of loses 
            elif game_object.is_won("O"):
                score = +1 # indicates chance of win
            return [-1, -1, score]

        for cell in game_object.get_empty_cells():
            x, y = cell[0], cell[1]
            board[x][y] = "O" if bot else "X"
            player = False if bot else True
            score = self._minimax(board, depth - 1, game_object, player)
            board[x][y] = " "
            score[0], score[1] = x, y

            if bot:
                if score[2] > best[2]:
                    best = score
            else:
                if score[2] < best[2]:
                    best = score

        return best