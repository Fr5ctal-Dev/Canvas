from .base_editor import BaseEditor
from ..widgets.script import ScriptEditorWidget
from ..widgets.line_numbers import LineNumberWidget
from PySide6 import QtWidgets
from pathlib import Path
import tempfile


class ScriptEditor(BaseEditor):
    def __init__(self):
        super().__init__()
        self.directory = tempfile.TemporaryDirectory()

        self.directory_path = Path(self.directory.name)
        self.script_path = self.directory_path / 'main.py'

        with open(self.script_path, 'w') as f:
            f.write('')

        self.main_layout = QtWidgets.QHBoxLayout(self)

        self.script_editor = ScriptEditorWidget(self.script_path, self.directory_path)
        self.line_numbers = LineNumberWidget(self.script_editor)

        self.main_layout.addWidget(self.line_numbers)
        self.main_layout.addWidget(self.script_editor)

    def on_close(self):
        super().on_close()

        self.script_editor.update_timer.stop()
        self.script_editor.update_timer.deleteLater()

        if self.script_editor.completion_worker is not None:
            self.script_editor.completion_worker_thread.quit()
            self.script_editor.completion_worker_thread.wait()
            self.script_editor.completion_worker_thread.deleteLater()
            self.script_editor.completion_worker = None
            self.script_editor.completion_worker_thread = None

        self.directory.cleanup()
