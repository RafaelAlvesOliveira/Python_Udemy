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

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QWidget)


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Configuração básica da janela
        self.setWindowTitle('Minha janela')  # Use self, não self.window
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)  # Use self, não self.window

        # Botões
        self.botao1 = self.make_button('Texto do botão')
        self.botao1.clicked.connect(self.segunda_acao_marcada)

        self.botao2 = self.make_button('Botao 2')

        self.botao3 = self.make_button('Terceiro')

        # self.botao2 = QPushButton('Botão2')
        # self.botao2.setStyleSheet('font-size: 40px;')

        # self.botao3 = QPushButton('Botão3')  # Corrigi o texto para Botão3
        # self.botao3.setStyleSheet('font-size: 40px;')

        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.botao1, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.botao2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.botao3, 3, 1, 1, 2)

        # statusBar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Mostrar mensagem na barra')

        # menuBar
        self.menu = self.menuBar()
        self.primeiro_menu = self.menu.addMenu('Primeiro menu')
        self.primeira_acao = self.primeiro_menu.addAction('Primeira ação')
        self.primeira_acao.triggered.connect(self.muda_mensagem_da_status_bar)

        self.segunda_action = self.primeiro_menu.addAction('Segunda ação')
        self.segunda_action.setCheckable(True)
        self.segunda_action.toggled.connect(self.segunda_acao_marcada)
        self.segunda_action.hovered.connect(self.segunda_acao_marcada)

    @Slot()
    def muda_mensagem_da_status_bar(self):
        self.status_bar.showMessage('O meu slot foi executado')

    @Slot()
    def segunda_acao_marcada(self):
        print('Está marcado?', self.segunda_action.isChecked())

    def make_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet('font-size: 80px;')
        return btn


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()  # O loop da aplicação
