from sys import displayhook
import numpy as np
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from datetime import date

from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.backends.backend_qtagg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QHeaderView

# pip instaall openpyxl


def procurar_acao(nome):
    ts = TimeSeries(key='2DIXCKIAIXV1A1Z9', output_format='pandas')
    return type(ts)

def umanoatras():
    data_atual = date.today()
    ano = int(data_atual.year)-1
    data = data_atual.strftime(f'{ano}/%m/%d')
    return data


def mostrar_cotacao(acao):
    from ui_main import grafico
    cotacao = web.DataReader(f'{acao}', data_source='yahoo', start=umanoatras(), end=str(date.today()))
    displayhook(cotacao)
    df = cotacao

    columns = [df.index.name] + [i for i in df.columns]
    rows = [[i for i in row] for row in df.itertuples()]
    print(columns, rows)

    grafico.tableWidget.setRowCount(len(rows) + 1)
    grafico.tableWidget.setColumnCount(len(columns))

    grafico.tableWidget.setHorizontalHeaderLabels(columns)

    count = 0
    for i in rows:
        count2 = 0
        for j in i:
            grafico.tableWidget.setItem(count, count2, QTableWidgetItem(f"{j}"))
            count2 += 1
        count += 1

    grafico.tableWidget.horizontalHeader().setStretchLastSection(True)
    grafico.tableWidget.horizontalHeader().setSectionResizeMode(
        QHeaderView.Stretch)

    # plt.figure(figsize=(15, 6))
    # displayhook(plt.plot(cotacao['Adj Close']))
    # plt.title(acao)
    # plt.grid(axis='y')
    # plt.show()

    layout = QtWidgets.QVBoxLayout(grafico.tab)
    static_canvas = FigureCanvas(Figure(figsize=(7, 3)))

    layout.addWidget(static_canvas)  # adicionando tabela


    grafico._static_ax = static_canvas.figure.subplots()

    grafico._static_ax.plot(cotacao['Adj Close'])
    grafico._static_ax.set_title(acao)

    grafico.show()

def ver_carteira():
    from ui_main import grafico
    carteira = pd.read_excel('Carteira.xlsx')
    tab_acoes = {}

    for acao in carteira['Ativos']:
        cotacao = web.DataReader(acao, data_source='yahoo', start=str(date.today()), end=str(date.today()))
        tab_acoes[acao] = cotacao
        carteira.loc[carteira['Ativos'] == acao, 'Valor'] = carteira.loc[carteira['Ativos'] == acao, 'Qtde'].values * \
                                                            cotacao.loc[str(date.today()), 'Adj Close']

    displayhook(carteira)

    dict = {}
    for acao in carteira['Ativos']:
        dict[acao] = float(carteira.loc[carteira['Ativos'] == acao, 'Valor'])

    qtde = []
    nome = []
    for i in sorted(dict, key=dict.get):
        qtde.append(dict[i])
        nome.append(i)

    y = np.array(qtde)
    x = np.array(nome)

    df = carteira
    columns = [df.index.name] + [i for i in df.columns]
    rows = [[i for i in row] for row in df.itertuples()]
    print(columns, rows)

    grafico.tableWidget.setRowCount(len(rows) + 1)
    grafico.tableWidget.setColumnCount(len(columns))

    grafico.tableWidget.setHorizontalHeaderLabels(columns)

    count = 0
    for i in rows:
        count2 = 0
        for j in i:
            grafico.tableWidget.setItem(count, count2, QTableWidgetItem(f"{j}"))
            count2 += 1
        count += 1

    grafico.tableWidget.horizontalHeader().setStretchLastSection(True)
    grafico.tableWidget.horizontalHeader().setSectionResizeMode(
        QHeaderView.Stretch)



    # plt.barh(x, y)
    # plt.show()
    layout = QtWidgets.QVBoxLayout(grafico.tab)
    static_canvas = FigureCanvas(Figure(figsize=(7, 3)))

    layout.addWidget(static_canvas)  # adicionando tabela


    grafico._static_ax = static_canvas.figure.subplots()

    grafico._static_ax.barh(x, y)

    grafico.show()

    return "Feito"


def comparar_cotacoes(acao1):
    from ui_main import grafico
    acao2= acao1.split()[1]
    acao1= acao1.split()[0]
    cotacao1 = web.DataReader(f'{acao1}', data_source='yahoo', start=umanoatras(), end=str(date.today()))
    cotacao2 = web.DataReader(f'{acao2}', data_source='yahoo', start=umanoatras(), end=str(date.today()))

    cot1_ajustado = cotacao1['Adj Close'] / cotacao1['Adj Close'].iloc[0]
    cot2_ajustado = cotacao2['Adj Close'] / cotacao2['Adj Close'].iloc[0]

    retorno_cot1 = cot1_ajustado[-1] - 1
    retorno_cot2 = cot2_ajustado[-1] - 1



    # plt.figure(figsize=(15, 6))
    # plt.subplot(2, 1, 1)
    # plt.plot(cotacao1['Adj Close'], color='b')
    # plt.ylabel(f'Retorno: {retorno_cot1:.4%}')
    # plt.title(acao1)
    # plt.grid(axis='y')
    #
    # plt.subplot(2, 1, 2)
    # plt.plot(cotacao2['Adj Close'])
    # plt.ylabel(f'Retorno: {retorno_cot2:.4%}')
    # plt.title(acao2)
    # plt.grid(axis='y')
    # plt.show()

    layout = QtWidgets.QVBoxLayout(grafico.tab)
    static_canvas = FigureCanvas(Figure(figsize=(7, 3)))
    static_canvas2 = FigureCanvas(Figure(figsize=(7, 3)))
    layout.addWidget(static_canvas)  # adicionando tabela
    layout.addWidget(static_canvas2)  # adicionando tabela

    grafico._static_ax = static_canvas.figure.subplots()
    grafico._static_ax.set_title(acao1)
    grafico._static_ax.set_ylabel(f'Retorno: {retorno_cot1:.4%}')
    grafico._static_ax.plot(cotacao1['Adj Close'], color='b')


    grafico._static_ax2 = static_canvas2.figure.subplots()
    grafico._static_ax2.set_ylabel(f'Retorno: {retorno_cot2:.4%}')
    grafico._static_ax.set_title(acao2)
    grafico._static_ax2.plot(cotacao2['Adj Close'])

    grafico.show()
    return (f'Retorno {acao1}: {retorno_cot1:.4%} \nRetorno {acao2}: {retorno_cot2:.4%}')


def comparar_cotacao_carteira(acao1):
    from ui_main import grafico
    acao1 = acao1.upper()
    print(acao1)
    carteira = pd.read_excel('Carteira.xlsx')
    data_inicial = umanoatras()
    tab_acoes = {}
    for acao in carteira['Ativos']:
        cotacao = web.DataReader(acao, data_source='yahoo', start=umanoatras(), end=str(date.today()))
        tab_acoes[acao] = cotacao
        carteira.loc[carteira['Ativos'] == acao, 'Valor'] = carteira.loc[carteira['Ativos'] == acao, 'Qtde'].values * \
                                                            cotacao.loc[str(date.today()), 'Adj Close']
    tab_cotacoes = pd.DataFrame()
    for acao in tab_acoes:
        tab_cotacoes[acao] = tab_acoes[acao].loc[umanoatras(): str(date.today()), 'Adj Close']
    for acao in tab_cotacoes.columns:
        tab_cotacoes[acao] = tab_cotacoes[acao] * carteira.loc[carteira['Ativos'] == acao, 'Qtde'].values
    tab_cotacoes['Total'] = tab_cotacoes.sum(axis=1)
    carteira_ajustado = tab_cotacoes['Total'] / tab_cotacoes['Total'].iloc[0]  # porcentagem da carteira
    retorno_carteira = carteira_ajustado[-1] - 1

    cotacao = web.DataReader(f'{acao1}', data_source='yahoo', start=umanoatras(), end=str(date.today()))
    cot_ajustado = cotacao['Adj Close'] / cotacao['Adj Close'].iloc[0]
    retorno_cot = cot_ajustado[-1] - 1



    # plt.figure(figsize=(15, 6))
    # plt.subplot(2, 1, 1)
    # plt.plot(cotacao['Adj Close'], color='purple')
    # plt.ylabel(f'Retorno: {retorno_cot:.4%}')
    # plt.title(acao1)
    # plt.grid(axis='y')
    #
    # plt.subplot(2, 1, 2)
    # plt.plot(tab_cotacoes['Total'])
    # plt.ylabel(f'Retorno: {retorno_carteira:.4%}')
    # plt.title('Carteira')
    # plt.grid(axis='y')
    # plt.show()

    layout = QtWidgets.QVBoxLayout(grafico.tab)
    static_canvas = FigureCanvas(Figure(figsize=(7, 3)))
    static_canvas2 = FigureCanvas(Figure(figsize=(7, 3)))
    layout.addWidget(static_canvas)  # adicionando tabela
    layout.addWidget(static_canvas2)  # adicionando tabela


    grafico._static_ax = static_canvas.figure.subplots()
    grafico._static_ax.set_title(acao1)
    grafico._static_ax.set_ylabel(f'Retorno: {retorno_cot:.4%}')
    grafico._static_ax.plot(cotacao['Adj Close'], color='purple')


    grafico._static_ax2 = static_canvas2.figure.subplots()
    grafico._static_ax2.set_ylabel(f'Retorno: {retorno_carteira:.4%}')
    grafico._static_ax.set_title("Carteira")
    grafico._static_ax2.plot(tab_cotacoes['Total'])

    grafico.show()
    return (f'Retorno {acao1}: {retorno_cot:.4%} \n Retorno Carteira: {retorno_carteira:.4%}')



def ver_tab_carteira():
    from ui_main import grafico
    carteira = pd.read_excel('Carteira.xlsx')
    data_inicial = umanoatras()
    tab_acoes = {}

    for acao in carteira['Ativos']:
        cotacao = web.DataReader(acao, data_source='yahoo', start=umanoatras(), end=str(date.today()))
        tab_acoes[acao] = cotacao
        carteira.loc[carteira['Ativos'] == acao, 'Valor'] = carteira.loc[carteira['Ativos'] == acao, 'Qtde'].values #* \
                                                            # cotacao.loc[str(date.today()), 'Adj Close'] #PC JOILSON SO FUNCIONOU ASSIM

    tab_cotacoes = pd.DataFrame()
    for acao in tab_acoes:
        tab_cotacoes[acao] = tab_acoes[acao].loc[umanoatras(): str(date.today()), 'Adj Close']

    for acao in tab_cotacoes.columns:
        tab_cotacoes[acao] = tab_cotacoes[acao] * carteira.loc[carteira['Ativos'] == acao, 'Qtde'].values

    tab_cotacoes['Total'] = tab_cotacoes.sum(axis=1)
    carteira_ajustado = tab_cotacoes['Total'] / tab_cotacoes['Total'].iloc[0]  # porcentagem da carteira
    retorno_carteira = carteira_ajustado[-1] - 1
    print(f'Retorno Carteira: {retorno_carteira:.4%}')
    displayhook(tab_cotacoes)

    df = tab_cotacoes
    columns = [df.index.name] + [i for i in df.columns]
    rows = [[i for i in row] for row in df.itertuples()]
    print(columns, rows)


    grafico.tableWidget.setRowCount(len(rows) + 1)
    grafico.tableWidget.setColumnCount(len(columns))

    grafico.tableWidget.setHorizontalHeaderLabels(columns)

    count = 0
    for i in rows:
        count2 = 0
        for j in i:
            grafico.tableWidget.setItem(count, count2, QTableWidgetItem(f"{j}"))
            count2 += 1
        count += 1

    grafico.tableWidget.horizontalHeader().setStretchLastSection(True)
    grafico.tableWidget.horizontalHeader().setSectionResizeMode(
        QHeaderView.Stretch)

    # plt.figure(figsize=(15, 6))
    # plt.subplot(2, 1, 1)
    # plt.plot(tab_cotacoes['Total'])
    # plt.title('Carteira')
    #
    # plt.subplot(2, 1, 2)
    # plt.plot(tab_cotacoes.drop(columns=['Total']), label=carteira['Ativos'])
    # plt.title('Ações da Carteira')
    # plt.grid(axis='y')
    # plt.legend()
    # plt.show()

    layout = QtWidgets.QVBoxLayout(grafico.tab)

    static_canvas = FigureCanvas(Figure(figsize=(7, 3)))
    static_canvas2 = FigureCanvas(Figure(figsize=(7, 3)))
    layout.addWidget(static_canvas)  # adicionando tabela
    layout.addWidget(static_canvas2)  # adicionando tabela




    grafico._static_ax = static_canvas.figure.subplots()
    grafico._static_ax.set_title("Carteira")
    grafico._static_ax.plot(tab_cotacoes['Total'])


    grafico._static_ax2 = static_canvas2.figure.subplots()
    grafico._static_ax.set_title("Ações Carteira")
    # grafico._static_ax.get_legend()
    grafico._static_ax2.plot(tab_cotacoes.drop(columns=['Total']), label=carteira['Ativos'])

    grafico.show()

    return 'Feito'




# comparar_cotacao_carteira('ITUB4.SA')
# comparar_cotacoes('ITUB4.SA VALE3.SA')
# ver_tab_carteira()  # OK
# ver_carteira() # OK
# mostrar_cotacao('VALE3.SA') # OK
# print(procurar_acao('ibov')) #OK


