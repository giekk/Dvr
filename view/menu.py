from PyQt5.QtWidgets import QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QFrame
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize, pyqtSignal
from view.add_library_dialog import AddLibraryDialog

class Menu(QWidget):
    to_home = pyqtSignal()
    change_category = pyqtSignal(str)
    add_library_to_db = pyqtSignal(str)
    remove_library_from_db = pyqtSignal(str)

    def __init__(self, libraries):
        super().__init__()
        self.selected_menu_button = None
        self.selected_button = None
        self.initUI(libraries)

    def initUI(self, libraries):
        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter | Qt.AlignTop)

        menu_layout = QVBoxLayout()
        menu_layout.setAlignment(Qt.AlignCenter | Qt.AlignTop)

        self.home_button = QPushButton()
        self.home_button.setIcon(QIcon('icons/home-icon.png'))
        self.home_button.setIconSize(QSize(30, 30))
        self.home_button.setStyleSheet(' border: none; ')
        self.home_button.setCursor(Qt.PointingHandCursor)
        self.home_button.setToolTip('Home')
        self.home_button.clicked.connect(self.to_home.emit)

        self.categories_button = QPushButton()
        self.categories_button.setIcon(QIcon('icons/categories-icon.png'))
        self.categories_button.setIconSize(QSize(30, 30))
        self.categories_button.setStyleSheet('border: none;')
        self.categories_button.setCursor(Qt.PointingHandCursor)
        self.categories_button.setToolTip('Categorie')

        self.libraries_button = QPushButton()
        self.libraries_button.setIcon(QIcon('icons/libraries-icon.png'))
        self.libraries_button.setIconSize(QSize(30, 30))
        self.libraries_button.setStyleSheet('border: none;')
        self.libraries_button.setCursor(Qt.PointingHandCursor)
        self.libraries_button.setToolTip('Librerie')

        menu_layout.addWidget(self.home_button)
        menu_layout.addWidget(self.categories_button)
        menu_layout.addWidget(self.libraries_button)

        self.categories_button.clicked.connect(self.show_categories_widget)
        self.libraries_button.clicked.connect(self.show_libraries_widget)

        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.VLine)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setStyleSheet(
            ' background-color: #1e0c53; '
            ' color: #1e0c53;'
            ' height: 1px; '
            ' border: none; '
            ' opacity: 0.5; '
        ) 

        self.categories_widget = self.categories_widget()
        self.libraries_widget = self.libraries_widget(libraries)

        self.layout.addLayout(menu_layout)
        self.layout.addWidget(self.frame)

        self.categories_widget.hide()
        self.libraries_widget.hide()

    def show_categories_widget(self):
        if self.categories_widget.isHidden() and self.libraries_widget.isHidden():
            self.layout.addWidget(self.categories_widget)
            self.categories_widget.show()
        elif self.categories_widget.isHidden() and self.libraries_widget.isVisible():
            self.layout.removeWidget(self.libraries_widget)
            self.libraries_widget.hide()
            self.layout.addWidget(self.categories_widget)
            self.categories_widget.show()
        else:
            self.layout.removeWidget(self.categories_widget)
            self.categories_widget.hide()

    def show_libraries_widget(self):
        if self.libraries_widget.isHidden() and self.categories_widget.isHidden():
            self.layout.addWidget(self.libraries_widget)
            self.libraries_widget.show()
        elif self.libraries_widget.isHidden() and self.categories_widget.isVisible():
            self.layout.removeWidget(self.categories_widget)
            self.categories_widget.hide()
            self.layout.addWidget(self.libraries_widget)
            self.libraries_widget.show()
        else:
            self.layout.removeWidget(self.libraries_widget)
            self.libraries_widget.hide()

    def categories_widget(self):
        categories = QWidget()
        layout = QVBoxLayout(categories)
        layout.setAlignment(Qt.AlignCenter | Qt.AlignTop)

        all_button = QPushButton('Tutti')
        drama_button = QPushButton('Drammatico')
        comedy_button = QPushButton('Commedia')
        action_button = QPushButton('Azione')
        thriller_button = QPushButton('Thriller')
        horror_button = QPushButton('Horror')
        fantasy_button = QPushButton('Fantastico')
        animation_button = QPushButton('Animazione')
        science_fiction_button = QPushButton('Fantascienza')
        romance_button = QPushButton('Romantico')
        adventure_button = QPushButton('Avventura')
        gangster_button = QPushButton('Gangster')
        war_button = QPushButton('Guerra')

        buttons = [
            all_button, drama_button, comedy_button, action_button, thriller_button, horror_button,
            fantasy_button, animation_button, science_fiction_button, romance_button, adventure_button,
            gangster_button, war_button
        ]

        self.button_style(buttons)

        for button in buttons:
            button.clicked.connect(lambda checked, b=button: self.on_button_clicked(b))
            layout.addWidget(button)

        return categories
    
    def libraries_widget(self, libraries):
        libraries_widget = QWidget()
        self.libraries_layout = QVBoxLayout(libraries_widget)
        self.libraries_layout.setAlignment(Qt.AlignCenter | Qt.AlignTop)

        add_library_button = QPushButton()
        add_library_button.setIcon(QIcon('icons/add-icon.png'))
        add_library_button.setStyleSheet('border: none;')
        add_library_button.setCursor(Qt.PointingHandCursor)
        add_library_button.setToolTip('Aggiungi Libreria')
        add_library_button.clicked.connect(self.add_library)

        self.libraries_layout.addWidget(add_library_button)
        self.libraries_layout.addSpacing(20)

        buttons = []
        for library in libraries:
            button_layout = QHBoxLayout()
            button = QPushButton(library)
            buttons.append(button)
            button.clicked.connect(lambda checked, b=button: self.on_button_clicked(b))
            remove_button = QPushButton()
            remove_button.setIcon(QIcon('icons/remove-icon.png'))
            remove_button.setStyleSheet('border: none;')
            remove_button.setCursor(Qt.PointingHandCursor)
            remove_button.setToolTip('Elimina Libreria')
            remove_button.clicked.connect(lambda checked, b=button, r=remove_button: self.remove_library_from_widget(b, r))
            button_layout.addWidget(button)
            button_layout.addWidget(remove_button)
            self.libraries_layout.addLayout(button_layout)

        self.button_style(buttons)

        return libraries_widget
    
    def add_library(self):
        dialog = AddLibraryDialog()
        dialog.add_library.connect(self.add_library_to_widget)
        dialog.exec_()
        
    def add_library_to_widget(self, library):
        button_layout = QHBoxLayout()
        button = QPushButton(library)
        button.clicked.connect(lambda checked, b=button: self.on_button_clicked(b))
        remove_button = QPushButton()
        remove_button.setIcon(QIcon('icons/remove-icon.png'))
        remove_button.setStyleSheet('border: none;')
        remove_button.setCursor(Qt.PointingHandCursor)
        remove_button.setToolTip('Elimina Libreria')
        remove_button.clicked.connect(lambda checked, b=button, r=remove_button: self.remove_library_from_widget(b, r))
        button_layout.addWidget(button)
        button_layout.addWidget(remove_button)
        self.libraries_layout.addLayout(button_layout)
        button.setStyleSheet(
                ' QPushButton { '
                    ' background-color: #1e0c53; '
                    ' border-radius: 8px; '
                    ' border: 1px solid white; '
                    ' color: white; '
                ' } '
                ' QPushButton:hover { '
                    ' background-color: #2f1188; '
                ' } '
                )
        button.setCursor(Qt.PointingHandCursor)
        button.setFixedSize(80, 20)
        self.add_library_to_db.emit(button.text())

    def remove_library_from_widget(self, button, remove_button):
        button.deleteLater()
        remove_button.deleteLater()
        self.remove_library_from_db.emit(button.text())

    def button_style(self, buttons):
        for button in buttons:
            button.setStyleSheet(
                ' QPushButton { '
                    ' background-color: #1e0c53; '
                    ' border-radius: 8px; '
                    ' border: 1px solid white; '
                    ' color: white; '
                ' } '
                ' QPushButton:hover { '
                    ' background-color: #2f1188; '
                ' } '
                )
            button.setCursor(Qt.PointingHandCursor)
            button.setFixedSize(80, 20)

    def on_button_clicked(self, button):
        if self.selected_button:
            self.selected_button.setStyleSheet(
                ' QPushButton { '
                    ' background-color: #1e0c53; '
                    ' border-radius: 8px; '
                    ' border: 1px solid white; '
                    ' color: white; '
                ' } '
                ' QPushButton:hover { '
                    ' background-color: #2f1188; '
                ' } '
            )

        button.setStyleSheet(
            ' QPushButton { '
                ' background-color: #3e1c73; '  # New color for selected button
                ' border-radius: 8px; '
                ' border: 1px solid white; '
                ' color: white; '
            ' } '
            ' QPushButton:hover { '
                ' background-color: #4e2c83; '  # New hover color for selected button
            ' } '
        )
        self.selected_button = button
        self.change_category.emit(button.text())
        


       

