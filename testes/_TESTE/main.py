from azure.cognitiveservices.speech.audio import AudioOutputConfig
import azure.cognitiveservices.speech as speechsdk
import speech_recognition as sr

import importlib
import unidecode

from testes._TESTE import rotinas
import comandos

lista_comandos = comandos.lista_comandos

def receber_lista_comandos_atualizada():
    importlib.reload(comandos)
    importlib.reload(rotinas)
    global lista_comandos
    lista_comandos = comandos.lista_comandos
    return comandos.lista_comandos.keys()

def executar_rotina(nome_rotina):
    print("inicio rotina")
    comandos = eval(f"rotinas.{nome_rotina}()")
    print(comandos)
    for i in comandos:
        run_minerva(input_microfone = False, input_texto = f"{i}")
    return "rotina finalizada"






def fale(text):
    print(text)
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
    fale(text)
    valor = input(text)
    return valor


def receber_audio():
    # print(sr.Microphone.list_microphone_names())
    rec = sr.Recognizer()
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        print("Estou te ouvindo...")
        audio = rec.listen(mic)
        try:
            print("Trancrevendo...")
            frase = rec.recognize_google(audio, language="pt-BR")
            frase = unidecode.unidecode(frase)
            print(frase)
            return frase.lower()
        except:
            print("Erro no recebimento de áudio")
            return "erro"


def run_minerva(input_microfone=False, input_texto=""):
    if input_microfone == True:
        comando = receber_audio()
    else:
        comando = input_texto

#IMPORTANTE LEMBRAR DE COMANDOS COM MAIS ARGUMENTOS [*] MAIS EM CIMA
    print(lista_comandos.keys())
    for chave in lista_comandos.keys():
        if "*" in chave: #verifico se o comando precisa de argumentos
   
            argumentos_chave = chave.split() 
            #Separo as palavras da chave da lista de comandos
            
            argumentos_comando = comando.split() #Separo as palavras do comando
            if argumentos_comando[0] == "minerva":
                argumentos_comando = argumentos_comando.pop(0) #Retiro a palavra Minerva
            contem_palavras_necessarias = 0
            palavras_necessarias = len(argumentos_chave) - argumentos_chave.count("*")

            for palavra in range(len(argumentos_chave)): #pra cada palavra na chave
                if argumentos_chave[palavra] != "*": #se for diferente de *
                   if argumentos_chave[palavra] in comando: #vejo se a palavra esta no comando inicial
                       contem_palavras_necessarias += 1 #se sim ela tem +1 palavra necessaria pra rodar esse comandos
                       try:
                           argumentos_comando.remove(argumentos_chave[palavra]) #Retiro essa palavra do comando, para sobrar so oque não tem a ver com chamar a função
                       except:
                           break
            if palavras_necessarias == contem_palavras_necessarias: #se ela atingir o total de palavras necessarias
                resposta = lista_comandos[chave](' '.join(argumentos_comando))
                try:
                    fale(resposta)
                    return resposta
                except:
                    pass
                break

        elif "@" in chave:
            if chave.replace("@ ", "") in comando:
                return executar_rotina(lista_comandos[chave])
                break

        else:

            if chave in comando:
                resposta = lista_comandos[chave]()
                fale(resposta)
                return resposta
                break

    else:
        fale('Desculpe, comando não encontrado ' + comando)
        return 'Desculpe, comando não encontrado '

def teste_microfone():
    while True:
        a = receber_audio()
        print(a)

def tela():
    tipo_input = input("[1]Microfone [2]Comando: ")
    if tipo_input == "1":
        run_minerva(input_microfone=True)
    elif tipo_input == "2":
        run_minerva(input_texto=input("Digite seu comando:"))
    else:
        fale("opção invalida")



if __name__ == "__main__":
    while True:
        # teste_microfone()
        importlib.reload(rotinas)
        importlib.reload(comandos)
        lista_comandos = comandos.lista_comandos
        tela()























