import speech_recognition as sr
from os import system as komut



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

 
r = sr.Recognizer()
with sr.Microphone() as source:
    komut("cls")
    print("Merhaba Yasin Nasıl Yardımcı olabilirim  ? ")
    audio = r.listen(source)

    flag = False
 
try:
    text = r.recognize_google(audio, language = "tr")
    print("Algılanan: " + text )
    flag = True
    text = lower(text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

    if flag:
        if text == "program çalıştır":
            komut("atom.exe")
