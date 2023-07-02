import os
import sys
import webbrowser

import speech_recognition as sr

# ------------------
import pyttsx3
engine = pyttsx3.init()
# engine.say("Текст")
# engine.runAndWait()
# -------------------


def talk(words):
    print(words)
    # os.system("say " + words)
    engine.say(words)
    engine.runAndWait()


# talk("Привіт, чим можу допомогти?")
talk("Hello")


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        # task = r.recognize_google(audio, language="en-US").lower() # ru-RU
        # task = r.recognize_google(audio, language="ru-RU").lower()  # ru-RU
        task = r.recognize_google(audio, language="uk-UA").lower()  # ru-RU
        print("You: " + task)
    except sr.UnknownValueError:
        talk("Don`t understand")
        task = command()

    return task


def make_something(ar_task):
    if ("відкрити" and "сайт") in ar_task:
        talk("ok")
        url = "https://ituniver.com"
        webbrowser.open(url)

    elif "стоп" in ar_task:
        talk("Good bye")
        sys.exit()

    elif "ім'я" in ar_task:
        talk("My name is JARVIS")


while True:
    make_something(command())
