#constants
PLAYER_MARKS = { 
        "0": "X", # first_player
        "1": "O" # second_player
    }

GAME_INFO = "Welcome to the tic tac toe game \n " + \
            "-------------------------------- \n" + \
            f"Movement of Player1 will be shown as {PLAYER_MARKS['0']} in the board \n" + \
            f"Movement of Player2 will be shown as {PLAYER_MARKS['1']} in the board \n" + \
            "Note- Input will be considered invalid if the input value is not between 1 to 9 \n" + \
            "Enter ctrl + c key to quit the game"

BOARD_SIZE = 3
BOARD_TOTAL_CELLS = BOARD_SIZE * BOARD_SIZE

BOT="bot"
HUMAN="human"