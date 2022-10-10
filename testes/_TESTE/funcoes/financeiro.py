import sqlite3 as sqlite3
import datetime

banco = sqlite3.connect(r'bancoteste.db')
cursor = banco.cursor()



#=== JA IMPLEMENTADAS ===



# adiciona novo dado com a data do computador
def adicionar(text):
    try:


        if "mensal" in text:
            categoria = "fixa"
        else:
            categoria = "variavel"

        for i in text.split():
            try:
                valor = int(i)
                break
            except:
                pass
        else:
            return "Desculpe, mas nenhum valor foi informado"

        for i in range(len(text.split())):
            if text.split()[i] == "com":
                descricao = ' '.join(text.split()[i+1:])
                break
        else:
            descricao = "Alguma coisa"


        data = datetime.datetime.now()
        dataauto = str(data.date())
        cursor.execute(f"INSERT INTO bancoteste(data, descricao, valor, categoria) VALUES(?,?,?,?)", (dataauto, descricao, valor, categoria))
        banco.commit()
        return f'Adicionado {valor} reais gastos com {descricao}'
    except:
        return 'Não foi possivel adicionar o valor'



def deletar(text):
    try:
       id = receber_variaveis('Qual o numero da conta?')
       cursor.execute(f"DELETE FROM bancoteste WHERE id='{id}'")  # deletar dado
       banco.commit()
       return 'Deletado'
    # deletar('17')
    except:
        return 'Não foi possivel deletar a conta'


# mostra o total das contas do mês (dia 01 ao 31)
def soma_total_mes():
    try:
        data = datetime.datetime.now()
        ano = str(data.date())[:4]
        mes = str(data.date())[5:7]
        mes2 = int(mes)+1
        cursor.execute(f"SELECT * FROM bancoteste WHERE data BETWEEN '{ano}-{mes}-01' AND '{ano}-{mes2}-31'")
        res = cursor.fetchall()
        list = []
        for i in res:
            list.append(float(i[3]))
        soma = sum(list)
        return f'O total do mês é {soma}'
    # soma_total_mes()
    except:
        return 'Não foi possivel fazer a soma'


def listar_gastos_mes():
    try:
        data = datetime.datetime.now()
        ano = str(data.date())[:4]
        mes = str(data.date())[5:7]
        mes2 = int(mes)+1
        cursor.execute(f"SELECT * FROM bancoteste WHERE data BETWEEN '{ano}-{mes}-01' AND '{ano}-{mes2}-31'")
        res = cursor.fetchall()
        list = []
        for i in res:
            list.append(f"dia {i[1]} foram gastos {i[3]} reais com {i[2]} ")
        return f'{list}'
    except:
        return 'Não foi possivel listar os gastos'




#=== === ===



#Cria o banco
def criar_banco():
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS bancoteste("
                       "ID integer primary key AUTOINCREMENT,"
                       "data text, "
                       "descricao text, "
                       "valor real, "
                       "categoria text,"
                       "FOREIGN KEY (categoria) REFERENCES bancoteste (descricao))")
    # criar_banco()
    except:
        return 'Não foi possivel criar o banco'








def mudar_data(id, ano, mes, dia):
    try:
       cursor.execute(f"UPDATE bancoteste SET data='{ano}-{mes}-{dia}' "
                      f"WHERE ID='{id}'") # mudar informações
       banco.commit()
       return print('Mudado')
    # mudar_data('40', '2020', '02', '17')
    except:
        return 'Não foi possivel mudar a data'


def mudar_descricao(id, descricao):
    try:
        cursor.execute(f"UPDATE bancoteste SET descricao='{descricao}' "
                       f"WHERE ID='{id}'")
        banco.commit()
        return print('Mudado')
    # mudar_descricao('3', 'internet')
    except:
        return 'Não foi possivel mudar a descrição'


def mudar_valor(id, valor):
    try:
        cursor.execute(f"UPDATE bancoteste SET valor='{valor}' "
                       f"WHERE id='{id}'")
        banco.commit()
        return print('Mudado')
    # mudar_valor('1', 300)
    except:
        return 'Não foi possivel mudar o valor'


def mudar_categoria(id, cat):
    try:
        cursor.execute(f"UPDATE bancoteste SET categoria='{cat}' "
                       f"WHERE id='{id}'")
        banco.commit()
        return print('Mudado')
    # mudar_categoria('1', 'fixo')
    except:
        return 'Não foi possivel mudar a categoria'





# mostra todos os dados do banco
def filtrar_tudo():
    try:
        cursor.execute("SELECT * FROM bancoteste ORDER BY data")
        res = cursor.fetchall()
        for i in res:
            print(i)
        return print('Feito')
    # filtrar_tudo()
    except:
        return 'Não foi possivel filtrar'


# filtra dados por data
def filtrar_data(ano, mes, dia):
    try:
        cursor.execute(f'SELECT * FROM bancoteste WHERE data="{ano}-{mes}-{dia}"')
        res = cursor.fetchall()
        for i in res:
            print(i)
        return print('Feito')
    # filtrar_data('2022', '10', '20')
    except:
        return 'Não foi possivel filtrar'


# filtra dados entre duas datas
def filtrar_data_entre(ano, mes, dia, ano1, mes1, dia1):
    try:
        cursor.execute(f"SELECT * FROM bancoteste WHERE data BETWEEN '{ano}-{mes}-{dia}' AND '{ano1}-{mes1}-{dia1}' ORDER BY data")
        res = cursor.fetchall()
        for i in res:
            print(i)
        return print('Feito')
    # filtrar_data_entre('2020', '03', '11', '2022', '12', '17') #2020-03-11     2022-12-17
    except:
        return 'Não foi possivel filtrar'


# filtra dados por descrição
def filtrar_descricao(descr):
    try:
        cursor.execute(f"SELECT * FROM bancoteste WHERE descricao='{descr}'")
        res = cursor.fetchall()
        for i in res:
            print(i)
        return print('Feito')
    # filtrar_descricao('energia')
    except:
        return 'Não foi possivel filtrar'


# filtra dados por categoria
def filtrar_categoria(cat):
    try:
        cursor.execute(f"SELECT * FROM bancoteste WHERE categoria='{cat}'")
        res = cursor.fetchall()
        for i in res:
            print(i)
        return print('Feito')
    # filtrar_categoria('fixo')
    except:
        return 'Não foi possivel filtrar'





# mostra o total das contas de certa categoria (fixo ou variável) do dia 01 ao 31
def soma_total_categoria(tipo):
    try:
        data = datetime.datetime.now()
        ano = str(data.date())[:4]
        mes = str(data.date())[5:7]
        cursor.execute(f"SELECT valor FROM bancoteste WHERE categoria='{tipo}' AND data BETWEEN '{ano}-{mes}-01' AND '{ano}-{mes}-31'")
        res = cursor.fetchall()
        lista = []
        for i in res:
            s = str(i)
            n = float(s.replace('(', '').replace(',', '').replace(')', ''))
            lista.append(n)
        soma = sum(lista)
        return print(soma)
    # soma_total_categoria('variável')
    except:
        return 'Não foi possivel somar'
