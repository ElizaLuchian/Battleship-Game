from board.board import Board
from gameservices.game import Game
from ui.ui import Ui
from gameservices.ai import Ai


def main():
    _board = Board()
    _ai_board = Board()
    _ai = Ai(_ai_board, _board)
    _game = Game(_board, _ai_board, _ai)
    _ui = Ui(_game)

    _ui.start()


main()
