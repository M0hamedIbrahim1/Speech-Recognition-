import speech_recognition as sr
from gtts import gTTS
from time import ctime
import subprocess
import webbrowser
import playsound
import random
import os



r = sr.Recognizer()
m = sr.Microphone()

def record_audio(ask = False):
        if ask:
            speak(ask)
            print(ask)
        print("A moment of silence, please")
        with m as source: r.adjust_for_ambient_noise(source)
        flag = True
        while flag:
            speak("Say something!")
            print("Say something!")
            with m as source: audio = r.listen(source)
            speak("wait yaa Mohamed")
            try:
                value = r.recognize_google(audio)
                flag = False
            except sr.UnknownValueError:
                print("Didn't catch that")
        return value
    
def speak(audio_string):
    aud = gTTS(text=audio_string, lang='en')
    amp = 'audio'+str(random.randint(1, 999999))+'.mp3'
    aud.save(amp)
    playsound.playsound(amp)
    os.remove(amp) 

def respond(value):
    if 'what is your name' in value:
        speak('My name is Mohamed')
        print('My name is Mohamed')
        
    if 'how are you' in value:
        speak('I am fine , Thanks Mohamed')
        print('I am fine , Thanks Mohamed')
        
    if 'search' in value:
        print('What do you want to search')
        search = record_audio('What do you want to search')
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        
    if 'open brackets' in value:
        subprocess.Popen(['C:\Program Files (x86)\Brackets\Brackets.exe'])
        
    if 'open anydesk' in value:
        subprocess.Popen(['C:\Program Files (x86)\AnyDesk\AnyDesk.exe'])
        
    if 'find location' in value:
        print('What is the location?')
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location
        webbrowser.get().open(url)
                
    if 'I am bored' in value:
        speak('Watch a movie or Play a video game')
        print('Watch a movie or Play a video game')  
        
    if 'what time is it' in value:
        speak(ctime())
        print(ctime())
    if 'exit' in value:
        exit()

speak('How can I help you')
while True:
    value = record_audio()  
    respond(value) 
    
    
