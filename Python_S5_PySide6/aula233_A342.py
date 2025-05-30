# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec

import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout
# from Pyside6.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout
app = QApplication(sys.argv)

botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 80px;')

botao2 = QPushButton('Botão2')
botao2.setStyleSheet('font-size: 40px;')

botao3 = QPushButton('Botão2')
botao3.setStyleSheet('font-size: 40px;')

central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1, 1)
layout.addWidget(botao2, 2, 1)
layout.addWidget(botao3, 3, 1)

# Central widget entre na hierarquia e mostre sua janela
central_widget.show()
app.exec()    # O loop da aplicação
