import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit, QMessageBox, QFileDialog


class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        self.create_actions()
        self.create_menus()

        self.setWindowTitle("NotePad")
        self.setGeometry(100, 100, 800, 600)

    def create_actions(self):
        self.new_action = QAction("&Yangi", self)
        self.new_action.triggered.connect(self.new_file)

        self.open_action = QAction("&Ochish", self)
        self.open_action.triggered.connect(self.open_file)

        self.save_action = QAction("&Saqlash", self)
        self.save_action.triggered.connect(self.save_file)

        self.close_action = QAction("&Yopish", self)
        self.close_action.triggered.connect(self.close_file)

        self.edit_action = QAction("&Tahrirlash", self)
        self.edit_action.triggered.connect(self.edit_file)

    def create_menus(self):
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("&Fayl")
        file_menu.addAction(self.new_action)
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addAction(self.close_action)

        edit_menu = menu_bar.addMenu("&Fayllarni tahrirlash")
        edit_menu.addAction(self.edit_action)

    def new_file(self):
        self.text_edit.clear()

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Faylni tanlang", filter="JSON Fayllar (*.json)")
        if file_name:
            with open(file_name, 'r') as f:
                text = f.read()
                self.text_edit.setText(text)

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Faylni saqlash")
        if file_name:
            with open(file_name, 'w') as f:
                text = self.text_edit.toPlainText()
                f.write(text)

    def close_file(self):
        unsaved_text = self.text_edit.toPlainText()
        if unsaved_text.strip():
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Question)
            msg_box.setText("Kiritilgan ma'lumotlar saqlansinmi?")
            msg_box.setWindowTitle("Ogohlantirish?")
            msg_box.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
            ret = msg_box.exec_()
            if ret == QMessageBox.Save:
                self.save_file()
            elif ret == QMessageBox.Discard:
                self.text_edit.clear()
        else:
            self.text_edit.clear()

    def edit_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Fayl Tahrirlash', '', 'JSON Fayllar (*.json)')
        if file_path:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.text_edit.setText(data.get('mavzu', ''))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Notepad()
    window.show()
    sys.exit(app.exec_())







from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QLineEdit, QComboBox, QVBoxLayout, QHBoxLayout
from random import randint
from time import sleep

from PyQt5 import QtGui


class FirstWindow(QWidget):
    
  def __init__(self):
    super().__init__()
    self.VLay = QVBoxLayout(self)

    self.lbl1 = QLineEdit(self)
    self.lbl2 = QLineEdit(self)
    self.btn1 = QPushButton("click",self)
    self.btn1.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)

        
    self.hLay = QHBoxLayout(self)
    self.hLay.addWidget(self.lbl1)
    self.hLay.addWidget(self.lbl2)
    self.VLay.addLayout(self.hLay)

    self.btnLay = QHBoxLayout(self)
    self.btnLay.addWidget(self.btn1)


    self.VLay.addLayout(self.btnLay)

    self.setLayout(self.VLay)


app = QApplication([])
obj = FirstWindow()
obj.show()
app.exec()

