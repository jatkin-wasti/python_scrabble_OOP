class ScrabbleDict:  # Creating the class that will hold the letters and their values
    def __init__(self):
        # We can iterate through these lists and assign relevant scores in our other class
        self.one_point = ["a", "e", "i", "o", "u", "l", "n", "r", "s", "t"]
        self.two_points = ["d", "g"]
        self.three_points = ["b", "c", "m", "p"]
        self.four_points = ["f", "h", "v", "w", "y"]
        self.five_points = ["k"]
        self.eight_points = ["j", "x"]
        self.ten_points = ["q", "z"]
