import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(" Good Morning!")
    elif hour>=12 and hour<18:
        speak(" Good Afternoon!")   
    else: 
        speak(" Good Evening!")  
    speak('Hi , I am ULTRON your digital voice assistant, How may i help you?')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1 
        r.energy_threshold = 900
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
            speak('HI I am ULTRON , what can I do for you')  
        elif 'bye' in query or 'stop' in query:
            speak('Bye , have a good day')
            break      













