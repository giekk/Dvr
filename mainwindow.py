from PyQt5.QtWidgets import QVBoxLayout, QWidget, QMainWindow, QToolBar, QLabel
from PyQt5.QtGui import QIcon, QColor, QWindow
from PyQt5.QtCore import Qt
from view.home_view import HomeView
from view.dvr_view import DvrView
import ctypes

from assets.constants import Constants

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.home = HomeView()
        self.dvr_view = None
        self.initUI()

    def initUI(self):
        self.setMinimumSize(Constants.HOME_VIEW_WIDTH, Constants.HOME_VIEW_HEIGHT)
        self.setWindowTitle("DVR")
        self.setWindowIcon(QIcon('icons/dvr-icon.ico'))
        self.setStyleSheet("QMainWindow { background: #2f1188; }")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.home)
        self.home.to_dvr.connect(self.show_dvr_view)

    def hide_current_view(self):
        if self.home.isVisible():
            self.home.hide()
            self.layout.removeWidget(self.home)
        if self.dvr_view and self.dvr_view.isVisible():
            self.dvr_view.hide()
            self.layout.removeWidget(self.dvr_view)

    def show_dvr_view(self):
        self.hide_current_view()
        if not self.dvr_view:
            self.dvr_view = DvrView(self.home.directory)
        self.layout.addWidget(self.dvr_view)
        self.setMinimumSize(Constants.DVR_VIEW_WIDTH, Constants.DVR_VIEW_HEIGHT)
        self.dvr_view.show()
        self.dvr_view.show_home.connect(self.show_home_view)

    def show_home_view(self):
        self.hide_current_view()
        self.layout.addWidget(self.home)
        self.home.show()
        self.home.to_dvr.connect(self.show_dvr_view)
        if self.dvr_view:
            self.dvr_view.deleteLater()
            self.dvr_view = None
