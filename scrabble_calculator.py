from scrabble import ScrabbleDict


class ScrabbleCalculator(ScrabbleDict):
    def __init__(self, word):
        super().__init__()
        self.score = 0
        self.word = word.lower()

    def score_check(self):
        for letters in self.word:
            if letters in self.one_point:
                self.score += 1
            elif letters in self.two_points:
                self.score += 2
            elif letters in self.three_points:
                self.score += 3
            elif letters in self.four_points:
                self.score += 4
            elif letters in self.five_points:
                self.score += 5
            elif letters in self.eight_points:
                self.score += 8
            elif letters in self.ten_points:
                self.score += 10
            else:
                return "Please only include letters!"
        return self.score


test = ScrabbleCalculator("Amazing")
print(test.score_check())
