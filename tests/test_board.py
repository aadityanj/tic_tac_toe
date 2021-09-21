from app.constants import PLAYER_MARKS
from unittest.mock import patch
from app.board import Board
import unittest

class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        self.board_obj = Board()

    @patch("builtins.print")
    def test_print_board_info(self, mock_print):
        """Verify Print_board_info method"""
        self.board_obj.print_board_info()
        mock_print.assert_called()
    
    def test_mark_moves(self):
        """Verify Mark Moves method"""
        self.board_obj.mark_moves(PLAYER_MARKS["1"], 1)
        self.assertEqual(self.board_obj.board[0][0], PLAYER_MARKS["1"])
    
    @patch("builtins.print")
    def test_print_current_board(self, mock_print):
        """Verify print_current_board method"""
        self.board_obj.print_current_board()
        mock_print.assert_called()
    
    def test_is_valid_cell_no(self):
        """Verify is_valid_cell_no method"""
        self.assertTrue(self.board_obj.is_valid_cell_no(9))
        self.assertFalse(self.board_obj.is_valid_cell_no(0))

    def test_is_cell_available(self):
        """Verify is_cell_available method"""
        self.board_obj.board[0][0] = PLAYER_MARKS["1"]
        self.assertEqual(2, self.board_obj.is_cell_available(2))
        self.assertIsNone(self.board_obj.is_cell_available(1))

    def test_get_empty_cells(self):
        """Verify get_empty_cells method"""
        self.board_obj.board[0][0] = PLAYER_MARKS["1"]
        cells = self.board_obj.get_empty_cells()
        self.assertEqual(8, len(cells))