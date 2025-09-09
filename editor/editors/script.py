from .base_editor import BaseEditor
from ..widgets.script import ScriptEditorWidget
from ..widgets.line_numbers import LineNumberWidget
from ..utils import get_resource_path
from PySide6 import QtWidgets, QtCore, QtGui
from pathlib import Path
import tempfile
import subprocess
import shutil


class ScriptEditor(BaseEditor):
    def __init__(self):
        super().__init__()
        self.directory = tempfile.TemporaryDirectory()

        self.directory_path = Path(self.directory.name)
        self.script_path = self.directory_path / 'main.py'

        with open(self.script_path, 'w') as f:
            f.write('')

        self.execution_process = None
        self.execution_timer = QtCore.QTimer()
        self.execution_timer.timeout.connect(self.check_if_execution_has_ended)
        self.execution_timer.start(100)

        self.main_layout = QtWidgets.QHBoxLayout(self)

        self.script_editor = ScriptEditorWidget(self.script_path, self.directory_path)
        self.line_numbers = LineNumberWidget(self.script_editor)

        self.main_layout.addWidget(self.line_numbers)
        self.main_layout.addWidget(self.script_editor)

        self.command_bar = QtWidgets.QWidget()
        self.main_layout.addWidget(self.command_bar)
        self.command_bar_layout = QtWidgets.QVBoxLayout(self.command_bar)

        self.run_button = QtWidgets.QPushButton()
        self.command_bar_layout.addWidget(self.run_button)
        self.run_button.setText('Run')
        self.run_button.setIcon(QtGui.QIcon(get_resource_path('editor/assets/icons/play.svg')))
        self.run_button.clicked.connect(self.run_script)

        self.stop_button = QtWidgets.QPushButton()
        self.command_bar_layout.addWidget(self.stop_button)
        self.stop_button.setText('Stop')
        self.stop_button.setIcon(QtGui.QIcon(get_resource_path('editor/assets/icons/stop.svg')))
        self.stop_button.clicked.connect(self.terminate_execution)

    def run_script(self):
        if self.execution_process is not None:
            return
        self.script_editor.save()
        self.execution_process = subprocess.Popen([shutil.which('python') or shutil.which('python3') or 'python', self.script_path], cwd=self.directory_path)

    def check_if_execution_has_ended(self):
        if self.execution_process is None:
            return
        if self.execution_process.poll() is not None:
            self.execution_process.wait()
            self.execution_process = None

    def terminate_execution(self):
        if self.execution_process is None:
            return
        self.execution_process.terminate()
        self.execution_process.wait()

    def on_close(self):
        super().on_close()

        self.execution_timer.stop()
        self.terminate_execution()

        self.script_editor.update_timer.stop()
        self.script_editor.update_timer.deleteLater()

        if self.script_editor.completion_worker_thread is not None:
            self.script_editor.completion_worker_thread.quit()
            self.script_editor.completion_worker_thread.wait()
            self.script_editor.completion_worker_thread.deleteLater()
            self.script_editor.completion_worker = None
            self.script_editor.completion_worker_thread = None

        self.directory.cleanup()
