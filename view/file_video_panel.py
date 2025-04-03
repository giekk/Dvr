from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QFrame
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize, pyqtSignal
from file_video import AVI, MP4, MKV
from visitor import IconVisitor

from constants import STANDARD_BUTTON_HEIGHT, STANDARD_BUTTON_WIDTH

class FileVideoPanel(QWidget):
    riproduction = pyqtSignal(object)

    def __init__(self, file_video):
        super().__init__()
        self.file_video = file_video
        self.is_playing = False
        self.initUi()

    def initUi(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignLeft | Qt.AlignCenter)

        main_layout = QHBoxLayout()

        self.play_button = QPushButton('Riproduci')
        self.play_button.setStyleSheet('''
            QPushButton { 
                background-color: #2f1188; 
                border-radius: 8px; 
                border: 1px solid white; 
                color: white;
            }
            QPushButton:hover { 
                background-color: #1e0c53;
            }
        ''')
        self.play_button.setFixedHeight(STANDARD_BUTTON_HEIGHT)
        self.play_button.setFixedWidth(STANDARD_BUTTON_WIDTH)
        self.play_button.setCursor(Qt.PointingHandCursor)
        self.play_button.clicked.connect(self.play)

        visitor = IconVisitor()
        self.file_video.accept(visitor)
        self.icon = visitor.icon
        self.name = QLabel(self.file_video.name)
        self.name.setStyleSheet('font-size: 12px;')

        main_layout.addWidget(self.play_button)
        main_layout.addWidget(self.icon)
        main_layout.addWidget(self.name)
        layout.addLayout(main_layout)

    def play(self):
        if not self.is_playing:
            self.is_playing = True
            self.play_button.setText('In riproduz.')
            self.play_button.setStyleSheet('background-color: #3e1c73; border-radius: 8px; border: 1px solid white;')
            self.riproduction.emit(self)

    def stop(self):
        self.is_playing = False
        self.play_button.setText('Riproduci')
        self.play_button.setStyleSheet('''
            QPushButton { 
                background-color: #2f1188; 
                border-radius: 8px; 
                border: 1px solid white; 
                color: white;
            }
            QPushButton:hover { 
                background-color: #1e0c53;
            }
        ''')