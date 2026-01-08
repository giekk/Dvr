from PyQt5.QtWidgets import QVBoxLayout, QWidget, QMainWindow, QToolBar, QLabel
from PyQt5.QtGui import QIcon, QColor, QWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWinExtras import QtWin
from view.home import Home
from view.dvr_view import DvrView
import ctypes

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.home = Home()
        self.dvr_view = None
        self.initUI()

    def set_window_title_color(self, hwnd, color):
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        DWMWA_CAPTION_COLOR = 35
        DWMWA_TEXT_COLOR = 36

        # Convert QColor to COLORREF
        colorref = color.red() | (color.green() << 8) | (color.blue() << 16)

        # Set the caption color
        ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, DWMWA_CAPTION_COLOR, ctypes.byref(ctypes.c_int(colorref)), ctypes.sizeof(ctypes.c_int))

        # Set the text color
        ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, DWMWA_TEXT_COLOR, ctypes.byref(ctypes.c_int(colorref)), ctypes.sizeof(ctypes.c_int))
    
    def initUI(self):
        self.setMinimumSize(500, 400)
        self.setWindowTitle("DVR")
        self.setWindowIcon(QIcon('icons/dvr-icon.ico'))
        self.setStyleSheet("QMainWindow { background: #2f1188; }")

        # Imposta il colore della barra del titolo
        if hasattr(QtWin, 'setCurrentProcessExplicitAppUserModelID'):
            QtWin.setCurrentProcessExplicitAppUserModelID('myappid')
        hwnd = int(self.winId())
        self.set_window_title_color(hwnd, QColor(47, 17, 136))

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
        self.setMinimumSize(800, 500)
        self.dvr_view.show()
        self.dvr_view.show_home.connect(self.show_home_view)

    def show_home_view(self):
        self.hide_current_view()
        self.setMinimumSize(500, 400)
        self.layout.addWidget(self.home)
        self.home.show()
        self.home.to_dvr.connect(self.show_dvr_view)
        if self.dvr_view:
            self.dvr_view.deleteLater()
            self.dvr_view = None
