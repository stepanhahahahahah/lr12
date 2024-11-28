from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QTextEdit, QFileDialog, QListView, QLabel, QLineEdit, QDialog

class FormWindow(QDialog):
    def __init__(self, parent = None, object = None):
        super().__init__(parent)
        if object is None:
            self.setWindowTitle("Форма Добавления")
            self.button = QPushButton("Добавить")
            self.button.clicked.connect(self.button_click)
        else:
            self.setWindowTitle("Форма Изменения")
            self.button = QPushButton("Изменить")
            self.button.clicked.connect(self.button_click)
            self.id = object.split(":")[0]

        label = QLabel("Название: ")
        if object is None:
            self.name_text = QLineEdit()
        else:
            self.name_text = QLineEdit(object.split(":")[1])

        name_input = QHBoxLayout()
        name_input.addWidget(label)
        name_input.addWidget(self.name_text)
        name_input_widget = QWidget()
        name_input_widget.setLayout(name_input)

        layout = QVBoxLayout()
        layout.addWidget(name_input_widget)
        layout.addWidget(self.button)

        self.setLayout(layout)
    def button_click(self):
        self.done(1)
