import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech.audio import AudioOutputConfig
from datetime import datetime
import speech_recognition as sr
import webbrowser

#TODO - Mudar para Mozilla caso não haja Chrome
#Abrir a primeira pesquisa no Youtube

def pesquisar_google(comando):
    print(comando)
    webbrowser.open(f'http://www.google.com/search?client=firefox-b-lm&q={comando}')
    talk(f'Pesquisei {comando} no Google.')

def pesquisar_youtube(comando):
    print(comando)
    webbrowser.open(f'https://www.youtube.com/results?search_query={comando}')
    talk(f'Pesquisei {comando} no Youtube.')

def exemplo(text):
    print(text)
    talk(text)


def talk(text):
    speech_config = speechsdk.SpeechConfig(subscription="x", region="brazilsouth")
    #In this sample we are using the default speaker  
    #Learn how to customize your speaker using SSML in Azure Cognitive Services Speech documentation
    
    speech_config.speech_synthesis_language = 'pt-br'
    audio_config = AudioOutputConfig(use_default_speaker=True)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    synthesizer.speak_text_async(text)

def recebendo_audio():
    rec = sr.Recognizer()
    with sr.Microphone(device_index=1) as mic:
        rec.adjust_for_ambient_noise(mic)
        print("Estou te ouvindo...")
        audio = rec.listen(mic)
        try:
            frase = rec.recognize_google(audio, language="pt-BR")
        except:
            print("Erro no recebimento de áudio")
        return frase.lower()


def run_minerva():
    comando = recebendo_audio()#.replace(" vírgula ", ", ")

    lista_comandos = {'fale':talk, 'fala':talk, 'que horas são':diga_hora, 'que dia é hoje':diga_data}

    for i in lista_comandos.keys():
        if i in comando:
            lista_comandos[i]((comando.replace(i+" ", "")))
    else:
        print(comando)


def diga_hora(comando):
    hora = datetime.now().strftime('%H:%M:%S')
    print(comando)
    talk(hora)


def diga_data(comando):
    data = datetime.now().strftime('%Y-%m-%d')
    print(comando)
    talk(data)

while True:
   try:
        run_minerva()
   except Exception as e:
        print(f"ERRO, {e}")



#PRECISA INSTALAR PYAUDIO    

#------------------------------------------------------------
#PARA RECONHECER MICROFONES, USAR: 
#TO RECOGNIZE MICROPHONES, USE:

# print( sr.Microphone.list_microphone_names())
#-------------------------------------------------------------

#FUNÇÃO MISTERIOSA E TALVEZ INÚTIL DA MICROSOFT:
# synthesize_to_speaker()
