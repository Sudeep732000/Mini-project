import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    speak("Loading Galaxy version 3.0")
    if hour>=0 and hour<12:
        speak(" Hello Good Morning!")
    elif hour>=12 and hour<15:
        speak(" Hello Good Afternoon!")  
    elif hour>=15 and hour<19:
        speak(" Hello Good Evening!")     
    else: 
        speak(" Hello Good Night!")  
    speak('Hi , I am Galaxy Version 1your digital voice assistant, How may i help you?')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Tell me what can i do now..")                                                                       
        print("Listening...")
        r.pause_threshold =  1 
        r.energy_threshold = 1000
        audio = r.listen(source)
    try:
        print('Recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        print('Say that again please....,I cant Recognize you.. ')
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia......')
            query = query.replace('wkipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('www.youtube.com') 

        elif 'open google' in query:
            webbrowser.open('www.google.com')  

        elif 'open hackerrank' in query:
            webbrowser.open('www.hackerrank.com')     

        elif 'open linkedin' in query:
            webbrowser.open('www.linkedin.com') 

        elif 'who is your master' in  query or 'who is your boss' in query:
            speak("I was created by Sudeep Balagopal")
            print("I was created by Sudeep Balagopal")    

        elif 'open whatsapp' in query:
            webbrowser.open('https://web.whatsapp.com/')    

        elif 'play music'in query:
            music_folder = "D:\\songs\\"
            music = ['TheSpectre','Rockabye', 'AllFallsDown']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
            speak('Okay, here is your music! Enjoy!')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir, The time is {strTime}')

        elif 'how are you' in query:
            msg  = ['I am fine', 'Awesome', 'just doing my job','Nice!']
            speak(random.choice(msg))
        elif 'hello' in query:
            speak('HI! I am Galaxy , what can I do for you')  
        elif 'bye' in query or 'stop' in query:
            speak('Bye , have a good day')
            break      













