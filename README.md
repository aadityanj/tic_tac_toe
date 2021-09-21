# Tic Tac Toe
**Description**: TicTacToe Game built with command-line interface  and written in Python. To know more about the game rules and other [info](https://en.wikipedia.org/wiki/Tic-tac-toe)

**Status**:  Current Version has all basic functionalities of the game with fixed board size. To know about the version [CHANGELOG](changelog.md)

**Test Coverage**: 98% of the whole code has been covered in the test  
## Dependencies
- Python - 3.8.5
- Coverage - 5.5
- git
### Linux and MacOS
Type the follwing commands on your terminal (without the '$')  
```
$ git clone https://github.com/aadityanj/tic_tac_toe
$ cd tic_tac_toe
$ python3 run.py
```
Now, you are good to start playing the game in your terminal
- To run the tests 
```
$ python3 run_test.py
```
##### How to play the Game
```
1. Game starts in terminal with showing general game information
2. Type 'yes or no` as the game asks for an option to play with bot or human player
3. Enter Name for the First player
4. Enter Name for the Second player
5. Game starts here and First turns be given for the First player
6. Enter Valid Choice to make your move in the game board
7. In Case of bot option, Once the first player enter the choice, bot choice will be made instantly
8. Until the game over, turns will keep rotating to both the user
9. Game Ends with 'Game Ties'  or 'Any player wins'
```
### Algorithm
- MiniMax Algorithm has been used to evaluvate best moves for the Bot player. To read [more](https://en.wikipedia.org/wiki/Minimax) about the algorithm
### Test Coverage
Type the following commands on your terminal to generate test coverage report
```
$ coverage run run_test.py && coverage report
```
### Enhancement Areas
- Log and store all the player's details and game's status
- Setup Dynamic Board size instead of sticking to 9 cells
- Provide Clues for Human player's to make a right move
- Increase more test cases to coverup all the logics
- Provice option to play bot first
### Coverage Report
```
Name                                 Stmts   Miss  Cover
--------------------------------------------------------
app/__init__.py                          0      0   100%
app/board.py                            41      0   100%
app/constants.py                         6      0   100%
app/main.py                             73      0   100%
app/players/__init__.py                  0      0   100%
app/players/bot_player.py               53      2    96%
app/players/human_player.py             26      4    85%
app/utils.py                             3      0   100%
run_test.py                              6      0   100%
tests/__pycache__/__init__.py            0      0   100%
tests/players/__init__.py                0      0   100%
tests/players/test_bot_player.py        79      1    99%
tests/players/test_human_player.py      35      1    97%
tests/test_board.py                     29      0   100%
tests/test_main.py                     118      1    99%
--------------------------------------------------------
TOTAL                                  469      9    98%
```

### Game Screenshot
```
Welcome to the tic tac toe game 
 -------------------------------- 
Movement of Player1 will be shown as X in the board 
Movement of Player2 will be shown as O in the board 
Note- Input will be considered invalid if the input value is not between 1 to 9 
Enter ctrl + c key to quit the game
Game Board
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
Play with bot ? (yes or no): yes
Enter a First Player Name - X: John   
Enter a Bot Player Name - O: Jack
John's turn ==> Enter your choice: 1
+---+---+---+
| X | 2 | 3 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
Jack's choice: 5
+---+---+---+
| X | 2 | 3 |
+---+---+---+
| 4 | O | 6 |
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
....
```
