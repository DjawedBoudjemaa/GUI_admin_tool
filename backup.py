import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class backupConfig(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(250, 250, 800, 600)
        self.setWindowTitle("Backup Configuration")
        # self.setWindowIcon(QIcon('icons/admin-tool3.png'))
        self.setFixedSize(self.size())

        self.UI()
        self.show()

    def UI(self):
        pass

def main():
    App = QApplication(sys.argv)
    window = backupConfig()
    sys.exit(App.exec_())
