from .app import App
from PySide6 import QtWidgets
import sys


def launch_app():
    app = QtWidgets.QApplication([])
    editor = App()
    editor.show()
    sys.exit(app.exec())
