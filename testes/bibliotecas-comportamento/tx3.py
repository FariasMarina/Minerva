import pyttsx3

engine = pyttsx3.init()

#PARA A VELOCIDADE DE REPRODUÇÃO
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 260)

#PARA FALAR
engine.say("Oi, bom dia! Tudo bem?")
engine.runAndWait()

#PARA O VOLUME
volume = engine.getProperty('volume')
print(volume)
engine.setProperty('volume', 400)


engine.save_to_file('Era uma vez um pintinho que se chama Relam. Toda vez que chovia, Relam piava!', 'test.mp3')
engine.runAndWait()




# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
# engine.say("Olá, tudo bem? Bom dia!")
# engine.runAndWait()
# engine.setProperty('voice', voices[1].id)
# engine.say("Bom dia, Josias!")
# engine.runAndWait()
#
#
# engine.say("Hello World!")
# engine.say('My current speaking rate is ' + str(rate))
# engine.runAndWait()
# engine.stop()
