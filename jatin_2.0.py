import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice' , voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am jatin two point o please tell we How can I help you")

def takeCommand():
    '''
    it takes microphone input and return string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language = 'en-in')
        print(f"User Said : {query}\n")
    except:
        # print(e)
        print("Say that again please")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    a = True
    while a:
        query = takeCommand().lower()
       
        if "wikipedia" in query:
            speak("Seraching wikipedia")
            query = query.replace("wikipedia" , "")
            results = wikipedia.summary(query , sentences = 2)  # speak two lines of wikipedia page
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "quit" in query:
            query = query.replace("query" , "")     # it will quit the jatin 2.0
            speak("Ok sir")
            a = False
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "play music" in query:
            music_dir = r"C:\FAST"     # my music directory you can use your music directory/folder
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir , songs[0]))
        elif "current time" in query:
            strtime = datetime.datetime.now().strftime('%H:%M:%S') #this function convert time to string
            speak(f"sir the time is {strtime}")


        

