# Tic Tac Toe
**Description**: TicTacToe Game built with command-line interface  and written in Python. To know more about the game rules and other [info](https://en.wikipedia.org/wiki/Tic-tac-toe)
**Status**:  Current Version has all basic functionalities of the game with fixed board size. To know about the version [CHANGELOG](changelog.md)
**Test Coverage**: 81% of the  total code has been tested  
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
5. Game Started and First turns be given for the First player
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
$ coverage report -m
```

### Game Screenshot