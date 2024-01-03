# import os
from Main import *
from Features import Speak


def weakUp():
    query = str(input(">> "))

    if "wake up" in query:
        # os.startfile(r"C:/Users/key/Desktop/Ai_Project/Main.py")
        wU = "i'm wake up what do you want me to do"
        print(wU)
        Speak(wU)
        MainEx()


while True:
    weakUp()
    # que = TakeCommand().lower()

    # if "stop" or "go to sleep" in que:
    #     Speak("i am shutting down take care")
    #     break