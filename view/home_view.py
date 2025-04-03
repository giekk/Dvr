from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QFileDialog, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, pyqtSignal

from assets.constants import HOME_WIDTH, HOME_HEIGHT, LOAD_BUTTON_WIDTH, LOAD_BUTTON_HEIGHT

class HomeView(QWidget):
    to_dvr = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #2f1188; color: white;')
        self.setMinimumSize(HOME_WIDTH, HOME_HEIGHT)
        self.setWindowTitle('DVR')
        self.load_button = QPushButton("Seleziona cartella")
        self.load_button.clicked.connect(self.load_video)
        self.load_button.setFixedHeight(LOAD_BUTTON_HEIGHT)
        self.load_button.setFixedWidth(LOAD_BUTTON_WIDTH)
        self.load_button.setStyleSheet('''
            QPushButton {
                background-color: #1e0c53; 
                border-radius: 8px; 
                border: 1px solid white;
                font-size: 20px;
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
