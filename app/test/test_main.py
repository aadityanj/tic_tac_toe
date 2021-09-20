from app.players.bot_player import BotPlayer
from app.players.human_player import HumanPlayer
from typing import Match
import unittest
from unittest.mock import MagicMock, patch
from app.main import TicTacToe

class TestMain(unittest.TestCase):
    
    def setUp(self) -> None:
        self.game = TicTacToe()
        self.game.initialize_first_player = MagicMock()
        self.game.initialize_second_player = MagicMock()
        self.game.mark_moves = MagicMock()
        self.game.print_winner_info = MagicMock()
        self.game.print_board_info = MagicMock()
        self.game.print_current_board = MagicMock()
        self.game.get_opponent_option = MagicMock()
        self.game.is_won = MagicMock()
        self.game.players = MagicMock(return_value={})
    
    @patch("builtins.print")
    def test_0_start(self, print):
        """
            Verify game executes all the methods & instructions - Ties Check
        """
        game = self.game
        game.players["0"] = MagicMock(HumanPlayer)
        game.players["1"] = MagicMock(HumanPlayer)
        game.is_won.return_value = False
        game.start()
        game.initialize_first_player.assert_called_once()
        game.initialize_second_player.assert_called_once()
        game.players["0"].get_choice.assert_called()
        game.players["1"].get_choice.assert_called()
        self.assertEqual(game.mark_moves.call_count, 9)
        game.is_won.assert_called()
        game.print_current_board.assert_called()
        game.print_winner_info.assert_not_called()
        print.assert_called_with("Game Tie!!")

    def test_1_start(self):
        """
            Verify game executes all the methods & instructions - Check Human wins
        """
        game = self.game
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
            Verify game executes all the methods & instructions - Check bot wins
        """
        game = self.game
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

    
if __name__ == "__main__":
    unittest.main()