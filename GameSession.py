
class GameSession:
    def __init__(self):
        self.field = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.turn = "❌"
        self.last_turn = None
        self.message_turn = None

    def make_turn(self, row, col):
        if self.field[row][col] != " ":
            return False
        self.field[row][col] = self.turn
        return True

    def switch_turn(self):
        self.last_turn = self.turn
        self.turn = "⭕️" if self.turn == "❌" else "❌"

    def check_win(self):
        global val1
        win_combos = [
            [[0, 0], [0, 1], [0, 2]],
            [[1, 0], [1, 1], [1, 2]],
            [[2, 0], [2, 1], [2, 2]],
            [[0, 0], [1, 0], [2, 0]],
            [[0, 1], [1, 1], [2, 1]],
            [[0, 2], [1, 2], [2, 2]],
            [[0, 0], [1, 1], [2, 2]],
            [[0, 2], [1, 1], [2, 0]],
        ]
        for combo in win_combos:
            a, b, c = combo
            val1 = self.field[a[0]][a[1]]
            val2 = self.field[b[0]][b[1]]
            val3 = self.field[c[0]][c[1]]
            if val1 == val2 == val3 and val1 != " ":
                self.winner = val1
                return True
        return False

    def is_draw(self):
        for row in self.field:
            if " " in row:
                return False
        return True        

    def clear(self):
        self.field = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

game = GameSession()

