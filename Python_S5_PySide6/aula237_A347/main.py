import sys

from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH

from main_window import MainWindow
from PySide6.QtWidgets import (QApplication, QLabel)


def temp_label(texto):
    label1 = QLabel(texto)
    label1.setStyleSheet('font-size: 150px')
    return label1


if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # label1 = QLabel('O meu texto')
    # label1.setStyleSheet('font-size: 150px')
    # window.addWidgetToVLayout(label1)

    # Executa tuo
    window.adjustFixedSize()
    window.show()
    app.exec()
