from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QEvent
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QIcon
import main

from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.backends.backend_qtagg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import keyboard




# def aparecer_graficos(title, ylabel, primeiro_arg, segundo_arg,
#                       dois_graficos = False, title2 = None, ylabel2 = None, primeiro_arg2 = None, segundo_arg2 = None,
#                       barra = False):
#     layout = QtWidgets.QVBoxLayout(grafico.tab)
#
#     static_canvas = FigureCanvas(Figure(figsize=(7, 3)))
#
#
#     # layout.addWidget(static_canvas, janela)) #adicionando navegaçao
#     layout.addWidget(static_canvas)  # adicionando tabela
#
#
#
#     grafico._static_ax = static_canvas.figure.subplots()
#
#     grafico._static_ax.set_title(title)
#     grafico._static_ax.set_ylabel(ylabel)
#     grafico._static_ax.plot(primeiro_arg, segundo_arg)
#
#     if dois_graficos:
#         static_canvas2 = FigureCanvas(Figure(figsize=(7, 3)))
#         layout.addWidget(static_canvas2)  # adicionando tabela
#         grafico._static_ax2 = static_canvas2.figure.subplots()
#         grafico._static_ax2.set_title(title2)
#         grafico._static_ax2.set_ylabel(ylabel2)
#         grafico._static_ax2.plot(primeiro_arg2, segundo_arg2)
#
#     grafico.show()
#     return "teste"


def aparecer_cadastro_rotina():
    global rotina
    rotina = uic.loadUi("rotina.ui")
    rotina.listWidget.setVisible(False)
    rotina.pushButton.clicked.connect(chamar_cadastrar_rotina)
    # print(bool(rotina.pushButton.clicked))
    rotina.lineEdit_2.textChanged.connect(update_display_rotina)
    rotina.listWidget.clicked.connect(clicked_rotina)
    rotina.listWidget.clicked.connect(clicked_rotina)
    rotina.pushButton_2.clicked.connect(adicionar_item_lista_e_limpar_linha)
    rotina.pushButton_3.clicked.connect(deletar_item_lista)
    rotina.show()
    return "Preencha os campos para cadastrar uma nova rotina"



def deletar_item_lista():
    item = rotina.listWidget_2.currentRow()
    print(item)
    rotina.listWidget_2.takeItem(item)
def adicionar_item_lista_e_limpar_linha():
    rotina.listWidget_2.insertItem(rotina.listWidget_2.count(), rotina.lineEdit_2.text())
    rotina.lineEdit_2.setText("")


def update_display_rotina():
    text = rotina.lineEdit_2.text()
    comandos = main.receber_lista_comandos_atualizada()
    if "/" in text:
        rotina.listWidget.setVisible(True)
        text = text.replace("/", "")

        comandos_filtro = []

        for widget in comandos:
            if text.lower() in widget.lower():
                comandos_filtro.append(widget)

        rotina.listWidget.clear()
        for i in comandos_filtro:
            rotina.listWidget.insertItem(2, i)

    else:
        rotina.listWidget.setVisible(False)


def chamar_cadastrar_rotina():
    import testes._TESTE.funcoes.func as t
    global rotina
    rotina.close()
    items = [rotina.listWidget_2.item(x).text() for x in range(rotina.listWidget_2.count())]
    t.a(rotina.lineEdit.text(), ", ".join(items))


timeline_de_comandos = ["comparar ITUB4.SA e VALE3.SA"]


def clicked_rotina():
    a = rotina.listWidget.currentItem()

    rotina.lineEdit_2.setText(a.text().replace("*", ""))


def clicked():
    a = janela.listWidget.currentItem()

    if "*" in a.text():
        janela.lineEdit.setText(a.text().replace("*", ""))
    else:
        timeline_de_comandos.append(a.text())
        janela.label_2.setText(main.run_minerva(input_texto=a.text().replace("@", "").replace("/", "")))
        janela.lineEdit.setText("")


def clicked_by_enter():
    global index_timeline
    a = janela.lineEdit.text()
    timeline_de_comandos.append(a)
    index_timeline = 0
    janela.label_2.setText(main.run_minerva(input_texto=a.replace("@", "").replace("/", "")))
    janela.lineEdit.setText("")


def clicked_on_microphone():
    try:
        janela.label_2.setText(main.run_minerva(input_microfone=True))
    except:
        janela.label_2.setText("Nenhum microfone reconhecido")


def caixa_de_lembrete(a):
    print("TENTANDO MOSTRAR LEMBRETE")

    app2 = QApplication([])

    global lembrete
    lembrete = uic.loadUi("lembrete.ui")
    lembrete.label_2.setText(a)

    lembrete.show()

    app2.exec()


def aparecer_help(a):
    janela.label.setVisible(True)


#
def desaparecer_help(a):
    janela.label.setVisible(False)


def update_display(text):
    comandos = main.receber_lista_comandos_atualizada()
    if "/" in text:
        janela.listWidget.setVisible(True)
        text = text.replace("/", "")

        comandos_filtro = []

        for widget in comandos:
            if text.lower() in widget.lower():
                comandos_filtro.append(widget)

        janela.listWidget.clear()
        for i in comandos_filtro:
            janela.listWidget.insertItem(2, i)

    else:
        janela.listWidget.setVisible(False)


index_timeline = 0


def timeline(event):
    global index_timeline

    if event.key() == 16777235:
        try:
            if index_timeline >= (len(timeline_de_comandos) - 1) * -1:
                index_timeline -= 1

            janela.lineEdit.setText(timeline_de_comandos[index_timeline])

        except:
            pass

    elif event.key() == 16777237:
        try:
            if index_timeline < -1:
                index_timeline += 1
                janela.lineEdit.setText(timeline_de_comandos[index_timeline])

            else:
                janela.lineEdit.setText("")
                index_timeline = 0

        except:
            pass


if __name__ == "__main__":
    app = QApplication([])
    janela = uic.loadUi("untitled.ui")
    lembrete = uic.loadUi("lembrete.ui")
    rotina = uic.loadUi("rotina.ui")

    grafico = uic.loadUi("graficos.ui")


    static_canvas = FigureCanvas(Figure(figsize=(7, 3)))
    static_canvas2 = FigureCanvas(Figure(figsize=(7, 3)))



    modelo = QStandardItemModel(12, 1)

    comandos = main.receber_lista_comandos_atualizada()

    janela.listWidget.clicked.connect(clicked)

    janela.lineEdit.textChanged.connect(update_display)
    janela.lineEdit.returnPressed.connect(clicked_by_enter)
    janela.pushButton.clicked.connect(clicked_on_microphone)
    janela.pushButton_3.clicked.connect(aparecer_help)
    janela.keyPressEvent = timeline
    janela.pushButton_3.enterEvent = aparecer_help
    janela.pushButton_3.leaveEvent = desaparecer_help

    # janela.pushButton.setIcon(QIcon('logo.png'))

    janela.listWidget.setVisible(False)
    janela.label.setVisible(False)

    janela.show()
    # print(aparecer_graficos("acao1", "retorno", [1, 2, 3], [1, 2, 3],
    #                   dois_graficos=False, title2=None, ylabel2=None, primeiro_arg2=None, segundo_arg2=None,
    #                   barra=False))

    # keyboard.add_hotkey('ctrl + shift + z', clicked_on_microphone)
    app.exec()


grafico = uic.loadUi("graficos.ui")
