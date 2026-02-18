from PyQt5.QtWidgets import QWidget, QVBoxLayout


class Workspace(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)