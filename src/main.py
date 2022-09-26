from azure.cognitiveservices.speech.audio import AudioOutputConfig


import azure.cognitiveservices.speech as speechsdk
import speech_recognition as sr

import comandos.Notas as Notas
from comandos.func import *
import comandos.financeiro as financeiro

#!/usr/bin/env python

def talk(text):

    speech_config = speechsdk.SpeechConfig(subscription="X",
										   region="brazilsouth")

    #In this sample we are using the default speaker
    #Learn how to customize your speaker using SSML in Azure Cognitive Services Speech documentation
	
    speech_config.speech_synthesis_language = 'pt-br'
    audio_config = AudioOutputConfig(use_default_speaker=True)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, 
											  audio_config=audio_config)
    synthesizer.speak_text_async(text)

    #synthesize_to_speaker()

def receber_variaveis(pergunta):
    talk(pergunta)
    valor = recebendo_audio()
    return valor

def recebendo_audio():
    #rec = sr.Recognizer()
    #with sr.Microphone(device_index=18) as mic:
    #    rec.adjust_for_ambient_noise(mic)
    #    print("Estou te ouvindo...")
    #    audio = rec.listen(mic)
    #    try:
    #        frase = rec.recognize_google(audio, language="pt-BR")
    #    except:
    #        print("Erro no recebimento de áudio")
    #    return frase.lower()
	return input("Digite seu comando: ")

def run_minerva():
    comando = recebendo_audio()

    lista_comandos = {'fale': fale,
					  'pesquise': pesquisar_google,
					  'apresenta': apresentar,
					  'piada': piadas,
					  'adicionar conta': financeiro.adicionar, 
                      #TODO: testar comandos com o reconhecimento de voz
					  #TODO: editar contas
					  'deletar conta': financeiro.deletar,
                      'total de gastos': financeiro.soma_total_mes,
                      'some': calculadora,
                      'divida': calculadora,
                      'multiplique': calculadora,
                      'calcule': calculadora,
                      'anote':Notas.adicionar_nota,
                      'frases motivacionas': frases,

}

    for i in lista_comandos.keys():
        if i in comando:
            resposta = lista_comandos[i]((comando.replace(i+" ", "")))
            talk(resposta)
            break


while True:
    run_minerva()







