import datetime
import smtplib
import webbrowser
import pyjokes
import pyttsx3
import speech_recognition as sr
import wikipedia

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

        except Exception as e:
            # print(e)
            # Say that again will be printed in case of improper voice
            print("Say that again please...")
            takeCommand()
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")

        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service{0}".format(e))

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


if __name__ == "__main__":
    wishMe()
    while True:
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
