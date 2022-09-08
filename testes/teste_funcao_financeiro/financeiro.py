import sqlite3
import datetime
from src.Minerva.testes.teste_geral import receber_variaveis

banco = sqlite3.connect(r'/testes/src\Minerva\testes\teste_funcao_financeiro\bancoteste.db')
cursor = banco.cursor()

#Cria o banco
def criar_banco():
    cursor.execute("CREATE TABLE IF NOT EXISTS bancoteste("
                   "ID integer primary key AUTOINCREMENT,"
                   "data text, "
                   "descricao text, "
                   "valor real, "
                   "categoria text,"
                   "FOREIGN KEY (categoria) REFERENCES bancoteste (descricao))")
criar_banco()

# adiciona novo dado podendo escolher a data
def adicionar_com_data(data, descricao, valor, categoria):

    descricao = receber_variaveis("Qual o nome da conta?")
    valor = receber_variaveis("Qual o valor da conta?")
    categoria = receber_variaveis("Esse conta é fixa ou variavel?")

    cursor.execute(f"INSERT INTO bancoteste(data, descricao, valor, categoria) VALUES(?,?,?,?)", (data, descricao, valor, categoria))  # inserir valores
    banco.commit()
    return print('adicionado')
# adicionar_com_data('2022-08-10', 'NetFlix', 1829.21, 'variável')


# adiciona novo dado com a data do computador
def adicionar():
    data = receber_variaveis("Qual a data?")
    if data == "hoje":

        descricao = receber_variaveis("Qual o nome da conta?")
        valor = receber_variaveis("Qual o valor da conta?")
        categoria = receber_variaveis("Esse conta é fixa ou variavel?")
        data = datetime.datetime.now()
        dataauto = str(data.date())
        cursor.execute(f"INSERT INTO bancoteste(data, descricao, valor, categoria) VALUES(?,?,?,?)", (dataauto, descricao, valor, categoria))
        banco.commit()
        return print('adicionado')
    else:
        adicionar_com_data(data)
# adicionar('agua', 156, 'fixo')



def mudar_data(id, ano, mes, dia):
   cursor.execute(f"UPDATE bancoteste SET data='{ano}-{mes}-{dia}' "
                  f"WHERE ID='{id}'") # mudar informações
   banco.commit()
   return print('mudado')
# mudar_data('40', '2020', '02', '17')


def mudar_descricao(id, descricao):
    cursor.execute(f"UPDATE bancoteste SET descricao='{descricao}' "
                   f"WHERE ID='{id}'")
    banco.commit()
    return print('mudado')
# mudar_descricao('3', 'internet')


def mudar_valor(id, valor):
    cursor.execute(f"UPDATE bancoteste SET valor='{valor}' "
                   f"WHERE id='{id}'")
    banco.commit()
    return print('mudado')
# mudar_valor('1', 300)


def mudar_categoria(id, cat):
    cursor.execute(f"UPDATE bancoteste SET categoria='{cat}' "
                   f"WHERE id='{id}'")
    banco.commit()
    return print('mudado')
# mudar_categoria('1', 'fixo')


def deletar(id):
   cursor.execute(f"DELETE FROM bancoteste WHERE id='{id}'")  # deletar dado
   banco.commit()
   return print('deletado')
# deletar('17')


# mostra todos os dados do banco
def filtrar_tudo():
    cursor.execute("SELECT * FROM bancoteste ORDER BY data")
    res = cursor.fetchall()
    for i in res:
        print(i)
    return print('feito')
# filtrar_tudo()


# filtra dados por data
def filtrar_data(ano, mes, dia):
    cursor.execute(f'SELECT * FROM bancoteste WHERE data="{ano}-{mes}-{dia}"')
    res = cursor.fetchall()
    for i in res:
        print(i)
    return print('feito')
# filtrar_data('2022', '10', '20')


# filtra dados entre duas datas
def filtrar_data_entre(ano, mes, dia, ano1, mes1, dia1):
    cursor.execute(f"SELECT * FROM bancoteste WHERE data BETWEEN '{ano}-{mes}-{dia}' AND '{ano1}-{mes1}-{dia1}' ORDER BY data")
    res = cursor.fetchall()
    for i in res:
        print(i)
    return print('feito')
# filtrar_data_entre('2020', '03', '11', '2022', '12', '17') #2020-03-11     2022-12-17


# filtra dados por descrição
def filtrar_descricao(descr):
    cursor.execute(f"SELECT * FROM bancoteste WHERE descricao='{descr}'")
    res = cursor.fetchall()
    for i in res:
        print(i)
    return print('feito')
# filtrar_descricao('energia')


# filtra dados por categoria
def filtrar_categoria(cat):
    cursor.execute(f"SELECT * FROM bancoteste WHERE categoria='{cat}'")
    res = cursor.fetchall()
    for i in res:
        print(i)
    return print('feito')
# filtrar_categoria('fixo')


# mostra o total das contas do mês (dia 01 ao 31)
def soma_total_mes(*args):
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
    return f'o total do mês é {soma}'
# soma_total_mes()


# mostra o total das contas de certa categoria (fixo ou variável) do dia 01 ao 31
def soma_total_categoria(tipo):
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
