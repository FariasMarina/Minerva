from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import main

def click():
    return main.run_minerva

app = QApplication([])
janela = uic.loadUi("microfone_main.ui")
janela.pushButton_microfone.clicked.connect(click)

janela.show()

app.exec()

#pro teste: adc pushButton_microfone