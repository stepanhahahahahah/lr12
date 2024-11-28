from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QTextEdit, QFileDialog, QListView
from PyQt6.QtCore import QStringListModel
from database import Database
from form_window import FormWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Главная")
        self.resize(800,600)
        
        list_model = QStringListModel()
        list_model.setStringList(self.get_animals())
        
        list_widget = QWidget()
        self.list_view = QListView(list_widget)
        self.list_view.setModel(list_model)
        self.list_view.resize(800,600)
        
        self.add_button = QPushButton("Добавить")
        self.add_button.clicked.connect(self.add_animals)
        self.del_button = QPushButton("Удалить")
        self.del_button.clicked.connect(self.del_animals)
        self.edit_button = QPushButton("Изменить")
        self.edit_button.clicked.connect(self.edit_animals)
        self.update_button = QPushButton("Обновить")
        self.update_button.clicked.connect(self.update_list_view_animals)
        
        buttons = QHBoxLayout()
        buttons.addWidget(self.add_button)
        buttons.addWidget(self.del_button)
        buttons.addWidget(self.edit_button)
        buttons.addWidget(self.update_button)

        buttons_widget = QWidget()
        buttons_widget.setLayout(buttons)

        layout = QVBoxLayout()
        layout.addWidget(buttons_widget)
        layout.addWidget(list_widget)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def get_list_model_animals(self):
        list_model = QStringListModel()
        list_model.setStringList(self.get_animals())
        return list_model
    
    def update_list_view_animals(self):
        self.list_view.setModel(self.get_list_model_animals())

    def get_animals(self):
        db = Database()
        result_raw = db.get_animals()
        result = []
        for r in result_raw:
            result.append(str(r["id"]) + ":" + r["name"])
        return result
        
    def del_animals(self):
        db = Database()
        indexes = self.list_view.selectedIndexes()
        for index in indexes:
            id = str(index.data()).split(":")[0]
            db.del_animals(id)
        self.update_list_view_animals()
        
    def add_animals(self):
        form_window = FormWindow(self)
        if form_window.exec() == 1:
            db = Database()
            db.add_animals(form_window.name_text.text())
            self.update_list_view_animals()
        
    def edit_animals(self):
        if len(self.list_view.selectedIndexes()) <= 0: return
        form_window = FormWindow(self, str(self.list_view.selectedIndexes()[0].data()))
        if form_window.exec() == 1:
            db = Database()
            db.edit_animals(form_window.name_text.text(), form_window.id)
            self.update_list_view_animals()