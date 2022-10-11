from testes._TESTE.funcoes import carteira_acoes, financeiro, func, notas
import matplotlib.pyplot as plt

lista_comandos = {
                      'criar rotina': func.criar_rotina,

                      'pesquise * no youtube': func.pesquisar_youtube,
                      'pesquise video de *': func.pesquisar_youtube,
                      'pesquise video da *': func.pesquisar_youtube,
                      'pesquise video do *': func.pesquisar_youtube,
                      'pesquise videos de *': func.pesquisar_youtube,
                      'pesquise videos da *': func.pesquisar_youtube,
                      'pesquise videos do *': func.pesquisar_youtube,


                      'pesquise *': func.pesquisar_google,

                      'apresentar': func.apresentar,
                      'se apresente': func.apresentar,
                      'se apresenta': func.apresentar,
                      
                      'piada': func.piadas,

                      'desligar computador': func.Desligar_pc,
                      'abrir arquivo *': func.Abrir_arquivo,

                      'frase motivacional': func.frases,

                      'calcule *': func.calculadora,
                      'some *': func.calculadora,
                      'subtraia *': func.calculadora,
                      'divida *': func.calculadora,
                      'multiplique *': func.calculadora,

                      'dia de hoje': func.diga_data,
                      'data de hoje': func.diga_data,

                      'que horas sao': func.diga_hora,
                      'que hora e': func.diga_hora,

                      'adicionar gasto *': financeiro.adicionar,
                      'anotar gasto *': financeiro.adicionar,
                      'gastei *': financeiro.adicionar,

                      'listar gastos': financeiro.listar_gastos_mes,

                      'total de gastos do mes': financeiro.soma_total_mes,
                      'soma de gastos do mes': financeiro.soma_total_mes,

                      'anote *': notas.adicionar_nota,

                      'ler notas': notas.mostrar_todas_notas,

                      'mostrar notas de hoje': notas.mostrar_nota_dia,

                      'me lembre de *': notas.adicionar_lembrete,
                      'me lembra de *': notas.adicionar_lembrete,

                      'qual a temperatura em *': func.temperatura,
                      'temperatura em *': func.temperatura,


                      'tocar *': func.tocar_musica,
                      'toque *': func.tocar_musica,

                      'fale *': func.fale,

                      "procurar açao *": carteira_acoes.procurar_acao,
                      "mostrar cotaçao da *": carteira_acoes.mostrar_cotacao,
                      "comparar * e *": carteira_acoes.comparar_cotacoes,
                      "mostrar carteira *": carteira_acoes.ver_carteira,
                      "mostrar tabela da carteira": carteira_acoes.ver_tab_carteira,
                      "comparar carteira com cotaçao da *": carteira_acoes.comparar_cotacao_carteira,




                      '@ a': 'a', 
                      '@ a': 'a', 
}

