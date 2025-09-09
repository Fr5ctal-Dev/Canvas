style = '''
QWidget {
    background-color: #282c34;
    color: #abb2bf;
    border: none;
}

QMainWindow {
    background-color: #282c34;
}

QToolTip {
    background-color: #2c313a;
    color: #abb2bf;
    border: 1px solid #4b5263;
    padding: 4px;
    border-radius: 3px;
    opacity: 230;
}

QDockWidget {
    color: #abb2bf;
    border: 1px solid #282c34;
    font-weight: bold;
}

QDockWidget::title {
    background-color: #2c313a;
    padding: 6px;
    border-radius: 4px 4px 0 0;
}

QDockWidget::close-button,
QDockWidget::float-button {
    background-color: transparent;
    border-radius: 2px;
    padding: 4px;
}

QDockWidget::close-button:hover,
QDockWidget::float-button:hover {
    background-color: #3e4451;
}

QDockWidget::close-button:pressed,
QDockWidget::float-button:pressed {
    background-color: #4b5263;
}

QMenuBar {
    background-color: #2c313a;
    padding: 4px;
    spacing: 10px;
}

QMenuBar::item {
    color: #abb2bf;
    background-color: transparent;
    padding: 4px 8px;
    border-radius: 3px;
}

QMenuBar::item:selected {
    background-color: #3e4451;
}

QMenuBar::item:pressed {
    background-color: #61afef;
    color: #ffffff;
}

QMenu {
    background-color: #2c313a;
    border: 1px solid #4b5263;
    padding: 5px;
}

QMenu::item {
    color: #abb2bf;
    padding: 4px 20px 4px 20px;
    border-radius: 3px;
}

QMenu::item:selected {
    background-color: #61afef;
    color: #ffffff;
}

QMenu::item:disabled {
    color: #5c6370;
    background-color: transparent;
}

QMenu::separator {
    height: 1px;
    background-color: #4b5263;
    margin: 4px 0px;
}

QPushButton {
    background-color: #3e4451;
    color: #abb2bf;
    border-radius: 4px;
    padding: 6px 12px;
    min-height: 1.5em;
}

QPushButton:hover {
    background-color: #4b5263;
}

QPushButton:pressed {
    background-color: #61afef;
    color: #ffffff;
}

QPushButton:checked {
    background-color: #61afef;
    border: 1px solid #61afef;
}

QPushButton:disabled {
    background-color: #2c313a;
    color: #5c6370;
}

QPushButton[primary="true"] {
    background-color: #61afef;
    color: #ffffff;
    font-weight: bold;
}
QPushButton[primary="true"]:hover {
    background-color: #7abfff;
}
QPushButton[primary="true"]:pressed {
    background-color: #4f9de8;
}

QLineEdit, QSpinBox, QDoubleSpinBox, QComboBox {
    background-color: #2c313a;
    color: #abb2bf;
    border: 1px solid #4b5263;
    border-radius: 4px;
    padding: 5px;
    selection-background-color: #3e4451;
    selection-color: #ffffff;
}

QLineEdit:focus, QSpinBox:focus, QDoubleSpinBox:focus, QComboBox:focus {
    border: 1px solid #61afef;
    outline: none;
}

QLineEdit:disabled, QSpinBox:disabled, QDoubleSpinBox:disabled, QComboBox:disabled {
    background-color: #282c34;
    color: #5c6370;
    border-color: #3e4451;
}

QSpinBox::up-button, QDoubleSpinBox::up-button,
QSpinBox::down-button, QDoubleSpinBox::down-button {
    subcontrol-origin: border;
    background-color: #3e4451;
    width: 16px;
    border-radius: 2px;
}

QSpinBox::up-button:hover, QDoubleSpinBox::up-button:hover,
QSpinBox::down-button:hover, QDoubleSpinBox::down-button:hover {
    background-color: #4b5263;
}

QSpinBox::up-arrow, QDoubleSpinBox::up-arrow {
    image: url(icons/arrow_up_light.png);
    width: 10px;
    height: 10px;
}

QSpinBox::down-arrow, QDoubleSpinBox::down-arrow {
    image: url(icons/arrow_down_light.png);
    width: 10px;
    height: 10px;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 20px;
    border-left: 1px solid #4b5263;
    border-radius: 0 4px 4px 0;
}

QComboBox::down-arrow {
    image: url(icons/arrow_down_light.png);
}

QComboBox QAbstractItemView {
    background-color: #2c313a;
    border: 1px solid #4b5263;
    selection-background-color: #3e4451;
    padding: 4px;
}

QCheckBox, QRadioButton {
    spacing: 8px;
    color: #abb2bf;
}

QCheckBox::indicator, QRadioButton::indicator {
    width: 16px;
    height: 16px;
    border-radius: 3px;
    background-color: #2c313a;
    border: 1px solid #4b5263;
}

QRadioButton::indicator {
    border-radius: 9px;
}

QCheckBox::indicator:checked, QRadioButton::indicator:checked {
    background-color: #61afef;
    border-color: #61afef;
}

QRadioButton::indicator:checked {
    background-color: #61afef;
    image: url(icons/radio_dot.png);
}

QCheckBox::indicator:hover, QRadioButton::indicator:hover {
    border-color: #61afef;
}

QCheckBox:disabled, QRadioButton:disabled {
    color: #5c6370;
}

QSlider::groove:horizontal {
    border: 1px solid #282c34;
    height: 4px;
    background-color: #4b5263;
    margin: 2px 0;
    border-radius: 2px;
}

QSlider::handle:horizontal {
    background-color: #61afef;
    border: 1px solid #61afef;
    width: 14px;
    height: 14px;
    margin: -5px 0;
    border-radius: 7px;
}

QSlider::handle:horizontal:hover {
    background-color: #7abfff;
    border-color: #7abfff;
}

QSlider::handle:horizontal:pressed {
    background-color: #4f9de8;
    border-color: #4f9de8;
}

QTabWidget::pane {
    border-top: 1px solid #4b5263;
    padding: 10px;
}

QTabBar::tab {
    background-color: #2c313a;
    color: #abb2bf;
    padding: 8px 16px;
    margin-right: 2px;
    border: 1px solid #2c313a;
    border-bottom: none;
    border-radius: 4px 4px 0 0;
}

QTabBar::tab:hover {
    background-color: #3e4451;
}

QTabBar::tab:selected {
    background-color: #282c34;
    color: #ffffff;
    border-color: #4b5263;
    border-bottom-color: #282c34;
}

QTabBar::tab:disabled {
    background-color: #282c34;
    color: #5c6370;
}

QTreeView, QListView {
    background-color: #2c313a;
    border: 1px solid #4b5263;
    alternate-background-color: #2f343e;
    outline: 0;
}

QTreeView::item, QListView::item {
    padding: 4px;
    min-height: 20px;
    color: #abb2bf;
}

QTreeView::item:hover, QListView::item:hover {
    background-color: #3e4451;
}

QTreeView::item:selected, QListView::item:selected {
    background-color: #61afef;
    color: #ffffff;
}

QTreeView::branch {
    background-color: transparent;
}

QTreeView::branch:closed:has-children:!has-siblings,
QTreeView::branch:closed:has-children:has-siblings {
    image: url(icons/arrow_right_light.png);
}

QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings {
    image: url(icons/arrow_down_light.png);
}

QHeaderView::section {
    background-color: #2c313a;
    color: #abb2bf;
    padding: 6px;
    border: 1px solid #4b5263;
    border-left: none;
    font-weight: bold;
}

QHeaderView::section:hover {
    background-color: #3e4451;
}

QScrollBar:vertical, QScrollBar:horizontal {
    background-color: #282c34;
    width: 12px;
    height: 12px;
    margin: 0px;
    border: none;
}

QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
    background-color: #4b5263;
    min-height: 20px;
    min-width: 20px;
    border-radius: 6px;
}

QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover {
    background-color: #5c6370;
}

QScrollBar::add-line, QScrollBar::sub-line {
    background: none;
    border: none;
    height: 0px;
    width: 0px;
}

QSplitter::handle {
    background-color: #282c34;
    border: none;
}

QSplitter::handle:hover {
    background-color: #3e4451;
}

QSplitter::handle:pressed {
    background-color: #61afef;
}

QStatusBar {
    background-color: #2c313a;
    color: #abb2bf;
    border-top: 1px solid #4b5263;
}

QStatusBar::item {
    border: none;
    margin: 0px;
}

QProgressBar {
    background-color: #2c313a;
    color: #ffffff;
    border: 1px solid #4b5263;
    border-radius: 4px;
    text-align: center;
}

QProgressBar::chunk {
    background-color: #61afef;
    border-radius: 3px;
    margin: 1px;
}
'''