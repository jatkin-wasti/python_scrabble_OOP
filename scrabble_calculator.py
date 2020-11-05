from scrabble import ScrabbleDict  # First we need to import the ScrabbleDict class


class ScrabbleCalculator(ScrabbleDict):  # Inheriting from the Parent class
    def __init__(self, word):  # Takes a word argument to calculate its score
        super().__init__()  # Using the parent classes initialisation
        self.score = 0  # Set the score to 0 to start with
        self.word = word.lower()  # using .lower() saves us having to check for capitals and lowercase in the dict

    def score_check(self):
        for letters in self.word:  # Loops through the word and increments the value with the appropriate score
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
            else:  # If the character received wasn't found in any of the dictionaries it must not be a letter
                return "Please only include letters!"  # So give the user some feedback
        return self.score  # Return the calculated score


test = ScrabbleCalculator("Amazing")  # Testing for an expected input
print(test.score_check())
test2 = ScrabbleCalculator("aglamgl!26262")  # Testing for an unexpected input
print(test2.score_check())
