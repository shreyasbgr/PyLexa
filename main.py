import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            talk('Hi there! I am Alexa!')

            print('Listening...')
            voice = listener.listen(source, phrase_time_limit=3)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    if 'play' in command:
        command = command.replace('alexa', '')
        song=command.replace('play','')
        print(song)
        pywhatkit.playonyt(song)
        talk('playing'+song)
        print('playing')

    elif 'wiki' in command:
        command = command.replace('alexa', '')
        search=command.replace('wiki','')
        info=wikipedia.summary(search,2)
        print(info)
        talk(info)



run_alexa()