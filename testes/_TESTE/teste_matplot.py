from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.backends.backend_qtagg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QHeaderView
import numpy as np
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from datetime import date

app = QApplication([])
grafico = uic.loadUi("graficos.ui")

layout = QtWidgets.QVBoxLayout(grafico.tab)

static_canvas = FigureCanvas(Figure(figsize=(7, 3)))
static_canvas2 = FigureCanvas(Figure(figsize=(7, 3)))

# layout.addWidget(static_canvas, janela)) #adicionando navegaçao
layout.addWidget(static_canvas) #adicionando tabela
layout.addWidget(static_canvas2) #adicionando tabela

t = [0, 2, 4]
x = [1, 3, 5]

grafico._static_ax = static_canvas.figure.subplots()

grafico._static_ax.set_title("A")
grafico._static_ax.set_ylabel("A")
grafico._static_ax.barh(t, t)


grafico._static_ax2 = static_canvas2.figure.subplots()
grafico._static_ax2.plot(t, t, color="b")





df = pd.DataFrame([[1,2,3],[3,4,5]], \
       columns=('first', 'second', 'third'), \
       index=('alpha', 'beta'))

# df = pandas
columns = [df.index.name] + [i for i in df.columns]
rows = [[i for i in row] for row in df.itertuples()]
print(columns, rows)




grafico.tableWidget.setRowCount(len(rows)+1)
grafico.tableWidget.setColumnCount(len(columns))

grafico.tableWidget.setHorizontalHeaderLabels(columns)



count = 1
for i in rows:
    count2 = 0
    for j in i:
        grafico.tableWidget.setItem(count, count2,  QTableWidgetItem(f"{j}"))
        count2 += 1
    count += 1

grafico.tableWidget.horizontalHeader().setStretchLastSection(True)
grafico.tableWidget.horizontalHeader().setSectionResizeMode(
    QHeaderView.Stretch)

layout.static_canvas.deleteLater()

grafico.show()

app.exec()