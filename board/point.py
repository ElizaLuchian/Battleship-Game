class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        """
        Function returns a string type to choose the move
        :return:
        """
        arr = "ABCDEFGHIJ"
        return "x: " + str(self.x) + " y: " + arr[self.y-1]
