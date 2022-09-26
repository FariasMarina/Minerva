from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from Minerva import main


app =  QApplication([])
janela = uic.loadUi("microfone.ui")
janela.pushButton.clicked.connect(main.run_minerva)

janela.show()

app.exec()

#usar teste_geral no mesmo diretorio
