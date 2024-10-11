import random

from board.board import Board
from board.point import Point


class Ai:
    def __init__(self, board: Board, player_board: Board):
        self._board = board
        self._player_board = player_board
        self._moves_queue = []

        self.decide_ship()

    def decide_ship(self):
        """
        Decides the position of the ships in all scenarios for the Ai board
        :return:
        """
        ships = [5, 4, 3, 2, 1]
        for ship in ships:
            found = False
            while found is False:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                try:
                    self._board.validate_point(Point(x, y))
                except:
                    continue

                available_directions = [
                    [Point(x - ship + 1, y), "up"],  # sus
                    [Point(x, y + ship - 1), "right"],  # dreapta
                    [Point(x + ship - 1, y), "down"],  # jos
                    [Point(x, y - ship + 1), "left"]  # stanga
                ]

                for el in available_directions:
                    p = el[0]
                    try:
                        self._board.validate_point(p)
                        self._board.validate_ship(p, Point(x, y))

                        self._board.drawship(Point(x, y), p, ship)

                        found = True
                        break
                    except:
                        pass

    def choose_move(self):
        """
        Function that chooses the move for the Ai
        :return:
        """
        move_found = False
        while move_found is False:
            if len(self._moves_queue) < 1:
                move_found = self.random_move(move_found)
            else:
                move_found = self.smart_move(move_found)

    def smart_move(self, move_found):
        """
        Function that chooses the move for the Ai
        :param move_found:
        :return:
        """
        while move_found is False:
            try:
                next_move = self._moves_queue.pop()
                self._player_board.validate_point(next_move)
                self.hit_player(next_move)
                move_found = True
            except:
                if len(self._moves_queue) < 1:
                    break
        return move_found

    def random_move(self, move_found):
        """
        Function marks a random move on the ai board
        :param move_found:
        :return:
        """
        while move_found is False:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            try:
                self._board.validate_point(Point(x, y))
                self.hit_player(Point(x, y))
                move_found = True
            except:
                continue
        return move_found

    def hit_player(self, move: Point):
        """
        Function that checks if the ai move hit the board of the player and then goes to put all the posible directions near that point
        on a moves_que array
        :param move: a move with coordinates
        :return:
        """
        previous_points = self._player_board.ship_points
        self._player_board.hit(move)
        new_points = self._player_board.ship_points

        if new_points < previous_points:
            dir = [
                Point(move.x - 1, move.y),
                Point(move.x + 1, move.y),
                Point(move.x, move.y - 1),
                Point(move.x, move.y + 1)
            ]

            for neighbour in dir:
                try:
                    self._player_board.validate_point(neighbour)
                    if self._player_board.was_revealed(neighbour) is False and neighbour not in self._moves_queue:
                        self._moves_queue.append(neighbour)
                except:
                    continue
