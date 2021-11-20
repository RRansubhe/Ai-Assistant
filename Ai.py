import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import  smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good morning Raman")
    elif hour >=12 and hour < 18:
        speak("Good afternoon Raman")
    else:
        speak("Good evening Raman")
    speak("I am your personal assistant. please tell me how may I help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("say that again please....")
        speak("say that again please....")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourmailaddress', 'password')
    server.sendmail("email id", to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentence=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'facebook' in query:
            speak ("opening facebook")
            webbrowser.open("facebook.com")

        if 'send mail to find' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "frnds mail address "
                sendEmail(to, content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry Raman. I am not able to send this mail")












