# Task
- Create a scrabble word calculator that gives the correct score depending on the given string
## Solution
### ScrabbleDict class
- First we create a Dictionary containing all of the letters and how many points they are worth
- We could use an actual dictionary for this but for simplicity we will group together all of the
letters that share a point value
```
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
```
### ScrabbleCalculator class
- Now we need to actually do something with this dictionary
- First, we'll import and extend the ScrabbleDict class so that we can inherit those class attributes
- It is good practise to use some RegEx to check user input and normalise it
- Therefore when the object is created, we will store the word provided in all lowercase seeing as our
dictionary uses lowercase letters
- Then we can make our score_check method that will actually calculate our score
- It will do this by looping through every letter of the word and look up which list it's stored in in our 
dictionary
- Then we simply add the score for letters in that list to the current score and continue with the next letter
- If the letter cannot be found in any of the lists, it isn't a letter so we tell the user to input letters next time
```
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
```
- Finally, we need to test to see if this function works with expected and unexpected values so we create two
new ScrabbleCalculator objects for this purpose
```
test = ScrabbleCalculator("Amazing")  # Testing for an expected input
print(test.score_check())
test2 = ScrabbleCalculator("aglamgl!26262")  # Testing for an unexpected input
print(test2.score_check())
```
- These tests pass so we know our classes and their functions work as intended!