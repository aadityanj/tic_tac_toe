import unittest
from unittest.mock import patch, MagicMock
from app.players.bot_player import BotPlayer
import io
from app.main import TicTacToe


class TestBotPlayer(unittest.TestCase):

    def setUp(self):
        """
            Inits required classes to Test BotPlayer's method
        """
        self.player = BotPlayer("O")
        self.mock_game_obj = TicTacToe()
        self.mock_game_obj.get_empty_cells = MagicMock()
        self.mock_game_obj.is_won = MagicMock()

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["123Adithya", "Adithya"])
    def test_set_player_info(self, mock_input, mock_print):
        """
            Assert the expected behaviour for both valid and invalid name
        """
        is_done = self.player.set_player_info("First Player")
        mock_print.assert_called_with("Invalid Name")
        self.assertEqual(self.player.name, 'Adithya')
        self.assertTrue(is_done)

    def test_1_get_choice(self):
        """
            Verify get_choice when the game is in over state
        """
        mock_game_obj = self.mock_game_obj
        mock_game_obj.get_empty_cells.return_value = [[0, 0], [0, 1]]
        mock_game_obj.is_won.return_value = [True]
        no_choice = self.player.get_choice(mock_game_obj)
        self.assertFalse(no_choice)

    def test_2_get_choice(self):
        """
            Verify get choice when the game board has no options
        """
        mock_game_obj = self.mock_game_obj
        mock_game_obj.get_empty_cells.return_value = []
        mock_game_obj.is_won.return_value = [False]
        no_choice = self.player.get_choice(mock_game_obj)
        self.assertFalse(no_choice)

    @patch("builtins.print")
    def test_3_get_choice(self, mock_print):
        """
            Verify get_choice returns the right cells from the board
        """
        self.player.name = "Bot"
        mock_game_obj = self.mock_game_obj
        mock_game_obj.get_empty_cells.return_value = [[""]] * 9
        mock_game_obj.is_won.return_value = False
        choice = self.player.get_choice(mock_game_obj)
        self.assertTrue(choice > 0 and choice < 10)
        mock_print.assert_called_with(f"{self.player.name}'s choice: {choice}")

    @patch("builtins.print")
    def test_4_get_choice(self, mock_print):
        """
            Verify get_choice returns new options from the board
        """
        self.player._minimax = MagicMock()
        self.player.name = "Bot"
        mock_game_obj = self.mock_game_obj
        self.mock_game_obj.get_empty_cells.return_value = [[""]] * 7
        self.mock_game_obj.is_won.return_value = False
        self.player._minimax.return_value = [1, 2]
        choice = self.player.get_choice(mock_game_obj)
        self.assertTrue(6)
        mock_print.assert_called_with(f"{self.player.name}'s choice: {choice}")

class TestMiniMaxAlgn(unittest.TestCase):
    
    def setUp(self):
        """
            Inits setup
        """
        self.player = BotPlayer("O")
        self.mock_game_obj = TicTacToe()

    def test_0_mini_max(self):
        """
            Verify the algorithm blocks the user's move against winning
        """
        mock_game_obj = self.mock_game_obj
        mock_game_obj.mark_moves("X", 1)
        mock_game_obj.mark_moves("X", 2)
        depth = len(mock_game_obj.get_empty_cells())
        pos = self.player._minimax(mock_game_obj.board, depth, self.mock_game_obj, True)
        x, y = pos[0], pos[1]
        self.assertTrue(x == 0 and y == 2)
    
    def test_1_mini_max(self):
        """
            Verify the algorithm blocks the user's move against winning
        """
        mock_game_obj = self.mock_game_obj
        mock_game_obj.mark_moves("X", 1)
        mock_game_obj.mark_moves("X", 4)
        depth = len(mock_game_obj.get_empty_cells())
        pos = self.player._minimax(mock_game_obj.board, depth, self.mock_game_obj, True)
        x, y = pos[1], pos[1]
        self.assertTrue(x == 1 and y == 1)

    def test_2_mini_max(self):
        """
            Verify the algorithm wins the game when it there is an option
        """
        mock_game_obj = self.mock_game_obj
        mock_game_obj.mark_moves("O", 1)
        mock_game_obj.mark_moves("O", 2)
        depth = len(mock_game_obj.get_empty_cells())
        pos = self.player._minimax(mock_game_obj.board, depth, self.mock_game_obj, True)
        x, y = pos[0], pos[1]
        self.assertTrue(x == 0 and y == 2)

if __name__ == "__main__":
    unittest.main()

