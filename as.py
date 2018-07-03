import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import webbrowser
 

buyukAlfabe = "ABCÇDEFGĞHİIJKLMNOÖPRSŞTUÜVYZ"
kucukAlfabe = "abcçdefgğhiıjklmnoöprsştuüvyz"

def lower(text:str):
    newText = str()
    for i in text:
        if i in buyukAlfabe:
            index = buyukAlfabe.index(i)
            newText += kucukAlfabe[index]

        else:
            newText += i


    return newText


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='tr')
    tts.save("audio.mp3")
    os.system("audio.mp3")
 
def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Soru Sorun")
        audio = r.listen(source)
    data = ""

    try:
        data = r.recognize_google(audio , language = "tr")
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
 
def jarvis(data):
    if "nasılsın" in data:
        speak("Ben iyim sen nasılsın")
 
    if "saat kaç" in data:
        speak(ctime())

    if "teşekkürler" in data:
        speak("Ben Teşekkür Ederim")
 
    if "neredeyim" in data:
        data = data.split(" ")
        location = data[2]
        speak("Bekle Yasin, sana nerde oldoğunu  " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")


    if "Tarayıcıyı aç" in data:
        speak("Lütfen Bekleyin tarayıcıyı Açıyorum")
        webbrowser.open("www.google.com")
 
 

time.sleep(2)
speak("Merhaba Yasin, Ben Tuğba senin için ne yapabilirim ?")
while 1:
    data = recordAudio()
    jarvis(data)