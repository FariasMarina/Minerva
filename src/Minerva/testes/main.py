import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech.audio import AudioOutputConfig
import speech_recognition as sr
import webbrowser

from src.Minerva.testes.func_deltatime.func_deltatime import *
import src.Minerva.testes.teste_funcao_financeiro.financeiro as financeiro

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
    
def se_apresente(comando):
    print(comando)
    talk(f'Olá, meu nome é Minerva! Sou uma assistente virtual open source feita em Python. Meus hobbie é contar piada, falar e dar rolê com a Ziri. Você pode adicionar comandos facilmente acessando meu repositório no Github.')

def exemplo(text):
    print(text)
    talk(text)


def talk(text):
    # speech_config = speechsdk.SpeechConfig(subscription="9bc9a7005e8f4ab9b42c4ecc13d5680a", region="brazilsouth")
    # #In this sample we are using the default speaker
    # #Learn how to customize your speaker using SSML in Azure Cognitive Services Speech documentation
    #
    # speech_config.speech_synthesis_language = 'pt-br'
    # audio_config = AudioOutputConfig(use_default_speaker=True)
    # synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    # synthesizer.speak_text_async(text)
    print(text)


def receber_variaveis(text):
    talk(text)
    valor = recebendo_audio()
    return valor

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

    # comando = input("Digite seu comando: ")

    lista_comandos = {'fale':talk, 'fala':talk, 'que horas são':diga_hora, 'que dia é hoje':diga_data, 'mostre as contas totais do mês': financeiro.soma_total_mes, 'adicionar conta':financeiro.adicionar(), 'se apresente':seapresente()}

    for i in lista_comandos.keys():
        if i in comando:
            a = lista_comandos[i]((comando.replace(i+" ", "")))
            talk(a)
    else:
        talk(comando)

print(recebendo_audio())



# try:
#     run_minerva()
# except Exception as e:
#     print(f"ERRO, {e}")



#PRECISA INSTALAR PYAUDIO    

#------------------------------------------------------------
#PARA RECONHECER MICROFONES, USAR: 
#TO RECOGNIZE MICROPHONES, USE:

# print( sr.Microphone.list_microphone_names())
#-------------------------------------------------------------

#FUNÇÃO MISTERIOSA E TALVEZ INÚTIL DA MICROSOFT:
# synthesize_to_speaker()
