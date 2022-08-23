import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech.audio import AudioOutputConfig
from datetime import datetime
import speech_recognition as sr
 



def exemplo(text):
    print(text)
    talk(text)


def talk(text):
    speech_config = speechsdk.SpeechConfig(subscription="", region="brazilsouth")
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
        print("Fale algo")
        audio = rec.listen(mic)
        try:
            frase = rec.recognize_google(audio, language="pt-BR")
        except:
            print("Erro no recebimento de áudio")
        return frase.lower()



def run_minerva():
    comando = recebendo_audio()#.replace(" vírgula ", ", ")

    lista_comandos = {'fale':talk, 'fala':talk, 'que horas são':diga_hora}

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
    except:
        print("ERRO")
    

#------------------------------------------------------------
#PARA RECONHECER MICROFONES, USAR: 
#TO RECOGNIZE MICROPHONES, USE:

# print( sr.Microphone.list_microphone_names())
#-------------------------------------------------------------

#FUNÇÃO MISTERIOSA E TALVEZ INÚTIL DA MICROSOFT:
# synthesize_to_speaker()
