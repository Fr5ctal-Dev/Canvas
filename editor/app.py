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
        self.tab_view.setMovable(True)
        self.tab_view.setTabsClosable(True)
        self.tab_view.setUsesScrollButtons(True)
        self.tab_view.setDocumentMode(True)
        self.tab_view.tabCloseRequested.connect(self.delete_tab)

        self.tab_view.addTab(ScriptEditor(), 'Python')

        self.new_tab_button = QtWidgets.QPushButton('New Tab')
        self.new_tab_button.clicked.connect(lambda: self.add_tab(ScriptEditor(), 'Python'))

        self.main_layout.addWidget(self.new_tab_button)
        self.main_layout.addWidget(self.tab_view)

    def add_tab(self, editor, name):
        tab = self.tab_view.addTab(editor, name)
        self.tab_view.setCurrentIndex(tab)

    def delete_tab(self, index):
        self.tab_view.widget(index).on_close()
        self.tab_view.removeTab(index)

    def closeEvent(self, event):
        for i in range(self.tab_view.count()):
            self.delete_tab(0)
        return super().closeEvent(event)
