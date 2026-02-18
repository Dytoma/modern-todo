from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt, QSize

# import os
#
# os.environ["QT_QPA_PLATFORM"] = 'wayland'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Modern Todo App")
        self.main_layout = QHBoxLayout()

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
