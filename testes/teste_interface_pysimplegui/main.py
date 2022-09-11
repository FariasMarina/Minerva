from azure.cognitiveservices.speech.audio import AudioOutputConfig
from PySimpleGUI import PySimpleGUI as sg

import azure.cognitiveservices.speech as speechsdk
import speech_recognition as sr

from datetime import datetime
#import emoji

from func import *
# import financeiro

def talk(text):
    speech_config = speechsdk.SpeechConfig(subscription="9bc9a7005e8f4ab9b42c4ecc13d5680a",
										   region="brazilsouth")

    #In this sample we are using the default speaker
    #Learn how to customize your speaker using SSML in Azure Cognitive Services Speech documentation
	
    speech_config.speech_synthesis_language = 'pt-br'
    audio_config = AudioOutputConfig(use_default_speaker=True)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, 
											  audio_config=audio_config)

    synthesizer.speak_text_async(text)

        
    #synthesize_to_speaker()

def receber_variaveis(text):
    talk(text)
    valor = recebendo_audio()
    return valor


def recebendo_audio():
    a = datetime.now() 
    rec = sr.Recognizer()
    c = datetime.now() 
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        print("Estou te ouvindo...")
        audio = rec.listen(mic)
        try:
            frase = rec.recognize_google(audio, language="pt-BR")
        except:
            print("Erro no recebimento de áudio")
        b = datetime.now()
        print(a, c ,b)
        return frase.lower()


def run_minerva(microfone=False, receber=""):
	
	if microfone == True:
		comando = recebendo_audio()
	else:
		comando = receber
	lista_comandos = {'fale': fale,
					  'pesquise': pesquisar_google,
					  'apresenta': apresentar,
					  'piada': piadas,
					  # 'adicionar conta': financeiro.adicionar,
                      #TODO: testar comandos com o reconhecimento de voz
					  #TODO: editar contas
					  # 'deletar conta': financeiro.deletar,
                      # 'total de gastos': financeiro.soma_total_mes,
                      'some': calculadora,
                      'divida': calculadora,
                      'multiplique': calculadora,
                      'calcule': calculadora,
}

	for i in lista_comandos.keys():
		if i in comando:
			resposta = lista_comandos[i]((comando.replace(i+" ", "")))
			talk(resposta)
			return resposta
			break
	else:
		talk('Desculpe, comando não encontrado')

font = ("Arial", 50)

sg.theme('DarkPurple')
layout = [
    [sg.Button("🎙️" ,font=font, key="microfone", size = (12, 1))],
    [sg.Input(key='comando', font=20)],
    [sg.Button(font=60, key="enter", bind_return_key=True, visible=False)],
	[sg.Text("", key="-OUTPUT-")]
]


janela = sg.Window('Minerva', layout, element_justification='c')

while True:
    eventos, valores = janela.read()

    if eventos == sg.WINDOW_CLOSED:
        break
    print(eventos)
    print(valores)
	
    if eventos == 'microfone':
        run_minerva(microfone=True)
    elif eventos == 'enter':
        janela["-OUTPUT-"].Update("")
        janela["comando"].Update("")
        janela["-OUTPUT-"].Update(run_minerva(receber=valores['comando']))



























