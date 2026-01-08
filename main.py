from PyQt5.QtWidgets import QApplication
from mainwindow import MainWindow

def main():
    app = QApplication([])
    app.setApplicationName("DVR")
    
    window = MainWindow()

    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
