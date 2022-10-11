from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QEvent
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QIcon
import testes._TESTE.main as main



timeline_de_comandos = []

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

    app2 = QApplication([])

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

index_timeline = 0

def timeline(event):
    global index_timeline

    if event.key() == 16777235:
        try:
            if index_timeline >= (len(timeline_de_comandos)-1) * -1:
                index_timeline -= 1

            janela.lineEdit.setText(timeline_de_comandos[index_timeline])

        except: pass

    elif event.key() == 16777237:
        try:
            if index_timeline < -1:
                index_timeline += 1
                janela.lineEdit.setText(timeline_de_comandos[index_timeline])

            else:
                janela.lineEdit.setText("")
                index_timeline = 0

        except: pass


if __name__ == "__main__":
    app = QApplication([])
    janela = uic.loadUi("untitled.ui")
    lembrete = uic.loadUi("lembrete.ui")


    modelo = QStandardItemModel(12,1)

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


    app.exec()



