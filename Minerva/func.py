import webbrowser
import random



# - Mudar para Mozilla caso não haja Chrome
#Abrir a primeira pesquisa no Youtube

def pesquisar_google(comando):
    print(comando)
    webbrowser.open(f'http://www.google.com/search?client=firefox-b-lm&q={comando}')
    return f'Pesquisei {comando} no Google.'

def pesquisar_youtube(comando):
    print(comando)
    webbrowser.open(f'https://www.youtube.com/results?search_query={comando}')
    return f'Pesquisei {comando} no Youtube.'

def fale(text):
    return text

def apresentar(text):
	# TODO: Colar o texto que esta la nos testes
    return "Olá me chamo Minerva, sou sua assitente virtual open source e estou a sua disposição"
	

def piadas(text):
	piadas = ['Duas galinhas estão na cozinha fazendo café. Uma delas pergunta: Pó pô pó?A outra responde: Pó pô.','No primeiro dia de aula, uma aluna nova se apresenta à professora:- Meu nome é Jaqueline, tenho 13 anos e já namoro.- Já o quê?- Jaqueline.', 'O que o lápis disse para o papel? Você está me desapontando','Soy paraguaio e vim para matar-te. Para o quê? Paraguaio.','Duas galinhas estão na cozinha fazendo café. Uma delas pergunta: Pó pô pó?A outra responde: Pó pô.', 'Eu tinha um pintinho chamado Relam. Toda vez que chovia, Relam piava.',' O que o martelo foi fazer no culto de domingo?- Pregar.',' Qual foi o peixe que caiu do 15º andar? Aaaaaaaaaatum.', 'No restaurante, o garçom pergunta: O que deseja para beber? Caipirinha? Não, obrigado, não bebo destilado. Ah, sem problemas. Posso servir pelo outro lado.', 'O paciente chega no consultório e o médico diz: Bom dia, tudo bem? Tudo sim, Doutor. Ótimo, então já pode ir embora.','Um filho diz para a mãe: Mãe, tenho uma festa de 15 anos para ir. Mas não dá para ficar só um dia? 15 anos é muito tempo.', 'Por que a planta não responde? Porque ela é mudinha.','Um amigo agradece ao outro: Muito obrigado. Disponha. Ponha.',' O que a esposa do Albert Einstein disse quando o viu sem roupa? Uau, que físico.', 'Por que o jacaré tirou o filho da escola?...Porque ele réptil de ano!','Qual é a diferença entre a pizza e a sua opinião?A pizza eu pedi! ','Qual é o animal que não vale mais nada? O javali! ']
	#TODO: Revisar piadas, ver se todas estão separadas no lugar certo,
	#TODO: ver um jeito de fazer ela esperar um pouco antes de dar a resposta 
	return random.choice(piadas)

def frases(text):
    lista_frases = ['É em meio a dificuldade que se encontra a oportunidade','O êxito é ir de frustração a frustração sem perder a animação','Mesmo que algo pareça difícil, nunca desista antes de tentar','Você é o único que entende as suas dificuldades, por isso motive se a prosseguir','Não é uma vida ruim, é apenas um dia ruim, lembre-se disso','A maior prova de que você pode fazer o impossível, é superar circunstâncias difíceis','Que os dias bons se tornem rotina, e os ruins se tornem raros','É genial celebrar a vitória, contudo é mais significativo aprender com as lições da derrota','Qualquer dificuldade pode ser ultrapassada, já que para todo problema há uma solução','Já pensou que você já superou muitas dificuldades até aqui?','Suas pequenas vitórias são todas as dificuldades superadas durante sua vida, tenha orgulho delas','Cada dificuldade ultrapassada te faz mais forte','Desistir não deve ser considerado, mesmo que as coisas não sejam fáceis']
    return random.choice(lista_frases)


def calculadora(text):
    print(len(text.split()))
    for _ in range(len(text.split())):
        print("A")
        if "mais" in text:
            a = text.replace("mais", "+")
        if "vezes" in text:
            a = text.replace("vezes", "*")
        if "dividido" in text:
            a = text.replace("dividido", "/")
        if "menos" in text:
            a = text.replace("menos", "-")
    print(eval(a))
    return eval(a)
