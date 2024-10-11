from gameservices.ai import Ai
from board.board import Board
from board.point import Point


class Game:
    def __init__(self, board1: Board, board2: Board, ai: Ai):
        self.player_board = board1
        self.ai_board = board2
        self.ai = ai

        self.user_turn = True

    def get_player_board(self):
        """
        Function returns the display of player board
        :return:
        """
        return self.player_board.display(False)

    def get_winner(self):
        """
        The Function returns who is the winner of the game when there are no more ship points
        :return:
        """
        if self.player_board.ship_points == 0:
            return "ai"
        elif self.ai_board.ship_points == 0:
            return "player"
        else:
            return None

    def user_move(self, move: Point):
        """
        The Functions implements the user move
        :param move:
        :return:
        """
        self.ai_board.validate_point(move)
        self.ai_board.hit(move)

    def ai_move(self):
        """
        The Function implements ai move
        :return:
        """
        self.ai.choose_move()


