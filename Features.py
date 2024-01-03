import os
import pygame
# import openai
import datetime
import webbrowser as wb
import subprocess as sp


def Speak(data):
    voice1 = "en-GB-SoniaNeural"
    filename = "data.mp3"
    extra_voice = 'en-GB-SoniaNeural'
    # Split the input text into chunks
    chunks = data.split()
    chunk_size = 100
    chunks = [chunks[i:i + chunk_size] for i in range(0, len(chunks), chunk_size)]

    # Convert and play each chunk
    for chunk in chunks:
        text = ' '.join(chunk)
        command1 = f'edge-tts --voice "{voice1}" --text "{text}" --write-media "{filename}"'
        os.system(command1)

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("data.mp3")

        try:
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

        except Exception as e:
            print(e)
        finally:
            pygame.mixer.music.stop()
            pygame.mixer.quit()
    return True


def time():
    """Speak the current time."""
    ti_me = datetime.datetime.now().strftime("%H:%M:%S")
    Speak(ti_me)
    print(ti_me)


def date():

    day = str(datetime.datetime.now().day)
    month = str(datetime.datetime.now().month)
    year = str(datetime.datetime.now().year)
    in_str = day + "/" + month + "/" + year
    Speak(f"Current date is {in_str}")
    # print(f"{day}/{month}/{year}")
    # Speak(in_str)
    # speak(month)
    # speak(year)


def open_application(app_path):
    sp.Popen([app_path])
    Speak("what next ?")


def open_link(url):
    # url = "www.google.com/"
    # brave_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application %s'
    brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s"
    wb.get(brave_path).open(url, 1)
    Speak("anything else senpai ?")


def wishme():

    hour = datetime.datetime.now().hour
    if 6 <= hour <= 12:
        Speak('Good morning')
    elif 12 <= hour <= 18:
        Speak('Good afternoon')
    elif 18 <= hour <= 24:
        Speak('Good evening')
    else:
        Speak('good night')

    Speak("How can i help you today")


# def openAi(que):

#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=que,
#         temperature=0.9,
#         max_tokens=150,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0.6,
#         stop=[" Human:", " AI:"]
#     )

#     # text = response['choices'][0]['text']
#     data = response['choices'][0]['text']
#     print("Ans : " + data)
#     Speak(data)
