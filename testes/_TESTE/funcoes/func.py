import webbrowser
import random
from datetime import datetime
import requests
import urllib.request
import re
import os






def criar_rotina():
    try:
        nome_rotina = input("Nome função: ")
        nome_funcao= nome_rotina.replace(" ", "_")
        funcoes = input("Lista com funcoes: ").split(",")

    #    comandos_cadastrados = []
    #    for i in lista_comandos.values():
    #        comandos_cadastrados.append(i.__name__)
    #        print(func.__file__)

        with open("rotinas.py", "a") as arquivo:
            arquivo.write(f"\n\ndef {nome_funcao}():\n    return [\n")
            for i in funcoes:
    #            if i in comandos_cadastrados:
                    arquivo.write(f"            '{i}'," + "\n")
    #            else:
    #                print("comando nao cadastrado " + i)
            arquivo.write(f"]\n")

        with open("testes/_TESTE/comandos.py", "r") as f:
            contents = f.readlines()

        contents.insert(-2, f"                      '@ {nome_rotina}': '{nome_funcao}', \n")

        with open("comandos.py", "w") as f:
            contents = "".join(contents)
            f.write(contents)
        return f"Rotina {nome_rotina} adicionada com sucesso"
    except:
        return 'Não foi possivel criar a rotina'














def tocar_musica(*musica):
    try:
        print(musica)
        if musica[0] == '':
            proucura = "musica"
        else:
            proucura = musica[0].replace(" ", "+")

        html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+proucura)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        webbrowser.open("https://www.youtube.com/watch?v="+video_ids[0])
        return f"Tocando agora {musica} no youtube"
    except:
        return 'Não foi possivel tocar a música'


def temperatura(*argv):
    try:
        API_KEY = "1a32328f047315c5036afdf2c4fbf1a8"
        print(argv)
        if argv == () or argv[0] == "":
            cidade = "blumenau"
        else:
            cidade = argv[0].replace("na", "").replace("no", "")
        link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang={'pt_br'}"
        requisicao = requests.get(link)
        requisicao_dic = requisicao.json()
        try:
            descricao = requisicao_dic['weather'][0]['description']
            temperatura = requisicao_dic['main']['temp'] - 273.15
            return f'em {cidade} está fazendo {temperatura:.0f}ºC e esta {descricao}'
        except:
            return "Desculpe cidade não encontrada"
    except:
        return 'Não foi possivel ver a temperatura'


def pesquisar_google(comando):
    try:
        print(comando)
        webbrowser.open(f'http://www.google.com/search?client=firefox-b-lm&q={comando}')
        return f'Pesquisei {comando} no Google.'
    except:
        return 'Não foi possivel pesquisar'


def pesquisar_youtube(comando):
    try:
        print(comando)
        webbrowser.open(f'https://www.youtube.com/results?search_query={comando}')
        return f'Pesquisei {comando} no Youtube.'
    except:
        return 'Não foi possivel pesquisar'


def fale(text):
    return text



def apresentar():
    try:
        # TODO: Colar o texto que esta la nos testes
        return "Olá, meu nome é Minerva! Sou uma assistente virtual open source feita em Python. Você pode adicionar comandos facilmente acessando meu repositório no guitirub."
    except:
        return 'Não foi possível apresentar'

def piadas():
    try:
        piadas = ['Duas galinhas estão na cozinha fazendo café. Uma delas pergunta: Pó pô pó?A outra responde: Pó pô.','No primeiro dia de aula, uma aluna nova se apresenta à professora:- Meu nome é Jaqueline, tenho 13 anos e já namoro.- Já o quê?- Jaqueline.', 'O que o lápis disse para o papel? Você está me desapontando','Soy paraguaio e vim para matar-te. Para o quê? Paraguaio.','Duas galinhas estão na cozinha fazendo café. Uma delas pergunta: Pó pô pó?A outra responde: Pó pô.', 'Eu tinha um pintinho chamado Relam. Toda vez que chovia, Relam piava.',' O que o martelo foi fazer no culto de domingo?- Pregar.',' Qual foi o peixe que caiu do 15º andar? Aaaaaaaaaatum.', 'No restaurante, o garçom pergunta: O que deseja para beber? Caipirinha? Não, obrigado, não bebo destilado. Ah, sem problemas. Posso servir pelo outro lado.', 'O paciente chega no consultório e o médico diz: Bom dia, tudo bem? Tudo sim, Doutor. Ótimo, então já pode ir embora.','Um filho diz para a mãe: Mãe, tenho uma festa de 15 anos para ir. Mas não dá para ficar só um dia? 15 anos é muito tempo.', 'Por que a planta não responde? Porque ela é mudinha.','Um amigo agradece ao outro: Muito obrigado. Disponha. Ponha.',' O que a esposa do Albert Einstein disse quando o viu sem roupa? Uau, que físico.', 'Por que o jacaré tirou o filho da escola?...Porque ele réptil de ano!','Qual é a diferença entre a pizza e a sua opinião?A pizza eu pedi! ','Qual é o animal que não vale mais nada? O javali! ']
        #TODO: Revisar piadas, ver se todas estão separadas no lugar certo,
        #TODO: ver um jeito de fazer ela esperar um pouco antes de dar a resposta
        return random.choice(piadas)
    except:
        return 'Não foi possível contar piada'

def frases():
    try:
        lista_frases = ['É em meio a dificuldade que se encontra a oportunidade','O êxito é ir de frustração a frustração sem perder a animação','Mesmo que algo pareça difícil, nunca desista antes de tentar','Você é o único que entende as suas dificuldades, por isso motive se a prosseguir','Não é uma vida ruim, é apenas um dia ruim, lembre-se disso','A maior prova de que você pode fazer o impossível, é superar circunstâncias difíceis','Que os dias bons se tornem rotina, e os ruins se tornem raros','É genial celebrar a vitória, contudo é mais significativo aprender com as lições da derrota','Qualquer dificuldade pode ser ultrapassada, já que para todo problema há uma solução','Já pensou que você já superou muitas dificuldades até aqui?','Suas pequenas vitórias são todas as dificuldades superadas durante sua vida, tenha orgulho delas','Cada dificuldade ultrapassada te faz mais forte','Desistir não deve ser considerado, mesmo que as coisas não sejam fáceis']
        return random.choice(lista_frases)
    except:
        return 'Não foi possível contar frase'


def calculadora(text):
    try:
        for _ in range(len(text.split())):
            if "mais" in text:
                text = text.replace("mais", "+")
            if "vezes" in text:
                text = text.replace("vezes", "*")
            if "x" in text:
                text = text.replace("x", "*")
            if "dividido" in text:
                text = text.replace("dividido", "/")
            if "menos" in text:
                text = text.replace("menos", "-")
            if "elevado a" in text:
                text = text.replace("elevado a ", "**")
            if "por" in text:
                text = text.replace("por", "")
        return f"O resultado é {str(eval(text))}"
    except:
        return 'Não foi possivel calcular'


def diga_hora():
    try:
        hora = datetime.now().strftime('%H:%M')
        return hora
    except:
        return 'Não foi possível ver a hora'

def diga_data():
    try:
        data = datetime.now().strftime('%Y-%m-%d')
        return data
    except:
        return 'Não foi possível dizer a data'

def Desligar_pc():
    try:
        if (os.name == "nt"):
            os.system("shutdown /s /t 1")
        else:
            os.system("shutdown -h now")
    except:
        return 'Não foi possível desligar o pc'

def Abrir_arquivo(comando):
    try:
        try:
            a = r'{}.exe'.format(comando)
            os.startfile(a)
            return f"{comando} aberto"
        except:
            os.startfile(comando)
            return  "Arquivo aberto"
        else:
            return "Caminho não encontrado"
    except:
        return 'Não foi possível abrir o arquivo'

