from .app import App
from .style import style
from PySide6 import QtWidgets
import sys


def launch_app():
    app = QtWidgets.QApplication([])
    app.setStyleSheet(style)
    editor = App()
    editor.show()
    sys.exit(app.exec())
