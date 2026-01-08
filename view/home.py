from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QFileDialog, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, pyqtSignal

class Home(QWidget):
    to_dvr = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #2f1188; color: white;')
        self.setMinimumSize(1000, 700)
        self.setWindowTitle('DVR')
        self.load_button = QPushButton("Seleziona cartella")
        self.load_button.clicked.connect(self.load_video)
        self.load_button.setFixedHeight(100)
        self.load_button.setFixedWidth(400)
        self.load_button.setStyleSheet('''
            QPushButton {
                background-color: #1e0c53; 
                border-radius: 8px; 
                border: 1px solid white;
                font-size: 50px;
            }
            QPushButton:hover {
                background-color: #2f1188;
            }       
        ''')
        self.load_button.setCursor(Qt.PointingHandCursor)
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.load_button)

    def load_video(self):
        self.directory = QFileDialog.getExistingDirectory(self, "Selezionare una cartella")
        self.to_dvr.emit()

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    app.setApplicationName("File Video")
    window = Home()
    window.show()
    app.exec_()