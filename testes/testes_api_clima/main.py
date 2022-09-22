from azure.cognitiveservices.speech.audio import AudioOutputConfig
import azure.cognitiveservices.speech as speechsdk
import speech_recognition as sr

import func
import financeiro
import notas

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
    print(sr.Microphone.list_microphone_names())
    rec = sr.Recognizer()
    with sr.Microphone(device_index=18) as mic:
        rec.adjust_for_ambient_noise(mic)
        print("Estou te ouvindo...")
        audio = rec.listen(mic)
        try:
            print("Trancrevendo...")
            frase = rec.recognize_google(audio, language="pt-BR")
        except:
            print("Erro no recebimento de áudio")
            return "erro"
        return frase.lower()


def run_minerva(input_microfone=False, input_texto=""):
	
    if input_microfone == True:
        comando = receber_audio()
    else:
        comando = input_texto

#IMPORTANTE LEMBRAR DE COMANDOS COM MAIS ARGUMENTOS [*] MAIS EM CIMA
    lista_comandos = {
                      'pesquise * no youtube': func.pesquisar_youtube,
                      'pesquise vídeo de *': func.pesquisar_youtube,
                      'pesquise vídeo da *': func.pesquisar_youtube,
                      'pesquise vídeo do *': func.pesquisar_youtube,
                      'pesquise vídeos de *': func.pesquisar_youtube,
                      'pesquise vídeos da *': func.pesquisar_youtube,
                      'pesquise vídeos do *': func.pesquisar_youtube,


                      'pesquise *': func.pesquisar_google,

                      'apresentar': func.apresentar,
                      'se apresente': func.apresentar,
                      'se apresenta': func.apresentar,
                      
                      'piada': func.piadas,
                      'me faça rir': func.piadas,

                      'frase motivacional': func.frases,

                      'calcule *': func.calculadora,
                      'some *': func.calculadora,
                      'subtraia *': func.calculadora,
                      'divida *': func.calculadora,
                      'multiplique *': func.calculadora,

                      'dia é hoje': func.diga_data,
                      'data é hoje': func.diga_data,
                      'dia de hoje': func.diga_data,
                      'data de hoje': func.diga_data,

                      'horas são': func.diga_hora,
                      'horas é': func.diga_hora,
                      'hora são': func.diga_hora,
                      'hora é': func.diga_hora,

                      'adicionar gasto *': financeiro.adicionar,
                      'gastei *': financeiro.adicionar,
                      
                      'mostrar gastos': financeiro.listar_gastos_mes,
                      'listar gastos': financeiro.listar_gastos_mes,
                      'liste os gastos': financeiro.listar_gastos_mes,

                      'total de gastos do mês': financeiro.soma_total_mes,
                      'soma de gastos do mês': financeiro.soma_total_mes,

                      'anote *': notas.adicionar_nota,
                      'adicionar nota *': notas.adicionar_nota,

                      'mostre minhas notas': notas.mostrar_todas_notas,
                      'minhas notas': notas.mostrar_todas_notas,
                      'mostre as minhas notas': notas.mostrar_todas_notas,
                      'listar notas': notas.mostrar_todas_notas,
                      'ler notas': notas.mostrar_todas_notas,

                      'mostrar notas de hoje': notas.mostrar_nota_dia,
                      'mostrar as notas de hoje': notas.mostrar_nota_dia,
                      'mostre as notas de hoje': notas.mostrar_nota_dia,
                      'mostre notas de hoje': notas.mostrar_nota_dia,

                      'lembrete *': notas.adicionar_lembrete,
                      'me lembre de *': notas.adicionar_lembrete,
                      'lembre *': notas.adicionar_lembrete,
                      'me lembra de *': notas.adicionar_lembrete,
                      'me da um toque *': notas.adicionar_lembrete,


                      'qual a temperatura *': func.temperatura,
                      'qual a temperatura agora': func.temperatura,
                      'qual a previsão do tempo agora': func.temperatura,
                      'qual a previsão do tempo em *': func.temperatura,
                      'qual a previsão do tempo para *': func.temperatura,
                      'previsão do tempo': func.temperatura,

                      'teste microfone': teste_microfone
}

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
                fale(resposta)
                return resposta
                break
            
        else:
            if chave in comando:
                resposta = lista_comandos[chave]()
                fale(resposta)
                return resposta
                break

    else:    
        fale('Desculpe, comando não encontrado ' + comando)

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
        tela()






















