from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from main import run_minerva

def click():
    return "oi"

app = QApplication([])
janela = uic.loadUi("untitled.ui")
janela.pushButton.clicked.connect(run_minerva)

janela.show()

app.exec()

#pro teste: adc pushButton_microfone
