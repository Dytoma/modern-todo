from PyQt5.QtWidgets import QHBoxLayout, QLabel, QWidget
from styles.colors import Colors
from PyQt5.QtCore import Qt


class TopBar(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout(self)
        self.setStyleSheet(f"padding: Opx 24px 0px 24px; border-radius: 12px;")
        self.title = QLabel("Menu")

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(145)

        self.layout.addWidget(self.title)
