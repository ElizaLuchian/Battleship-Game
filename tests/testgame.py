import unittest
from gameservices.game import Game
from gameservices.ai import Ai
from board.board import Board
from board.point import Point


class TestGame(unittest.TestCase):

    def setUp(self):
        self.board1 = Board()
        self.board2 = Board()
        self.ai = Ai(self.board2, self.board1)
        self.game = Game(self.board1, self.board2, self.ai)

    def test_init(self):
        self.assertIsInstance(self.game.player_board, Board)
        self.assertIsInstance(self.game.ai_board, Board)
        self.assertIsInstance(self.game.ai, Ai)
        self.assertTrue(self.game.user_turn)

    def test_get_player_board(self):
        display_str = self.game.get_player_board()
        self.assertIsInstance(display_str, str)

    def test_get_winner_ai(self):
        self.game.player_board.ship_points = 0
        self.assertEqual(self.game.get_winner(), 'ai')

    def test_get_winner_player(self):
        self.game.ai_board.ship_points = 0
        self.assertEqual(self.game.get_winner(), 'player')

    def test_get_winner_none(self):
        self.assertIsNone(self.game.get_winner())

    def test_user_move(self):
        move = Point(2, 2)
        self.board2.drawship(move, move, 1)
        self.assertEqual(self.game.ai_board.ship_points, 15)
        self.game.user_move(move)
        self.assertEqual(self.game.ai_board.ship_points, 14)

    def test_ai_move(self):
        self.game.ai_move()  # just test if it runs without errors


if __name__ == '__main__':
    unittest.main()
