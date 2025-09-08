from .editors.script import ScriptEditor
from PySide6 import QtWidgets, QtCore


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Canvas')
        self.setMinimumSize(QtCore.QSize(700, 500))

        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QVBoxLayout(self.main_widget)
        self.setCentralWidget(self.main_widget)

        self.tab_view = QtWidgets.QTabWidget()
        self.main_layout.addWidget(self.tab_view)
        self.tab_view.setMovable(True)
        self.tab_view.setTabsClosable(True)
        self.tab_view.setUsesScrollButtons(True)
        self.tab_view.setDocumentMode(True)
        self.tab_view.tabCloseRequested.connect(self.delete_tab)

        # TEST #
        self.add_tab(ScriptEditor(), 'hello')

    def add_tab(self, editor, name):
        tab = self.tab_view.addTab(editor, name)
        self.tab_view.setCurrentIndex(tab)

    def delete_tab(self, index):
        self.tab_view.widget(index).on_close()
        self.tab_view.removeTab(index)

    def closeEvent(self, event):
        for index in range(self.tab_view.count()):
            self.delete_tab(index)
        return super().closeEvent(event)
