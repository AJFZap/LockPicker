"""
Holds the logic of all the buttons from the different menus.
"""

from kivy.uix.relativelayout import RelativeLayout
from kivy.clock import Clock

def on_press_play(self):
    """
    Starts the game by making a new cipher number and starts the clock from the timer.
    """
    # Main menu music stops
    self.mainMenu_audio.stop()
    # Sound of the button when clicked.
    self.buttonClick_audio.play()
    # Ingame music starts.
    self.ingame_audio.play()

    # Creates a secret number.
    self.CipherNumber()

    # Hides the Main Menu.
    self.ids["menu_layout"].opacity = 0
    
    # Sets the gameState and starts the Timer.
    self.gameStarted = True
    Clock.schedule_interval(self.Timer, 0.01)
    Clock.schedule_interval(self.PlayGame, 0.01)


def retry_game(self):
    """
    Restarts the game at the difficulty is being played.
    """
    # Stops the music from either win or lose screen.
    self.win_audio.stop()
    self.gameOver_audio.stop()

    # Sound of the button when clicked.
    self.buttonClick_audio.play()

    # Ingame music starts.
    self.ingame_audio.play()

    # Set the opacity of the menus back to 0 }
    self.ids["cipher_unlocked"].opacity = 0
    self.ids["over_guesses"].opacity = 0
    self.ids["over_menu_lose"].opacity = 0
    
    # Restarts the cipher number, the guesses, and the gameState.
    self.cipherNumber = ''
    self.guesses = 10
    self.ids['guesses'].text = f"Guesses: {self.guesses}"
    self.time = 25.00
    self.gameOver = False

    # Turns the background of the ciphers white and the value of the ciphers to 0.
    self.ids['firstCipher'].background_color = (1, 1, 1, 1)
    self.ids['secondCipher'].background_color = (1, 1, 1, 1)
    self.ids['thirdCipher'].background_color = (1, 1, 1, 1)
    
    self.cipherOne = 0
    self.cipherTwo = 0
    self.cipherThree = 0

    # Calls the function to get a new cipher code and start the game again.
    self.on_press_play()

def main_menu(self):
    """
    Goes back to the main menu, reseting the game.
    """
    # Stops the music from either win or lose screen.
    self.win_audio.stop()
    self.gameOver_audio.stop()
    
    # Sound of the button when clicked.
    self.buttonClick_audio.play()

    # Play Menu music again.
    self.mainMenu_audio.play()
    self.mainMenu_audio.loop = True

     # Set the opacity of the menus back to 0 }
    self.ids["cipher_unlocked"].opacity = 0
    self.ids["over_guesses"].opacity = 0
    self.ids["over_menu_lose"].opacity = 0
    self.ids['tutorial_menu'].opacity = 0
    
    # Restarts the cipher number, the guesses, and the gameState.
    self.cipherNumber = ''
    self.guesses = 10
    self.ids['guesses'].text = f"Guesses: {self.guesses}"
    self.time = 25.00
    self.gameOver = False

    # Turns the background of the ciphers white and the value of the ciphers to 0.
    self.ids['firstCipher'].background_color = (1, 1, 1, 1)
    self.ids['secondCipher'].background_color = (1, 1, 1, 1)
    self.ids['thirdCipher'].background_color = (1, 1, 1, 1)
    
    self.cipherOne = 0
    self.cipherTwo = 0
    self.cipherThree = 0

    # Puts the Main Menu on screen.

    self.ids["menu_layout"].opacity = 1

def Tutorial(self):
    """
    Displays the tutorial images.
    """
    # Sound of the button when clicked.
    self.buttonClick_audio.play()

    # Hides the Menu and show the tutorial.
    self.ids['menu_layout'].opacity = 0
    self.ids['tutorial_menu'].opacity = 1

    # When clicked it always shows the first image and resets the image list number.
    self.ids['tutorial_menu'].ids['display'].tutorialDisplayed = "Images/Tutorial images/Tutorial-image-1.png"
    self.currentImage = 0
    self.ids['tutorial_menu'].ids['left_arrow'].img = "Images/Tutorial images/Celtic-Arrow-left-disabled.png"

def PrevTutorial(self):
    """
    Changes the image that is being displayed in the tutorial menu to the previous one.
    """
    # Sound of the button when clicked.
    self.buttonClick_audio.play()

    # Reduces the image list number and displays the previous image.
    self.currentImage -= 1
    self.ids['tutorial_menu'].ids['display'].tutorialDisplayed = f"Images/Tutorial images/{self.tutorialImages[self.currentImage]}"
    
    if self.currentImage > 0:
        # Enables the right arrow to function and changes its color to the enabled arrow one.
        self.ids['tutorial_menu'].ids['right_arrow'].disabled = False
        self.ids['tutorial_menu'].ids['right_arrow'].img = "Images/Tutorial images/Celtic-Arrow-right.png"
    elif self.currentImage == 0:
        # When there is no more previous images it disables itself and changes its color.
        self.ids['tutorial_menu'].ids['left_arrow'].disabled = True
        self.ids['tutorial_menu'].ids['left_arrow'].img = "Images/Tutorial images/Celtic-Arrow-left-disabled.png"
        

def NextTutorial(self):
    """
    Changes the image that is being displayed in the tutorial menu to the next one.
    """
    # Sound of the button when clicked.
    self.buttonClick_audio.play()

    # Increments the image list number and displays the next image.
    self.currentImage += 1
    self.ids['tutorial_menu'].ids['display'].tutorialDisplayed = f"Images/Tutorial images/{self.tutorialImages[self.currentImage]}"

    if self.currentImage == 7:
        # Enables the left arrow to function and changes its color to the enabled arrow one.
        self.ids['tutorial_menu'].ids['right_arrow'].disabled = True
        self.ids['tutorial_menu'].ids['right_arrow'].img = "Images/Tutorial images/Celtic-Arrow-right-disabled.png"
    else:
        # When there is no more next images it disables itself and changes its color.
        self.ids['tutorial_menu'].ids['left_arrow'].disabled = False
        self.ids['tutorial_menu'].ids['left_arrow'].img = "Images/Tutorial images/Celtic-Arrow-left.png"
    
