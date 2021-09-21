from app.utils import is_valid_name


class HumanPlayer:

    def __init__(self, mark: str) -> None:
        self.mark = mark

    def set_player_info(self, meta_str: str) -> None:
        """
            Ask the name of the player and set it
            Args:
                meta_str: Player's turn Either First player or Second player
        """
        while True:
            name = input(f'Enter a {meta_str} Name - {self.mark}: ')
            try:
                if is_valid_name(name):
                    self.name = name
                    return True
                else:
                    print("Invalid Name")
            except KeyboardInterrupt:
                print("Keyboard Interrupted")

    def get_choice(self, game_object: object) -> int:
        """
            Get player's choice
            Args:
                game_object: Context of the game to use for the
            Returns:
                position: Player's choice for the move
        """
        while True:
            position = input(f"{self.name}'s turn ==> Enter your choice: ")
            try:
                position = int(position.strip())
                if not game_object.is_valid_cell_no(position):
                    print("Position is Invalid")
                    continue
                if not game_object.is_cell_available(position):
                    print("Cell is already occupied")
                    continue
                return position
            except BaseException:
                print("Given input is invalid")
