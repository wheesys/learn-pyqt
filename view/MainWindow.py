import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QAction


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(300, 220)
        self.center()

        self.statusBar().showMessage("un login")

        self.setWindowTitle("OneDrive")
        self.setWindowIcon(QIcon('OneDrive.png'))

        exit_action = QAction(QIcon('OneDrive.png'), '&Exit', self)
        exit_action.setShortcut('Super+Q')
        exit_action.setStatusTip('Exit OneDrive')
        exit_action.triggered().connect(QApplication.quit)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(exit_action)

        # close_btn = QPushButton('close', self)
        # close_btn.resize(close_btn.sizeHint())
        # close_btn.move(self.width()/2, self.height()/2)
        # close_btn.clicked.connect(QCoreApplication.instance().quit)

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

