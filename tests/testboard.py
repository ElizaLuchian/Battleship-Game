import unittest
from board.board import Board, BoardException, Point


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_init(self):
        self.assertEqual(self.board._rows, 10)
        self.assertEqual(self.board._columns, 10)
        self.assertEqual(self.board.ship_points, 15)
        self.assertEqual(len(self.board._board), 10)
        self.assertEqual(len(self.board._board[0]), 10)
        self.assertEqual(len(self.board._revealed), 10)
        self.assertEqual(len(self.board._revealed[0]), 10)

    def test_was_revealed(self):
        move = Point(1, 1)
        self.assertFalse(self.board.was_revealed(move))
        self.board.hit(move)
        self.assertTrue(self.board.was_revealed(move))

    def test_hit(self):
        move = Point(2, 2)
        self.board.drawship(move, move, 1)
        self.assertEqual(self.board.ship_points, 15)
        self.board.hit(move)
        self.assertEqual(self.board.ship_points, 14)

    def test_initboard(self):
        self.board.initboard()
        self.assertEqual(len(self.board._board), 10)
        self.assertEqual(len(self.board._board[0]), 10)
        self.assertEqual(len(self.board._revealed), 10)
        self.assertEqual(len(self.board._revealed[0]), 10)

    def test_validate_point(self):
        move = Point(11, 0)
        with self.assertRaises(BoardException):
            self.board.validate_point(move)
        move = Point(0, 11)
        with self.assertRaises(BoardException):
            self.board.validate_point(move)
        move = Point(1, 1)
        self.board._revealed[1][1] = True
        with self.assertRaises(BoardException):
            self.board.validate_point(move)

    def test_validate_ship(self):
        self.board.validate_ship(Point(0, 0), Point(0, 1))
        self.board.drawship(Point(0, 0), Point(0, 1), 1)
        with self.assertRaises(BoardException):
            self.board.validate_ship(Point(0, 0), Point(0, 1))

    def test_drawship(self):
        self.board.drawship(Point(0, 0), Point(0, 1), 1)
        self.assertEqual(self.board._board[0][0], '1')
        self.assertEqual(self.board._board[0][1], '1')
        self.assertEqual(self.board._board[0][2], ' ')
        self.assertEqual(self.board._revealed[0][0], False)
        self.assertEqual(self.board._revealed[0][1], False)
        self.assertEqual(self.board._revealed[0][2], False)


if __name__ == '__main__':
    unittest.main()
