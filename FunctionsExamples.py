#Install playsound3 with the following command: pip install playsound3
#You will also need the neccessary sound files, obviously.
from playsound3 import playsound
import librosa
import soundfile as sf

def boop():
    print("BOOP")
    playsound("sounds/boop.mp3")

def play_boop_faster(speed_factor: float):
    # Load audio
    y, sr = librosa.load("sounds/boop.mp3", sr=None)
    # Time-stretch audio
    y_fast = librosa.effects.time_stretch(y, rate=speed_factor)
    # Save temporary fast audio file
    #sf.write("sounds/boop.mp3", y_fast, sr)
    # Play using playsound3
    playsound("sounds/boop.mp3")

def gonk():
    print("GONK")
    playsound("sounds/gonk.mp3")

def beep():
    print("BEEP")
    playsound("sounds/beep.mp3")

def weeo():
    print("WEEOOO")
    playsound("sounds/weeo.mp3")


def woop():
    print("WOOP")
    playsound("sounds/woop.mp3")


def goodmorning():
    print("GOOD MORNING")
    playsound("sounds/GoodMorning.mp3")


def pigeon():
    print("PIGEON")
    playsound("sounds/pigeon.mp3")


boop()
beep()
boop()
gonk()
play_boop_faster(2.0)
play_boop_faster(0.2)
boop()
boop()
boop()
gonk()
boop()
pigeon()
boop()
weeo()
woop()
woop()
pigeon()
gonk()
gonk()
gonk()
goodmorning()