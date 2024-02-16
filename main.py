from kivy.lang.builder import Builder
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.clock import Clock
from kivy.properties import NumericProperty
from random import randint

Builder.load_file("menu.kv")
Builder.load_file("gameover.kv")
Builder.load_file("guessesover.kv")
Builder.load_file("unlocked.kv")
Builder.load_file("tutorial.kv")

class LockPicker(RelativeLayout):
    from menu_buttons import on_press_play, retry_game, main_menu, Tutorial, PrevTutorial, NextTutorial
    from audio import init_audio

    cipherOne = NumericProperty()
    cipherTwo = NumericProperty()
    cipherThree = NumericProperty()
    cipherNumber = ''

    guesses = 10
    time = 25.00

    gameOver = False
    gameStarted = False

    tutorialImages = ["Tutorial-image-1.png", "Tutorial-image-2.png", "Tutorial-image-3.png", "Tutorial-image-4.png", "Tutorial-image-5.png", "Tutorial-image-6.png", "Tutorial-image-7.png", "Tutorial-image-8.png"]
    currentImage = 0

    def __init__(self, **kwargs):
        super(LockPicker, self).__init__(**kwargs)
        self.init_audio()
        self.mainMenu_audio.play()
        self.mainMenu_audio.loop = True

    def Timer(self, dt):
        """
        Decreases the time by 0.01 and updates the Clock of the app. And gives a game over if the clock reaches 0.
        """
        self.time -= 0.01
        self.ids['clock'].text = f"Time: {round(self.time, 2):.2f}" # :.2f is to display the trailing 0s. So the word Tiem doesn't move much.
        
        if self.time < 0.00: # If the time limit is surpassed the game is over
            self.ids["over_menu_lose"].opacity = 1
            self.gameStarted = False
            self.gameOver = True
            Clock.unschedule(self.Timer)
            self.ingame_audio.stop()
            self.gameOver_audio.play()
    
    def PlayGame(self, dt):
        """
        Checks the GameState, if the game has started then it enables the buttons, if not and the game is over, then it disables them.
        """
        if self.gameStarted == True:
            # Enables the buttons of the game.
            self.ids['moreOne'].disabled = False
            self.ids['moreTwo'].disabled = False
            self.ids['moreThree'].disabled = False
            self.ids['lessOne'].disabled = False
            self.ids['lessTwo'].disabled = False
            self.ids['lessThree'].disabled = False
            self.ids['unlock_button'].disabled = False
        else:
            self.ids['moreOne'].disabled = True
            self.ids['moreTwo'].disabled = True
            self.ids['moreThree'].disabled = True
            self.ids['lessOne'].disabled = True
            self.ids['lessTwo'].disabled = True
            self.ids['lessThree'].disabled = True
            self.ids['unlock_button'].disabled = True

    def CipherNumber(self):
        """
        Each time the program is run or the player retries a random number is generated to be deciphered.
        """
        firstNum = randint(0, 9)
        secondNum = randint(0, 9)
        thirdNum = randint(0, 9)

        self.cipherNumber = str(firstNum) + str(secondNum) + str(thirdNum)
        
        #self.ids['clock'].text = "Time: " + self.cipherNumber // Debugging to know the Cipher code.

    def ArrowUp(self, id):
        """
        When the top arrow of a number is pressed the number goes up until it's 9, if it's higher it goes back to 0.
        """
        # Sound when clicked.
        self.turnDial_audio.play()

        if id == 'moreOne':
            if self.cipherOne >= 9:
                self.cipherOne = 0
            else:
                self.cipherOne += 1
        
        elif id == 'moreTwo':
            if self.cipherTwo >= 9:
                self.cipherTwo = 0
            else:
                self.cipherTwo += 1
        
        elif id == 'moreThree':
            if self.cipherThree >= 9:
                self.cipherThree = 0
            else:
                self.cipherThree += 1

    def ArrowDown(self, id):
        """
        When the down arrow of a number is pressed the number goes down until it's 0, if it's lower it goes back to 9.
        """
        # Sound when clicked.
        self.turnDial_audio.play()

        if id == 'lessOne':
            if self.cipherOne <= 0:
                self.cipherOne = 9
            else:
                self.cipherOne -= 1
        
        elif id == 'lessTwo':
            if self.cipherTwo <= 0:
                self.cipherTwo = 9
            else:
                self.cipherTwo -= 1
        
        elif id == 'lessThree':
            if self.cipherThree <= 0:
                self.cipherThree = 9
            else:
                self.cipherThree -= 1

    def Unlock(self):
        """
        When te Unlock button it's clicked it checks if the input by the user is the same as the random cipher.
        """
        for i in range(len(self.cipherNumber)):
            if str(self.cipherOne) == self.cipherNumber[0]:
                self.ids['firstCipher'].background_color = (0, 1, 0, 1)
            elif str(self.cipherOne) in self.cipherNumber:
                self.ids['firstCipher'].background_color = (1, 1, 0, 1)
            else:
                self.ids['firstCipher'].background_color = (1, 0, 0, 1)

        for i in range(len(self.cipherNumber)):
            if str(self.cipherTwo) == self.cipherNumber[1]:
                self.ids['secondCipher'].background_color = (0, 1, 0, 1)
            elif str(self.cipherTwo) in self.cipherNumber:
                self.ids['secondCipher'].background_color = (1, 1, 0, 1)
            else:
                self.ids['secondCipher'].background_color = (1, 0, 0, 1)

        for i in range(len(self.cipherNumber)):
            if str(self.cipherThree) == self.cipherNumber[2]:
                self.ids['thirdCipher'].background_color = (0, 1, 0, 1)
            elif str(self.cipherThree) in self.cipherNumber:
                self.ids['thirdCipher'].background_color = (1, 1, 0, 1)
            else:
                self.ids['thirdCipher'].background_color = (1, 0, 0, 1)


        # Game Over states for both, running out of guesses or Winning by decoding the cipher.

        if str(self.cipherOne) + str(self.cipherTwo) + str(self.cipherThree) == self.cipherNumber:
            # Play Unlocked Cipher sound and victory song.
            self.unlocked_audio.play()
            self.win_audio.play()

            Clock.unschedule(self.Timer)
            self.ingame_audio.stop()
            self.ids["cipher_unlocked"].opacity = 1
            self.gameOver = True
            self.gameStarted = False

        else:
            # Play failed unlock sound.
            self.locked_audio.play()
            if self.guesses > 1:
                self.guesses -= 1
                self.ids['guesses'].text = f"Guesses: {self.guesses}"
            else:
                self.gameOver = True
                self.gameStarted = False
                Clock.unschedule(self.Timer)
                self.ingame_audio.stop()
                self.gameOver_audio.play()
                self.ids["over_guesses"].opacity = 1
                

class LockPickerApp(App):
    pass

if __name__ == "__main__":
    LockPickerApp().run()

