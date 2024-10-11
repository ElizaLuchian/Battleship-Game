import copy

from texttable import Texttable

from board.point import Point


class BoardException(Exception):
    def __init__(self, msg: str):
        self.message = msg

    def __str__(self):
        return self.message




class Board:
    def __init__(self):
        self._rows = 10
        self._columns = 10
        self._board = []
        self._revealed = []
        self._ship_revealed = [0, 0, 0, 0, 0]
        self.ship_points = 15

        self.initboard()
        pass

    def was_revealed(self, move: Point):
        """
        function that checks if a move was already revealed
        :param move: the move to be checked
        :return: nothing
        """
        return self._revealed[move.x][move.y]

    def hit(self, move: Point):
        """
        Function that checks if a move is a hit or not
        :param move: move to be chcked
        :return:
        """
        self._revealed[move.x][move.y] = True
        if self._board[move.x][move.y].isnumeric():
            self.ship_points -= 1
            self._ship_revealed[int(self._board[move.x][move.y])-1] += 1

    def initboard(self):
        """
        Function that initializes the board as a matrix of 10x10
        :return:
        """
        self._board = []
        for i in range(self._rows):
            row = []
            for j in range(self._columns):
                column = " "
                row.append(column)

            self._board.append(row)
        self._revealed = [[False for _ in range(self._rows)] for _ in range(self._columns)]

    def display(self, hide: bool):

        """
        Function that display the board in all the scenarios
        :param hide: a parameter that checks if the board is the ai board or the player board
        :return:
        """
        if hide is True:
            print("\n\n THE CURRENT AI BOARD \n\n")
        else:
            print("\n\n THE CURRENT PLAYER BOARD \n\n")

        table = Texttable()

        board = copy.deepcopy(self._board)

        for i in range(self._rows):
            for j in range(self._columns):
                if board[i][j].isnumeric():
                    if self._revealed[i][j] is False:
                        if hide is True: # the ai board
                            board[i][j] = ' '
                    else:
                        if self._ship_revealed[int(board[i][j]) - 1] < int(board[i][j]):
                            board[i][j] = '*'
                        else:
                            board[i][j] = 'X'
                elif self._revealed[i][j] is True:
                    board[i][j] = 'O'

        header = [' ']
        for char in range(ord("A"), ord("J") + 1):
            header.append(chr(char))

        table.add_row(header)

        for i in range(len(board)):
            arr = [str(i + 1)] + board[i]
            table.add_row(arr)

        return table.draw()

    def validate_point(self, point: Point):
        """
        Function that validates the coordinates of a point and also if it was already chosen in another round
        :param point: an object of type Point
        :return:
        """
        if point.y < 0 or point.y > self._columns:
            raise BoardException("invalid coordinate for y")

        if point.x < 0 or point.x > self._rows:
            raise BoardException("invalid coordinate for x")

        if self._revealed[point.x][point.y] is True:
            raise BoardException("[x, y] coordinate already used")

    def validate_ship(self, point1: Point, point2: Point):
        """
        Function that validates if a ship can be placed on the board
        :param point1: an object of type Point
        :param point2: an object of type Point
        :return:
        """
        if point1.x == point2.x:
            if point1.y > point2.y:
                point1, point2 = point2, point1
            for j in range(point1.y, point2.y + 1):
                if self._board[point1.x][j] != ' ':
                    raise BoardException("the space is occupied")

        else:
            if point1.x > point2.x:
                point1, point2 = point2, point1
            for i in range(point1.x, point2.x + 1):
                if self._board[i][point1.y] != ' ':
                    raise BoardException("the space is occupied")

    def drawship(self, point1: Point, point2: Point, value: int):
        """
        Function that draws a ship on the board
        :param point1:object of type Point
        :param point2:object of type Point
        :param value:on integer
        :return:
        """

        if point1.x == point2.x:
            if point1.y > point2.y:
                point1, point2 = point2, point1
            for j in range(point1.y, point2.y + 1):
                self._board[point1.x][j] = str(value)

        else:

            if point1.x > point2.x:
                point1, point2 = point2, point1
            for i in range(point1.x, point2.x + 1):
                self._board[i][point1.y] = str(value)

