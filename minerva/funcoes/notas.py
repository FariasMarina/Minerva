from threading import Timer
import sqlite3
import datetime



banco = sqlite3.connect('BancoNotas.db', check_same_thread=False)
cursor = banco.cursor()


def criar_banco():
    try:
        cursor.execute('CREATE TABLE IF NOT EXISTS "Notas"('
                       '"ID" integer primary key AUTOINCREMENT,'
                       '"data" text not null,'
                       '"nome" text not null,'
                       '"notas" text not null)')
        banco.commit()
    except:
        return 'Não foi possivel criar o banco'


criar_banco()
def adicionar_nota(anotacao):
    try:
        print(anotacao)

        nome = "_"
        nota = anotacao
        dataauto = "-"
        cursor.execute(f"INSERT INTO Notas(data, nome, notas) VALUES(?,?,?)", (dataauto, nome, nota))
        banco.commit()
        return f'nota {nota} salva'
    except:
        return 'Não foi possivel adicionar nota'


def mostrar_nota_dia():
    try:
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
    except:
        return 'Não foi possivel mostrar a nota'


def mostrar_nota_nome(nome):
    from main import receber_variaveis
    try:
        nome = receber_variaveis('Qual o nome da nota?')
        cursor.execute(f"SELECT notas FROM Notas WHERE nome='{nome}'")
        res = cursor.fetchall()
        for i in res:
            tex = str(i)
            texto = tex.replace('(', '').replace(')', '').replace(',', '')
            print(texto)
    except:
        return 'Não foi possivel mostrar nota'


def mostrar_todas_notas():
    try:
        cursor.execute(f"SELECT notas, data FROM Notas")
        res = cursor.fetchall()
        resposta = []
        print(res)
        for i in res:
            if i[1] == '-':
                tex = str(i[0])
                texto = tex.replace('(', '').replace(')', '').replace(',', '')
                resposta.append(texto)
        return f"Voce tem as seguintes notas anotadas, {' e '.join(resposta)}"
    except:
        return 'Não foi possivel mostrar as notas'


def adicionar_lembrete(texto):

    try:

        texto2 = texto.split()
        # as 16 h para tirar o frangi
        # as 16 h de tirar o frangi
        # de tirar o frango as 16
        texto3 = "1"
        #TODO: remover palavras tipo... "Daqui", "Em" etc...
        for i in range(len(texto2)):
            try:
                data = int(texto2[i])
                if texto2[i+1] == "minutos" or texto2[i+1] == "minuto":
                    data = data * 60
                    texto3 = texto.replace("minutos", "").replace("minuto", "")
                elif texto2[i+1] == "horas" or texto2[i+1] == "hora":
                    data = data * 3600
                    texto3 = texto.replace("horas", "").replace("hora", "")
                elif texto2[i+1] == "segundos" or texto2[i+1] == "segundo":
                    data = data
                    texto3 = texto.replace("segundos", "").replace("segundo", "")
                break
            except:
                pass

        nome = "_"
        lembrete = texto3.replace(str(data), "")
        cursor.execute('INSERT INTO Notas(data, nome, notas) VALUES(?,?,?)', (data, nome, lembrete))
        banco.commit()
        print("Lembrete adicionado")
        temporizador = Timer(data, ler_Lembrete)
        temporizador.start()

        return 'Lembrete criado'
    except:
        return 'Não foi possivel adicionar lembrete'


def ler_Lembrete():
    print("TENTANDO LER LEMBRETE")
    import minerva.ui_main as t
    # try:
    cursor.execute(f"SELECT notas, data, ID FROM Notas")
    res = cursor.fetchall()
    resposta = None
    nota_mais_recente = 1000000
    id_nota_resposta = 0
    for i in res:
        if i[1] != '-':
            if int(nota_mais_recente) > int(i[1]):
                nota_mais_recente = i[1]
                id_nota_resposta = i[2]
                tex = str(i[0])
                texto = tex.replace('(', '').replace(')', '').replace(',', '')
                resposta = texto
    cursor.execute('DELETE FROM Notas WHERE ID=?', (id_nota_resposta, ))
    banco.commit()
    print(resposta)
    t.caixa_de_lembrete(f"Se lembre de {resposta.replace('daqui', '').replace('em', '')}")
    print("LEMBRETE LIDO")
        # t.janela.show()
    # except:
    #     print('Não foi possivel ler o lembrete')





# criar_banco()
# adicionar_nota('dog', 'levar dog para passear')
# mostrar_nota_dia('2022-09-12')
# mostrar_nota_nome('dog')
# mostrar_todas_notas()
# adicionar_lembrete('2022-09-13', 'remédio', 'tomar remédio')
# ler_Lembrete() #lê somente os do dia



