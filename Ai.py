import datetime
import os
import smtplib
import webbrowser
import pyjokes
import pyttsx3
import speech_recognition as sr
import wikipedia
import subprocess
import ctypes
import winshell
import wolframalpha
import win32com.client as wincl
import time
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning")
    elif 12 <= hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am your personal assistant. please tell me how may I help you")


# noinspection PyBroadException

def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            # Using google for voice recognition.
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")  # User query will be printed.

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service{0}".format(e))
        except Exception:
            # print(e)
            # Say that again will be printed in case of improper voice
            print("Say that again please...")
            takeCommand()

        if query:
            return query.lower()
        else:
            takeCommand()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourmailaddress', 'password')
    server.sendmail("email id", to, content)
    server.close()


def uropen():
    pass


if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        query = takeCommand()

        if 'wikipedia' in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentence=2)
            speak("according to wikipedia")
            speak(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("https://www.google.com")

        elif 'open smartschoolz' in query:
            speak("opening smartschoolz")
            webbrowser.open("https://smartschoolz.com/login")

        elif 'open codetantra' in query:
            speak("opening codetantra")
            webbrowser.open("https://cornerstonepublicschool.codetantra.com/login.jsp")

        elif 'open github' in query:
            speak("opening ")
            webbrowser.open("https://github.com/")

        elif 'tell me a joke' in query:
            speak(pyjokes.get_joke())

            # basic questions

        elif 'how are you' in query:
            speak("I am fine. Thank you")
            print("I am fine. Thank you")
            speak("How are you")

        elif "good" in query:
            speak("Its good to know that you are fine")

        elif "Who are you" in query:
            speak("I am your assistant. I can do many things like, open google.")

        elif "Who made you" in query:
            speak("My sir Raman Ransubhe made me")

            # subprocesses

        elif "lock windows" in query:
            speak("locking Windows...")
            ctypes.windll.user32.lockWorkStation()

        elif "shutdown windows" in query:
            speak("shutting down Windows...")
            subprocess.call('shutdown / p /f')

        elif "hibernate windows" in query:
            speak("hibernating Windows...")
            subprocess.call('shutdown / h')

        elif "restart" in query:
            speak("restarting Windows...")
            subprocess.call(["shutdown", "/r"])

        elif "write a note" in query:
            speak("what should I write")
            note = takeCommand()
            file = open('data.txt', 'w')
            speak("sir, should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strtime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strtime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show me my notes" in query:
            speak("showing your notes")
            file = open("data.txt", "r")
            print(file.read())
            speak(file.read(6))





        elif 'news' in query:
            # noinspection PyBroadException
            try:
                uropen()
                data = jason.load(jsonObj)
                i = 1

                speak("here are your top news form times of India")
                print('''==============TIMES OF INDIA''' + '\n')
                for item in datetime.date['articles']:
                    print(str(i) + '.' + item['tittle'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '.' + item['tittle'] + '\n')

            except Exception:
                print(str(e))

        elif 'find' in query:
            app_id = "APP ID"
            clint = wolframalpha.Client(app_id)
            indx = query.lower().split().index('find')
            query = query.split()[indx + 1:1]
            res = clint.query(' '.join(query))
            answer = next(res.results).txt
            print("the answer is" + answer)
            speak("the answer is" + answer)

        elif 'calculate' in query:
            app_id = "APP ID"
            clint = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:1]
            res = clint.query(' '.join(query))
            answer = next(res.results).txt
            print("the answer is" + answer)
            speak("the answer is" + answer)
