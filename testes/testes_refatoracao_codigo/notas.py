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
    return print('Banco criado')


def adicionar_nota(comando):
    print(comando)
    #TODO: Ajeitar isso aqui
    from main import receber_variaveis
    nome = "_"
    nota = receber_variaveis('Qual a anotação?')
    data = datetime.datetime.now()
    dataauto = str(data.date())
    cursor.execute(f"INSERT INTO Notas(data, nome, notas) VALUES(?,?,?)", (dataauto, nome, nota))
    banco.commit()
    return print('feito')


def mostrar_nota_dia(dia):
    from main import receber_variaveis
    dia = receber_variaveis('Você quer receber as anotações de que dia?')
    cursor.execute(f"SELECT notas FROM Notas WHERE data='{dia}'")
    res = cursor.fetchall()
    for i in res:
        tex = str(i)
        texto = tex.replace('(','').replace(')','').replace(',','')
        print(texto)


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
    from main import receber_variaveis
    comando = receber_variaveis("Deseja ouvir todas as suas notas? Sim ou Não?")
    if comando == 'sim':
        cursor.execute(f"SELECT notas FROM Notas")
        res = cursor.fetchall()
        for i in res:
            tex = str(i)
            texto = tex.replace('(', '').replace(')', '').replace(',', '')
            print(texto)
    elif comando == 'nao':
        print('Ok, deixa pra depois')

def adicionar_lembrete(data, nome, lembrete):
    from main import receber_variaveis
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



