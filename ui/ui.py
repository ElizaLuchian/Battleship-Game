from board.board import *
from gameservices.game import Game


class Ui:
    def __init__(self, game: Game):
        self._game = game

    def start(self):
        print("Welcome to Battleship!")
        print(self._game.get_player_board())

        while True:
            try:
                print("1. Carrier length 5")
                self.decide_ship(5, 5)
                break
            except Exception as ex:
                print("Exception: " + str(ex))
        while True:
            try:
                print("2. Battleship length 4")
                self.decide_ship(4, 4)
                break
            except Exception as ex:
                print("Exception: " + str(ex))

        while True:
            try:
                print("3. Cruiser length 3")
                self.decide_ship(3, 3)
                break
            except Exception as ex:
                print("Exception: " + str(ex))

        while True:
            try:
                print("4. Submarine length 2")
                self.decide_ship(2, 2)
                break
            except Exception as ex:
                print("Exception: " + str(ex))

        while True:
            try:
                print("5. Pluta Destroyer length 1")
                self.decide_ship(1, 1)
                break
            except Exception as ex:
                print("Exception: " + str(ex))

        self.play()

    def decide_ship(self, length: int, value: int):
        x = int(input("X: ")) - 1
        y = input("Y: ")
        y = self.map_letter(y)
        y -= 1

        self._game.player_board.validate_point(Point(x, y))

        available_directions = [
            [Point(x - length + 1, y), "up"], # sus
            [Point(x, y + length - 1), "right"], # dreapta
            [Point(x + length - 1, y), "down"],  # jos
            [Point(x, y - length + 1), "left"] # stanga
        ]

        possible_directions = []
        for el in available_directions:
            p = el[0]
            try:
                self._game.player_board.validate_point(p)
                self._game.player_board.validate_ship(p, Point(x, y))

                indexed_at_1_point = Point(p.x + 1, p.y + 1)

                print("Possible end point(" + el[1] + "): " + str(indexed_at_1_point))
                possible_directions.append(p)
            except:
                pass

        point_option = int(input("point selected: ")) - 1

        if point_option < 0 or point_option > len(possible_directions):
            raise ValueError("invalid point option")

        self._game.player_board.drawship(Point(x, y), possible_directions[point_option], value)

        print(self._game.get_player_board())

    def map_letter(self, letter: str):
        letter = letter.upper()
        if letter == "A":
            return 1
        elif letter == "B":
            return 2
        elif letter == "C":
            return 3
        elif letter == "D":
            return 4
        elif letter == "E":
            return 5
        elif letter == "F":
            return 6
        elif letter == "G":
            return 7
        elif letter == "H":
            return 8
        elif letter == "I":
            return 9
        elif letter == "J":
            return 10

        raise ValueError("Invalid input.")

    def play(self):
        while self._game.get_winner() is None:
            while True:
                try:
                    self.do_round()
                    break
                except Exception as ex:
                    print("Exception: " + str(ex))

        winner = self._game.get_winner()
        print("The winner is: " + winner)

    def do_round(self):
        if self._game.user_turn:
            self.get_user_move_input()
            self._game.user_turn = not self._game.user_turn
        else:
            self.ai_move()
            self._game.user_turn = not self._game.user_turn

    def get_user_move_input(self):
        # input
        print(self._game.ai_board.display(True))

        x = int(input("X: ")) - 1
        y = input("Y: ")
        y = self.map_letter(y)
        y -= 1

        self._game.user_move(Point(x, y))
        print(self._game.ai_board.display(True))


    def ai_move(self):
        self._game.ai_move()
        print(self._game.player_board.display(False))