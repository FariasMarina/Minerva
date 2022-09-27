from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from src import main

def click():
    return

app = QApplication([])
janela = uic.loadUi("untitled.ui")
janela.pushButton.clicked.connect(main.run_minerva)

janela.show()

app.exec()

#pro teste: adc pushButton_microfone