from PyQt5.QtWidgets import QWidget, QVBoxLayout

class TaskForm(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)
