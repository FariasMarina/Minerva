'''Manter integrado com arquivo Excel 'Carteira.xlsx'.'''


from sys import displayhook
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from datetime import date

def procurar_acao(nome):
    ts = TimeSeries(key='2DIXCKIAIXV1A1Z9', output_format='pandas')
    return print(ts.get_symbol_search(nome))


def umanoatras(): #Não mexer
    data_atual = date.today()
    ano = int(data_atual.year)-1
    data = data_atual.strftime(f'{ano}-%m-%d')
    return data


def mostrar_cotacao(acao):
    cotacao = web.DataReader(f'{acao}', data_source='yahoo', start=umanoatras(), end=str(date.today()))
    displayhook(cotacao)
    plt.figure(figsize=(15, 6))
    displayhook(plt.plot(cotacao))
    plt.title(acao)
    plt.grid(axis='y')
    plt.show()


def ver_carteira():
    carteira = pd.read_excel('Carteira.xlsx')
    tab_acoes = {}
    for acao in carteira['Ativos']:
        cotacao = web.DataReader(acao, data_source='yahoo', start=str(date.today()), end=str(date.today()))
        tab_acoes[acao] = cotacao
        carteira.loc[carteira['Ativos'] == acao, 'Valor'] = carteira.loc[carteira['Ativos'] == acao, 'Qtde'].values * \
                                                            cotacao.loc[str(date.today()), 'Adj Close']
    return displayhook(carteira)


def ver_tab_cotacoes():
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
    print(f'Retorno Carteira: {retorno_carteira:.4f}')
    print(f'Retorno Carteira: {retorno_carteira:.4%}')
    carteira_ajustado.plot()
    tab_cotacoes.plot()  # porcentagem de cada ação
    plt.show()
    return displayhook(tab_cotacoes)




#procurar_acao('ambev')
#umanoatras()
#mostrar_cotacao('ITUB4.SA')
#ver_carteira() #ADICIONAR GRÁFICO PIZZA(mostrar total da carteira)
#ver_tab_cotacoes()
