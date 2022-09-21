from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import teste_geral


app =  QApplication([])
janela = uic.loadUi("microfone.ui")
janela.pushButton.clicked.connect(teste_geral.run_minerva())

janela.show()

app.exec()
