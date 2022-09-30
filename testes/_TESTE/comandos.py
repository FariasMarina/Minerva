from testes._TESTE.funcoes import carteira_acoes, financeiro, func, notas

lista_comandos = {
                      'criar rotina': func.criar_rotina,

                      'pesquise * no youtube': func.pesquisar_youtube,
                      'pesquise vídeo de *': func.pesquisar_youtube,
                      'pesquise vídeo da *': func.pesquisar_youtube,
                      'pesquise vídeo do *': func.pesquisar_youtube,
                      'pesquise vídeos de *': func.pesquisar_youtube,
                      'pesquise vídeos da *': func.pesquisar_youtube,
                      'pesquise vídeos do *': func.pesquisar_youtube,


                      'pesquise *': func.pesquisar_google,

                      'apresentar': func.apresentar,
                      'se apresente': func.apresentar,
                      'se apresenta': func.apresentar,
                      
                      'piada': func.piadas,
                      'me faça rir': func.piadas,

                      'desligar computador': func.Desligar_pc,
                      'abrir arquivo *': func.Abrir_arquivo,

                      'frase motivacional': func.frases,

                      'calcule *': func.calculadora,
                      'some *': func.calculadora,
                      'subtraia *': func.calculadora,
                      'divida *': func.calculadora,
                      'multiplique *': func.calculadora,

                      'dia é hoje': func.diga_data,
                      'data é hoje': func.diga_data,
                      'dia de hoje': func.diga_data,
                      'data de hoje': func.diga_data,

                      'horas são': func.diga_hora,
                      'horas é': func.diga_hora,
                      'hora são': func.diga_hora,
                      'hora é': func.diga_hora,

                      'adicionar gasto *': financeiro.adicionar,
                      'anotar gasto *': financeiro.adicionar,
                      'gastei *': financeiro.adicionar,
                      
                      'mostrar gastos': financeiro.listar_gastos_mes,
                      'listar gastos': financeiro.listar_gastos_mes,
                      'liste os gastos': financeiro.listar_gastos_mes,

                      'total de gastos do mês': financeiro.soma_total_mes,
                      'soma de gastos do mês': financeiro.soma_total_mes,

                      'anote *': notas.adicionar_nota,
                      'adicionar nota *': notas.adicionar_nota,

                      'mostre minhas notas': notas.mostrar_todas_notas,
                      'minhas notas': notas.mostrar_todas_notas,
                      'mostre as minhas notas': notas.mostrar_todas_notas,
                      'listar notas': notas.mostrar_todas_notas,
                      'ler notas': notas.mostrar_todas_notas,

                      'mostrar notas de hoje': notas.mostrar_nota_dia,
                      'mostrar as notas de hoje': notas.mostrar_nota_dia,
                      'mostre as notas de hoje': notas.mostrar_nota_dia,
                      'mostre notas de hoje': notas.mostrar_nota_dia,

                      'lembrete *': notas.adicionar_lembrete,
                      'me lembre de *': notas.adicionar_lembrete,
                      'lembre *': notas.adicionar_lembrete,
                      'me lembra de *': notas.adicionar_lembrete,
                      'me da um toque *': notas.adicionar_lembrete,


                      'qual a temperatura *': func.temperatura,
                      'temperatura em *': func.temperatura,
                      'temperatura *': func.temperatura,
                      'qual a temperatura agora': func.temperatura,
                      'qual a previsão do tempo agora': func.temperatura,
                      'qual a previsão do tempo em *': func.temperatura,
                      'qual a previsão do tempo para *': func.temperatura,
                      'previsão do tempo': func.temperatura,

                      'toque * musica': func.tocar_musica,
                      'tocar *': func.tocar_musica,
                      'toque *': func.tocar_musica,

                      'fale *': func.fale,

                      "procurar ação *": carteira_acoes.procurar_acao,
                      "mostrar cotação da *": carteira_acoes.mostrar_cotacao,
                      "mostrar carteira": carteira_acoes.ver_carteira,


}

