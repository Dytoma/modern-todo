from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget
from components.topbar import TopBar
from styles.colors import Colors
from PyQt5.QtCore import Qt


class TaskBar(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet(f"background-color: {Colors.GRAY};")
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 28, 20)
        self.layout.setSpacing(40)

        self.top_bar = TopBar()

        self.layout.addWidget(self.top_bar)

