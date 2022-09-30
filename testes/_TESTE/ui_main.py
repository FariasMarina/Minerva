from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItem, QStandardItemModel
import main

def clicked():
    a = janela.listWidget.currentItem()
    print(a.text())
    if "*" in a.text():
        janela.lineEdit.setText(a.text().replace("*", ""))
    else:
        main.run_minerva(input_texto=a.text().replace("@", ""))
        janela.lineEdit.setText("")


def clicked_by_enter():
    a = janela.lineEdit.text()
    main.run_minerva(input_texto=a.replace("@", ""))
    janela.lineEdit.setText("")



def update_display(text):

    comandos = main.receber_lista_comandos_atualizada()

    comandos_filtro = []


    for widget in comandos:
        if text.lower() in widget.lower():

            comandos_filtro.append(widget)


    janela.listWidget.clear()
    for i in comandos_filtro:
        janela.listWidget.insertItem(2, i)




app = QApplication([])
janela = uic.loadUi("untitled.ui")


modelo = QStandardItemModel(12,1)

comandos = main.receber_lista_comandos_atualizada()


janela.listWidget.clicked.connect(clicked)



janela.lineEdit.textChanged.connect(update_display)
janela.lineEdit.returnPressed.connect(clicked_by_enter)



janela.show()

app.exec()