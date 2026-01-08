from abc import ABC, abstractmethod

from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class Visitor(ABC):

    @abstractmethod
    def visitAVI(self, avi):
        pass
    @abstractmethod
    def visitMP4(self, mp4):
        pass
    @abstractmethod
    def visitMKV(self, mkv):
        pass

    @abstractmethod
    def visitVOB(self, vob):
        pass

class IconVisitor(Visitor):
    
    def __init__(self):
        self.icon = QLabel()

    def visitAVI(self, avi):
        avi.img_path = "icons/avi-icon.png"
        self.icon.setPixmap(QPixmap(avi.img_path).scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation))
    
    def visitMP4(self, mp4):
        mp4.img_path = "icons/mp4-icon.png"
        self.icon.setPixmap(QPixmap(mp4.img_path).scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation))
    
    def visitMKV(self, mkv):
        mkv.img_path = "icons/mkv-icon.png"
        self.icon.setPixmap(QPixmap(mkv.img_path).scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation))   
    def visitVOB(self, vob):
        vob.img_path = "icons/vob-icon.png"
        self.icon.setPixmap(QPixmap(vob.img_path).scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation))