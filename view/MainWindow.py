import sys

from PyQt5.QtCore import QCoreApplication, QPoint
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDesktopWidget, QMainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(300, 220)
        self.center()

        self.setWindowTitle("OneDrive")
        self.setWindowIcon(QIcon('OneDrive.png'))

        close_btn = QPushButton('close', self)
        close_btn.resize(close_btn.sizeHint())
        close_btn.move(self.width()/2, self.height()/2)
        close_btn.clicked.connect(QCoreApplication.instance().quit)

        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit?', "quit will miss sync from server", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        main_window = self.frameGeometry()
        center_point = QApplication.desktop().availableGeometry().center()
        main_window.moveCenter(center_point)
        self.move(main_window.topLeft())


if __name__ == '__main__':
    oneDrive = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(oneDrive.exec_())

