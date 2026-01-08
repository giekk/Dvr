from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from mainwindow import MainWindow
import sys

def main():
    # app = QApplication([])

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)

    app.setApplicationName("DVR")
    
    window = MainWindow()

    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
