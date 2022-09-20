import sqlite3
import datetime

banco = sqlite3.connect('BancoNotas.db')
cursor = banco.cursor()


def criar_banco():
    cursor.execute('CREATE TABLE IF NOT EXISTS "Notas"('
                   '"ID" integer primary key AUTOINCREMENT,'
                   '"data" text not null,'
                   '"nome" text not null,'
                   '"notas" text not null)')
    banco.commit()



def adicionar_nota(anotacao):
    print(anotacao)

    nome = "_"
    nota = anotacao
    data = datetime.datetime.now()
    dataauto = str(data.date())
    cursor.execute(f"INSERT INTO Notas(data, nome, notas) VALUES(?,?,?)", (dataauto, nome, nota))
    banco.commit()
    return f'nota {nota} salva'


def mostrar_nota_dia():
    data = datetime.datetime.now()
    dataauto = str(data.date())
    cursor.execute(f"SELECT notas FROM Notas WHERE data='{dataauto}'")
    res = cursor.fetchall()
    resposta = []
    for i in res:
        tex = str(i)
        texto = tex.replace('(', '').replace(')', '').replace(',', '')
        resposta.append(texto)
    return f"Voce tem as seguintes notas anotadas, {' e '.join(resposta)}"


def mostrar_nota_nome(nome):
    from main import receber_variaveis
    nome = receber_variaveis('Qual o nome da nota?')
    cursor.execute(f"SELECT notas FROM Notas WHERE nome='{nome}'")
    res = cursor.fetchall()
    for i in res:
        tex = str(i)
        texto = tex.replace('(', '').replace(')', '').replace(',', '')
        print(texto)


def mostrar_todas_notas():
        cursor.execute(f"SELECT notas FROM Notas")
        res = cursor.fetchall()
        resposta = []
        for i in res:
            tex = str(i)
            texto = tex.replace('(', '').replace(')', '').replace(',', '')
            resposta.append(texto)
        return f"Voce tem as seguintes notas anotadas, {' e '.join(resposta)}"


def adicionar_lembrete(texto):

    texto = texto.split()
    # as 16 h para tirar o frangi
    # de tirar o frango as 16

    for i in range(len(texto)):
        if texto[i] == "ás":
            hora = te

    nome = receber_variaveis('Qual nome deseja dar ao lembrete?')
    data = receber_variaveis('Pra que data?')
    lembrete = receber_variaveis('Pode falar o lembrete, estou te ouvindo')
    cursor.execute('INSERT INTO Notas(data, nome, notas) VALUES(?,?,?)', (data, nome, lembrete))
    banco.commit()
    return print('feito')


def ler_Lembrete():
    data = datetime.datetime.now()
    dataauto = str(data.date())
    cursor.execute(f'SELECT notas FROM Notas WHERE data="{dataauto}"')
    res = cursor.fetchall()
    for i in res:
        tex = str(i)
        texto = tex.replace('(', '').replace(')', '').replace(',', '')
        print(texto)



# criar_banco()
# adicionar_nota('dog', 'levar dog para passear')
# mostrar_nota_dia('2022-09-12')
# mostrar_nota_nome('dog')
# mostrar_todas_notas()
# adicionar_lembrete('2022-09-13', 'remédio', 'tomar remédio')
# ler_Lembrete() #lê somente os do dia



