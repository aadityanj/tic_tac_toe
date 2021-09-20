import unittest
from unittest import mock
from app.players.human_player import HumanPlayer
import io
from app.main import TicTacToe


class TestHumanPlayer(unittest.TestCase):
    
    def setUp(self):
        self.player = HumanPlayer("X")
    
    @mock.patch("builtins.print")
    @mock.patch("builtins.input", side_effect=["123Adithya", "Adithya"])
    def test_set_player_info(self, mock_input, mock_print):
        """
            Assert the expected behaviour for both valid and invalid name
        """
        is_done = self.player.set_player_info("First Player")
        mock_print.assert_called_with("Invalid Name")
        self.assertEqual(self.player.name, 'Adithya')
        self.assertTrue(is_done)

    @mock.patch("builtins.print")
    @mock.patch("builtins.input", side_effect=["1", "2", "3"])
    def test_get_choice(self, mock_input, mock_print):
        """
            Verify get_choice prints error message for wrong choice
        """
        self.player.name = "Adithya"
        mock_game_obj = TicTacToe()
        mock_game_obj.is_valid_cell_no = mock.MagicMock(name="us_valid_cell_no")
        mock_game_obj.is_cell_available = mock.MagicMock(name="is_cell_availble")
        mock_game_obj.is_valid_cell_no.side_effect = self.cell_no_side_effect
        mock_game_obj.is_cell_available.side_effect = self.cell_available_side_effect
        position = self.player.get_choice(mock_game_obj)
        mock_print.assert_called_with("Cell is already occupied")
        self.assertEqual(3, position)
        
    
    def cell_no_side_effect(self, pos):
        """
            dummy conditions to cover the test case
            Args:
                pos: Position of the board
            Returns:
                bool: True if it is valid pos
        """
        if pos == 1: return False
        elif pos == 2: return True
        elif pos == 3: return True
    
    def cell_available_side_effect(self, pos):
        """
            dummy conditions to cover the test case
            Args:
                pos: Position of the board
            Returns:
                bool: True if cell is available
        """
        if pos == 2: return False
        elif pos == 3: return True

if __name__ == "__main__":
    unittest.main()