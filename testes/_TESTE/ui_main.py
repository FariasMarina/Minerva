from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QIcon
import testes._TESTE.main as main


def clicked():
    a = janela.listWidget.currentItem()

    if "*" in a.text():
        janela.lineEdit.setText(a.text().replace("*", ""))
    else:
        janela.label_2.setText(main.run_minerva(input_texto=a.text().replace("@", "").replace("/", "")))
        janela.lineEdit.setText("")


def clicked_by_enter():
    a = janela.lineEdit.text()
    janela.label_2.setText(main.run_minerva(input_texto=a.replace("@", "").replace("/", "")))
    janela.lineEdit.setText("")


def clicked_on_microphone():
    print(main.run_minerva(input_microfone=True))


def caixa_de_lembrete(a):

    app2 = QApplication([])

    lembrete = uic.loadUi("lembrete.ui")
    lembrete.label_2.setText(a)

    lembrete.show()

    app2.exec()



def update_display(text):

    if "/" in text:
        janela.listWidget.setVisible(True)
        text = text.replace("/", "")

        comandos = main.receber_lista_comandos_atualizada()

        comandos_filtro = []


        for widget in comandos:
            if text.lower() in widget.lower():

                comandos_filtro.append(widget)


        janela.listWidget.clear()
        for i in comandos_filtro:
            janela.listWidget.insertItem(2, i)

    else:
        janela.listWidget.setVisible(False)


if __name__ == "__main__":
    app = QApplication([])
    janela = uic.loadUi("untitled.ui")
    lembrete = uic.loadUi("lembrete.ui")


    modelo = QStandardItemModel(12,1)

    comandos = main.receber_lista_comandos_atualizada()


    janela.listWidget.clicked.connect(clicked)



    janela.lineEdit.textChanged.connect(update_display)
    janela.lineEdit.returnPressed.connect(clicked_by_enter)
    janela.pushButton.clicked.connect(caixa_de_lembrete)

    # janela.pushButton.setIcon(QIcon('logo.png'))

    janela.listWidget.setVisible(False)

    janela.show()


    app.exec()