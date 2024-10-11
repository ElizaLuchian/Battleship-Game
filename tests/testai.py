import unittest
from gameservices.ai import Ai
from board.board import Board
from board.point import Point


class TestAi(unittest.TestCase):

    def setUp(self):
        self.board1 = Board()
        self.board2 = Board()
        self.ai = Ai(self.board2, self.board1)

    def test_init(self):
        self.assertIsInstance(self.ai._board, Board)
        self.assertIsInstance(self.ai._player_board, Board)
        self.assertEqual(len(self.ai._moves_queue), 0)

    def test_choose_move_random(self):
        self.ai.choose_move()  # test if it runs without errors

    def test_choose_move_smart(self):
        self.ai._moves_queue = [Point(1, 1), Point(2, 2)]
        self.ai.choose_move()  # test if it runs without errors
        self.assertTrue(self.board1.was_revealed(Point(2, 2)))
        self.assertEqual(len(self.ai._moves_queue), 1)

    def test_random_move(self):
        move_found = self.ai.random_move(False)
        self.assertTrue(move_found)

    def test_smart_move(self):
        self.ai._moves_queue = [Point(1, 1), Point(2, 2)]
        move_found = self.ai.smart_move(False)
        self.assertTrue(move_found)

    def test_hit_player(self):
        move = Point(2, 2)
        self.board1.drawship(move, move, 1)
        self.assertEqual(self.board1.ship_points, 15)
        self.ai.hit_player(move)
        self.assertEqual(self.board1.ship_points, 14)


if __name__ == '__main__':
    unittest.main()
