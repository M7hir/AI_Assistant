import pyttsx3
# import openai
import speech_recognition as sr
# from Features import *
import Features as fu
import Keys
import Web_Search

# openai.api_key = Keys.Api

engine = pyttsx3.init()  # initialise pyttsx3
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0-2 range for different voices
voice_speed = 140  # setting speed
engine.setProperty('rate', voice_speed)


def TakeCommand():
    """Listen for a command from the user and return it as text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print(": Recognising...")
        que = r.recognize_google(audio, language='en-in')
        print(f"Your command :{que}\n")
    except Exception:
        return ""
    return que.lower()


# if __name__ == "__main__":
def MainEx():
    # wishme()
    while True:
        # query = TakeCommand().lower()  
        query = str(input(">> "))
        print(query)

        if "good morning" in query:
            fu.Speak("Good Morning Sir")
        elif "time" in query:
            fu.time()
        elif "thank you" in query:
            fu.Speak("My pleasure Sir")
        elif "date" in query:
            fu.date()
            # open browser
        elif "open brave" in query:
            path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
            fu.open_application(path)

        elif "open youtube" in query:
            link = "youtube.com"
            fu.open_link(link)

        elif "what is" in query:
            Web_Search.googleSearch(query)

        elif "stop" in query:
            fu.Speak("good bye")
            break

        elif "in youtube" in query:
            Query = query.replace("in youtube", "")
            query = query.replace("search", "")
            query = query.replace("in youtube", "")
            Web_Search.youtubeSearch(query)

        # elif query:
        #     fu.openAi(query)


# MainEx()