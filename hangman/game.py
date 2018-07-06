class Game():

    def __init__(self, secret_word):
        self.secret_word  = secret_word.lower()                                 #add hangman figuire
        self.updating_word = self.create_updating_word()                        #not allowed to enter numbers
        self.location_array = []
        self.wrong_letters = []
        self.guesses = 10

    def play(self):
        print("Welcome to Hangman. you need to guess the letters you think will be in the word. \nYou have 10 lives!")
        print game.updating_word
        while game.guesses != 0 and not game.word_fully_guessed():
            game.set_letter()
            while game.repeated_letter_entry():
                print("You have already entered this letter, please enter another.")
                game.set_letter()
            if game.find_all_locations():
                game.insert_into_updating_word()
                print('You have %s guesses left') %(game.guesses)
                print ('Incorrect letters you have guessed: %s') %(game.wrong_letters)
                print game.updating_word
            else:
                game.add_to_wrong_letter_array()
                game.guesses = game.guesses - 1
                print('%s is incorrect') %(game.letter)
                print('You have %s guesses left') %(game.guesses)
                print ('Incorrect letters you have guessed: %s') %(game.wrong_letters)
                print game.updating_word
        if game.word_fully_guessed():
            print ('Congratulations for surviving, you managed to guess %s was the secret word!') %(game.secret_word)
        else:
            print('Unfortunatelly you were unable to guess that %s was the secret word! You have been hanged...') %(game.secret_word)

    def set_letter(self):
        self.letter = raw_input("Please enter your guess.  ").lower()
        while len(self.letter) != 1 or not self.letter.isalpha():
            self.letter = raw_input("Only enter one letter.  ").lower()

    def find_all_locations(self):
        for index, guess_letter in enumerate(self.secret_word):
            if self.letter == guess_letter:
                self.location_array.append(index)
        if self.letter in self.secret_word:
            return True
        else:
            return False

    def create_updating_word(self):
        length = len(self.secret_word)
        dashed_word = '_' * length
        return dashed_word

    def add_to_wrong_letter_array(self):
        self.wrong_letters.append(self.letter)                          #

    def insert_into_updating_word(self):
        self.updating_word = list(self.updating_word)
        for index in self.location_array:
            self.updating_word[index] = self.letter
        self.updating_word = ''.join(self.updating_word)
        self.location_array = []

    def repeated_letter_entry(self):
        if self.letter in self.wrong_letters:
            return True
        else:
            return False

    def word_fully_guessed(self):
        if '_' in self.updating_word:
            return False
        else:
            return True

#main body
game = Game("design")
game.play()
