from sys import displayhook
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from datetime import date


def procurar_acao(nome):
    ts = TimeSeries(key='2DIXCKIAIXV1A1Z9', output_format='pandas')
    return ts.get_symbol_search(nome)


def umanoatras():
    data_atual = date.today()
    ano = int(data_atual.year)-1
    data = data_atual.strftime(f'{ano}/%m/%d')
    return data


def mostrar_cotacao(acao):
    cotacao = web.DataReader(f'{acao}', data_source='yahoo', start=umanoatras(), end=str(date.today()))
    displayhook(cotacao)
    plt.figure(figsize=(15, 6))
    displayhook(plt.plot(cotacao))
    plt.title(acao)
    plt.grid(axis='y')


def ver_carteira():
    carteira = pd.read_excel('B3/Carteira.xlsx')
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
    carteira_ajustado.plot()
    tab_cotacoes.plot()  # porcentagem de cada ação

    retorno_carteira = carteira_ajustado[-1] - 1
    print(f'Retorno Carteira: {retorno_carteira:.4%}')

    return displayhook(tab_cotacoes)


def comparar_cotacoes(acao1, acao2):
    cotacao1 = web.DataReader(f'{acao1}', data_source='yahoo', start=umanoatras(), end=str(date.today()))
    cotacao2 = web.DataReader(f'{acao2}', data_source='yahoo', start=umanoatras(), end=str(date.today()))

    cot1_ajustado = cotacao1['Adj Close'] / cotacao1['Adj Close'].iloc[0]
    cot2_ajustado = cotacao2['Adj Close'] / cotacao2['Adj Close'].iloc[0]

    retorno_cot1 = cot1_ajustado[-1] - 1
    retorno_cot2 = cot2_ajustado[-1] - 1

    print(f'Retorno {acao1}: {retorno_cot1:.4%}')
    print(f'Retorno {acao2}: {retorno_cot2:.4%}')


def comparar_cotacao_carteira(acao1):
    carteira = pd.read_excel('B3/Carteira.xlsx')
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

    print(f'Retorno {acao1}: {retorno_cot:.4%}')
    print(f'Retorno Carteira: {retorno_carteira:.4%}')




# comparar_cotacao_carteira('ITUB4.SA')  # INTEGRAR GRÁFICOS PYQT5
# comparar_cotacoes('ITUB4.SA', 'VALE3.SA')  # INTEGRAR GRÁFICOS PYQT5
# ver_tab_carteira()  # CONSERTAR GRÁFICOS E INTEGRAR COM PYQT5
# ver_carteira()  # ADICIONAR GRÁFICO PIZZA PYQT5(mostrar total da carteira)
# mostrar_cotacao('VALE3.SA') #INTEGRAR COM PYQT5
# umanoatras()
# procurar_acao('ibov')


