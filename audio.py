"""
Holds all the code that makes the audio for the game.
"""
from kivy.core.audio import SoundLoader


def init_audio(self):
    """
    Initiates the audio files.
    """
    self.mainMenu_audio = SoundLoader.load("Sounds/Main_Menu_theme.mp3")
    self.buttonClick_audio = SoundLoader.load("Sounds/lock-sound.mp3")
    self.turnDial_audio = SoundLoader.load("Sounds/Click-sound.mp3")
    self.locked_audio = SoundLoader.load("Sounds/Unlock-failed.mp3")
    self.unlocked_audio = SoundLoader.load("Sounds/Unlocked-succesfully.mp3")
    self.ingame_audio = SoundLoader.load("Sounds/Ingame_song.mp3")
    self.win_audio = SoundLoader.load("Sounds/win-song.mp3")
    self.gameOver_audio = SoundLoader.load("Sounds/lose-song.mp3")

    self.mainMenu_audio.volume = 0.75
    self.buttonClick_audio.volume = 0.5
    self.turnDial_audio.volume = 0.5
    self.locked_audio.volume = 1
    self.unlocked_audio.volume = 1
    self.ingame_audio.volume = 0.75
    self.gameOver_audio.volume = 0.75