import pyttsx3

engine = pyttsx3.init()

while True:
    falar = input('>')
    if falar != 'sair':
        engine.say(falar)
        engine.runAndWait()
    else:
        break