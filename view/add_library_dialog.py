from PyQt5.QtWidgets import QVBoxLayout, QDialog, QPushButton, QHBoxLayout, QLabel, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal

class AddLibraryDialog(QDialog):
    add_library = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Aggiungi Libreria')
        self.setStyleSheet('background-color: #2f1188; color: white;')
        self.setMinimumSize(400, 100)
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter | Qt.AlignTop)

        library_name_label = QLabel('Nome Libreria:')
        library_name_edit = QLineEdit()

        add_button = QPushButton('Aggiungi')
        cancel_button = QPushButton('Annulla')

        button_layout = self.button_layout(add_button, cancel_button)

        add_button.clicked.connect(lambda: self.accept_dialog(library_name_edit))
        cancel_button.clicked.connect(self.close)

        layout.addWidget(library_name_label)
        layout.addWidget(library_name_edit)
        layout.addLayout(button_layout)

    def accept_dialog(self, library_name_edit):
        if library_name_edit.text() != '':
            self.accept()
            self.add_library.emit(library_name_edit.text())
        else:
            message = QMessageBox()
            message.setWindowTitle('Errore')
            message.setText('Inserisci il nome della libreria')
            message.exec_()

    def button_layout(self, add_button, cancel_button):
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignCenter)
        add_button.setStyleSheet(
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
        add_button.setCursor(Qt.PointingHandCursor)
        add_button.setFixedSize(80, 20)

        cancel_button.setStyleSheet(
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
        cancel_button.setCursor(Qt.PointingHandCursor)
        cancel_button.setFixedSize(80, 20)

        button_layout.addWidget(add_button)
        button_layout.addWidget(cancel_button)
        
        return button_layout

        