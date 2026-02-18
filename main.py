from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt, QSize
from layouts.taskbar import TaskBar
from layouts.workspace import Workspace
from layouts.task_form import TaskForm

# import os
#
# os.environ["QT_QPA_PLATFORM"] = 'wayland'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Modern Todo App")
        self.main_layout = QHBoxLayout()
        self.task_bar = TaskBar()
        self.workspace = Workspace()
        self.task_form = TaskForm()

        self.main_layout.addWidget(self.task_bar, 20)
        self.main_layout.addWidget(self.workspace, 50)
        self.main_layout.addWidget(self.task_form, 30)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        container = QWidget()
        container.setLayout(self.main_layout)

        self.setMinimumSize(QSize(1280, 832))
        self.setCentralWidget(container)


def main():
    app = QApplication([])
    window = MainWindow()

    window.show()
    app.exec()

if __name__ == '__main__':
    main()
