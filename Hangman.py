import random
#BONUS gives the user the ability to solve thw whole word if they want to
#BONUS2 sorts the guessed letters
#Binus3 User can not guess a non letter character
class Hangman:
    def __init__(self):
        """Set up the hangman game by getting the word to guess and initializing the game's state"""
        self.setWord(self.getWord())    #Calls the get word functions and gives it get word as an argument
        self.gameWon = False    #"records if the game is over by way of victory. Starts false as user has not guessed anything to be correct as of yet and thererfore not won"
        self.gameLost = False   #"Same as the latter but the inverse. If the game is over by way of loss and is false as the user has not begun"
        self.errorCount = 0     #"amounts of errors the user has made. initalised before any inputs therefore 0"
        self.GUESS_LIMIT = 6    #"The limit of errors for the user to make which you have set to six the amount of wrong letters a person can guess"

    def setWord(self, word):
        """Sets the given word as the word to guess, updating the working word and the list of already guessed letters as well."""
        self.wordToGuess = word.lower() #makes the word to guess all lower case and sets it to self.wordToGuess
        self.workingWord = ["-"]*len(self.wordToGuess) #creates the inital hangman -s string at the length of the correct word
        self.guessedAlready = [] #creats a list we will add the already guessed letters

#The functions above this point are "given," you don't need to modify them.
    
    def getWord(self):
        with open("USAD.py", "r") as file:
            allText = file.read()
            words = list(map(str, allText.split()))
            return random.choice(words)
    def getTextPerson(self, stage):
        str = ""
        if(not(isinstance(stage, int))):
            return "invalid"
        if stage >= 1:
            str = str + " o"
        if stage >= 2:
            str = str + "\n/"
        if stage >= 3:
            str = str + "|"
        if stage >= 4:
            str = str + "\ \n"
        if stage >= 5:
            str = str + "/"
        if stage >= 6:
            str = str + " \ "
        if stage > 6 :
            return "invalid"
        return str

    def allowableGuess(self, guess):
        return (len(guess) == 1) and (not guess in self.guessedAlready) and (guess.isalpha())
    def updateGame(self, guess):
        """Updates the game's state in response to the provided guess. Updates workingWord, guessedAlready, errorCount, and whether the game is won or lost."""
        self.guessedAlready.append(guess)
        list.sort(self.guessedAlready)
        x = 0
        y = 1
        for i in self.wordToGuess:
            if i == guess:
                self.workingWord[x] = guess
                y = 0
            x = x + 1
            if self.wordToGuess == ''.join([str(elem) for elem in self.workingWord]):
                self.gameWon = True
                
        if y == 1:
            self.errorCount = self.errorCount + 1
            if self.errorCount == self.GUESS_LIMIT:
                self.gameLost = True
    def solve(self):
        guess = input("Give me the full word: ").lower()
        if guess == self.wordToGuess:
            self.gameWon = True
        else:
            self.errorCount = self.errorCount + 1
        "FIX LIST SO IT DISLPAYS CORRECT ANSWER"
###Functions below this point assume that the game is being played on the terminal, and can use print and input.
    def showInTerminal(self):
        print(self.workingWord)
        print(self.guessedAlready)
        print(self.getTextPerson(self.errorCount))
    def getGuessFromTerminal(self):
        """Gets the next guess from the user. Returns the user's guess if and only if the guess is allowable (i.e., it repeats untill an allowable guess is given)."""
        guess = input("Give me a single letter or type SOLVE to guess right now: ").lower()
        if guess == "solve":
            self.solve()
        elif self.allowableGuess(guess):
            self.updateGame(guess)
        else:
            return
    def playGame(self):
        """Instructs the game to play itself with the user in the terminal."""
        print(self.workingWord)
        while (not self.gameWon) and (not self.gameLost):
            self.getGuessFromTerminal()
            self.showInTerminal()        
        if self.gameWon:
            print("Great job")
        else:

            print("W  A  S  T  E  D")
            print(self.wordToGuess)
if __name__ == "__main__":
    game = Hangman()
    game.playGame()
