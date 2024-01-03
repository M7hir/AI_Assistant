import pywhatkit
import wikipedia
from pywikihow import search_wikihow
from Features import Speak
import webbrowser as web
import Main


def googleSearch(term):
    que = term.replace("core", "")
    que = que.replace("what is", "")
    que = que.replace("how to", "")
    que = que.replace("what do you mean", "")
    que = que.replace("what is the meaning", "")
    que = que.replace(" ", "")

    santance = str(que)
    file = open("C:/Users/key/Desktop/Ai_Project/data.txt", 'a')
    file.write(santance)
    file.close()

    Que = str(term)
    pywhatkit.search(Que)

    if "how to" in Que:
        max_result = 1
        how_to_func = search_wikihow(query=Que, max_results=max_result)
        assert len(how_to_func) == 1
        how_to_func[0].print()
        Speak(how_to_func[0].summary)
    else:
        search = wikipedia.summary(Que, 2)
        Speak(f"According to google : {search}")


def youtubeSearch(term):
    url = "https://www.youtube.com/results?search_query=" + term
    web.open(url)
    Speak("This is what i found")
    query = Main.TakeCommand()
    if "play the video" in query:
        pywhatkit.playonyt(term)