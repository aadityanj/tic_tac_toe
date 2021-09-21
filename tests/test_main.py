from app.constants import BOT, GAME_INFO, HUMAN
from app.players.bot_player import BotPlayer
from app.players.human_player import HumanPlayer
import unittest
from unittest.mock import MagicMock, patch
from app.main import TicTacToe

class TestMain(unittest.TestCase):
    
    def setUp(self) -> None:
        self.game = TicTacToe()
        self.game.players = MagicMock(return_value={})
    
    def mock_all_methods(self):
        self.game.initialize_first_player = MagicMock()
        self.game.initialize_second_player = MagicMock()
        self.game.mark_moves = MagicMock()
        self.game.print_winner_info = MagicMock()
        self.game.print_board_info = MagicMock()
        self.game.print_current_board = MagicMock()
        self.game.get_opponent_option = MagicMock()
        self.game.is_won = MagicMock()

    @patch("builtins.print")
    def test_0_start(self, print):
        """
            Verify game executes all the methods & instructions - Ties Check
        """
        game = self.game
        self.mock_all_methods()
        game.players["0"] = MagicMock(HumanPlayer)
        game.players["1"] = MagicMock(HumanPlayer)
        game.is_won.return_value = False
        game.start()
        game.initialize_first_player.assert_called_once()
        game.initialize_second_player.assert_called_once()
        game.players["0"].get_choice.assert_called()
        game.players["1"].get_choice.assert_called()
        self.assertEqual(game.mark_moves.call_count, 9)
        self.assertEqual(game.is_won.call_count, 9)
        self.assertEqual(game.print_current_board.call_count, 9)
        game.print_winner_info.assert_not_called()
        print.assert_called_with("Game Tie!!")

    def test_1_start(self):
        """
            Verify game executes all the methods & instructions - Check on Human wins
        """
        game = self.game
        self.mock_all_methods()
        game.players["0"] = MagicMock(HumanPlayer)
        game.players["1"] = MagicMock(HumanPlayer)
        game.get_opponent_option.return_value = "human"
        game.is_won.side_effect=[False, False, True]
        game.start()
        game.initialize_second_player.assert_called_once()
        game.initialize_second_player.assert_called_once()
        game.players["0"].get_choice.assert_called()
        game.players["1"].get_choice.assert_called()
        game.mark_moves.assert_called()
        game.is_won.assert_called()
        game.print_current_board.assert_called()
        game.print_winner_info.assert_called_with("human", game.players["1"])

    def test_2_start(self ):
        """
            Verify game executes all the methods & instructions - Check on bot wins
        """
        game = self.game
        self.mock_all_methods()
        game.get_opponent_option.return_value = "bot"
        game.players["0"] = MagicMock(HumanPlayer)
        game.players["1"] = MagicMock(BotPlayer)
        game.is_won.side_effect=[False, True]
        game.start()
        game.initialize_first_player.assert_called_once()
        game.initialize_second_player.assert_called_once()
        game.players["0"].get_choice.assert_called()
        game.players["1"].get_choice.assert_called()
        game.mark_moves.assert_called()
        game.is_won.assert_called()
        game.print_current_board.assert_called()
        game.print_winner_info.assert_called_with("bot", game.players["1"])

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["random", "yes", "no"])
    def test_get_opponent_option(self, mock_input, mock_print):
        """
            Verify get_opponent_option returns right values
        """
        option = self.game.get_opponent_option()
        mock_print.assert_called_with("Invalid Input")
        self.assertEqual(option, "bot")
        option = self.game.get_opponent_option()
        self.assertEqual(option, "human")
    
    @patch("builtins.print")
    def test_print_game_info(self, mock_print):
        """
            Verify Print_game_info method prints game_info
        """
        self.game.print_game_info()
        mock_print.assert_called_with(GAME_INFO)
    
    def test_initialize_first_player(self):
        """
            Verify initialize_first_player method
        """
        self.game.players["0"] = MagicMock(HumanPlayer)
        self.game.initialize_first_player()
        self.game.players["0"].set_player_info.assert_called_once()

    def test_initialize_second_player(self):
        """
            Verify initialize_second_player method
        """
        self.game.players["1"] = MagicMock(BotPlayer)
        self.game.initialize_second_player(BOT)
        self.game.players["1"].set_player_info.assert_called()
        self.game.players["1"] = MagicMock(HumanPlayer)
        self.game.initialize_second_player(HumanPlayer)   
        self.game.players["1"].set_player_info.assert_called()

    def test_is_won(self):
        """
            Verify is_won method when any player finished the game
        """
        win_board = [["","X"," "],["","X",""], ["","X",""]]
        self.game.board = win_board
        self.assertTrue(self.game.is_won("X"))
        win_board = [["X",""," "],["X","",""], ["X","",""]]
        self.game.board = win_board
        self.assertTrue(self.game.is_won("X"))
        win_board = [["X",""," "],["","X",""], ["","","X"]]
        self.game.board = win_board
        self.assertTrue(self.game.is_won("X"))
        win_board = [["X",""," "],["","",""], ["","","X"]]
        self.game.board = win_board
        self.assertFalse(self.game.is_won("X"))

    @patch("builtins.print")  
    def test_print_winner_info(self, mock_print):
        """
            Verify print_winner_info method
        """
        player = MagicMock(BotPlayer)
        player.name = "Bot"
        player.mark = "O"
        self.game.print_winner_info(BOT, player)
        mock_print.assert_called()
        player = MagicMock(HumanPlayer)
        player.name = "Human"
        player.mark = "X"
        self.game.print_winner_info(HUMAN, player)
        mock_print.assert_called()

    
if __name__ == "__main__":
    unittest.main()