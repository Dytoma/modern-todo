from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout

class TaskBar(QVBoxLayout):
    def __init__(self):
        super().__init__()

        self.setContentsMargins(0, 40, 0, 40)
        self.setSpacing(0)

        self.top_bar = QHBoxLayout()
        self.top_bar.setContentsMargins(0, 0, 0, 0)
        self.top_bar.setSpacing(0)

        self.addLayout(self.top_bar)
