import webbrowser

# from main import receber_variaveis


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

def exemplo(text):
    return text

def apresentar(text):
    return "Olá me chamo Minerva, sou sua assitente virtual open source e estou a sua disposição"


