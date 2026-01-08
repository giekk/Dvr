from view.file_video_panel import FileVideoPanel
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QScrollArea, QFrame, QLineEdit, QHBoxLayout, QLabel, QSizePolicy
from PyQt5.QtCore import Qt, pyqtSignal
from dvr import DVR
from view.menu import Menu
from player import Player

class DvrView(QWidget):
    show_home = pyqtSignal()
    def __init__(self, directory):
        super().__init__()
        self.dvr = DVR(directory)
        self.player = Player(directory)
        self.menu = Menu(self.dvr.libraries)
        self.file_video_panels = []
        self.current_playing_panel = None
        self.initUI()
    
    def initUI(self):
        self.setStyleSheet('background-color: #2f1188; color: white;')
        self.setMinimumSize(1400, 1000)
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter | Qt.AlignLeft)

        main_layout = QHBoxLayout()
        main_layout.setAlignment(Qt.AlignLeft)

        directory_label = QLabel(f'Percorso Cartella: {self.dvr.directory}')

        self.no_video_label = QLabel('Nessun video trovato')
        self.no_video_label.setAlignment(Qt.AlignCenter)
        self.no_video_label.setStyleSheet('color: #2f1188; font-size: 50px;')

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText('Cerca...')
        self.search_bar.setFixedHeight(40)
        self.search_bar.setFixedWidth(600)
        self.search_bar.setStyleSheet(
            ' background-color: #1e0c53; '
            ' border-radius: 8px; '
            ' color: white; '
            ' border: 1px solid white; '
        )

        self.total_label = QLabel()

        scroll_area = QScrollArea(self)
        self.set_scroll_area(scroll_area)

        self.container = QWidget()
        self.container.setStyleSheet(' background-color: #1e0c53; ')
        self.container_layout = QVBoxLayout(self.container)
        self.container_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        total = 0
        for video in self.dvr.videos:
            panel = FileVideoPanel(video)
            panel.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
            self.file_video_panels.append(panel)
            self.container_layout.addWidget(panel)
            panel.riproduction.connect(self.riproduction)
            total += 1

        self.no_video_label.hide()
        if total == 0: 
            self.container_layout.addWidget(self.no_video_label)
            self.no_video_label.show()

        self.total_label.setText(f"Totale: {total}")
        
        self.container.setLayout(self.container_layout)
        scroll_area.setWidget(self.container)

        self.search_bar.textChanged.connect(self.update_display)
        self.menu.change_category.connect(self.update_display_by_category)
        self.menu.to_home.connect(self.show_home)

        main_layout.addWidget(self.menu)
        main_layout.addWidget(scroll_area)

        layout.addWidget(self.search_bar)
        layout.addWidget(self.total_label)
        layout.addLayout(main_layout)
        layout.addWidget(directory_label)

    def set_scroll_area(self, scroll_area):
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.NoFrame)

    def update_display(self):
        for i in reversed(range(self.container_layout.count())):
            widget = self.container_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        search_text = self.search_bar.text().lower()

        count = 0
        for panel in self.file_video_panels:
            if search_text in panel.file_video.name.lower():
                self.container_layout.addWidget(panel)
                count += 1
        
        self.total_label.setText(f"Totale: {count}")
        if count == 0:
            self.container_layout.addWidget(self.no_video_label)
            self.no_video_label.show()
        else:
            self.container_layout.removeWidget(self.no_video_label)
            self.no_video_label.hide()

    def update_display_by_category(self, category):
        for i in reversed(range(self.container_layout.count())):
            widget = self.container_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        count = 0
        if category == "Tutti":
            for panel in self.file_video_panels:
                self.container_layout.addWidget(panel)
                count += 1
        else:
            category_lower = category.lower()

            for panel in self.file_video_panels:
                if category_lower in panel.file_video.name.lower():
                    self.container_layout.addWidget(panel)
                    count += 1
        
        self.total_label.setText(f"Totale: {count}")
        if count == 0:
            self.container_layout.addWidget(self.no_video_label)
            self.no_video_label.show()
        else:
            self.container_layout.removeWidget(self.no_video_label)
            self.no_video_label.hide()

    def riproduction(self, panel):
        if self.current_playing_panel and self.current_playing_panel != panel:
            self.current_playing_panel.stop()
            print(f'{self.current_playing_panel.file_video.name} is stopping: {self.current_playing_panel.is_playing}')
        self.current_playing_panel = panel if panel.is_playing else None
        print(f'{panel.file_video.name} is playing: {panel.is_playing}')
        if panel.is_playing:
            if self.player.playing:
                self.player.update_video(panel.file_video.name)
                self.player.stopped.connect(panel.stop)
            else: 
                self.player.play_video(panel.file_video.name)
                self.player.stopped.connect(panel.stop)




        