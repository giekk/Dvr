from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap

from assets.constants import Constants  

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
    def visitMOV(self, mov):
        pass
    @abstractmethod
    def visitVOB(self, vob):
        pass

class IconVisitor(Visitor):
    def __init__(self):
        self.icon = QLabel()

    def visitAVI(self, avi):
        avi.img_path = "icons/avi-icon.png"
        self.icon.setPixmap(QPixmap(avi.img_path).scaled(Constants.FILE_AUDIO_IMG_WIDTH, Constants.FILE_AUDIO_IMG_HEIGHT))
    
    def visitMP4(self, mp4):
        mp4.img_path = "icons/mp4-icon.png"
        self.icon.setPixmap(QPixmap(mp4.img_path).scaled(Constants.FILE_AUDIO_IMG_WIDTH, Constants.FILE_AUDIO_IMG_HEIGHT))
    
    def visitMKV(self, mkv):
        mkv.img_path = "icons/mkv-icon.png"
        self.icon.setPixmap(QPixmap(mkv.img_path).scaled(Constants.FILE_AUDIO_IMG_WIDTH, Constants.FILE_AUDIO_IMG_HEIGHT))

    def visitMOV(self, mov):
        mov.img_path = "icons/mov-icon.png"
        self.icon.setPixmap(QPixmap(mov.img_path).scaled(Constants.FILE_AUDIO_IMG_WIDTH, Constants.FILE_AUDIO_IMG_HEIGHT))

    def visitVOB(self, vob):
        vob.img_path = "icons/vob-icon.png"
        self.icon.setPixmap(QPixmap(vob.img_path).scaled(Constants.FILE_AUDIO_IMG_WIDTH, Constants.FILE_AUDIO_IMG_HEIGHT))