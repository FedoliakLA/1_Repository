from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox
import json

Form, Window = uic.loadUiType("Smart_notes.ui")

app = QApplication([])
window = Window()
form = Form()

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = form
        self.ui.setupUi(self)
        # self.notes = {
        # "Назва замітки": {
        #    "Текст": "Значення текста",
        #    "Теги": ["Значення тега"]
        #    }
        # }
        #
        # with open("notes_data.json", "w", encoding = "utf-8") as file:
        #    json.dump(self.notes, file, sort_keys = True)
        with open("notes_data.json", "r", encoding = "utf-8") as file:
            self.notes = json.load(file)
        self.ui.List_name.addItems(self.notes)
        self.ui.List_name.itemClicked.connect(self.show_note)

        self.ui.Create_pb.clicked.connect(self.add_note)
        self.ui.Del_pb.clicked.connect(self.del_note)
        self.ui.Save_pb.clicked.connect(self.save_note)

        self.ui.Addtag_pb.clicked.connect(self.add_tag)
        self.ui.Deletetag_pb.clicked.connect(self.del_tag)
        self.ui.Searchtag_pb.clicked.connect(self.find_tag)

    # Записки і дії з ними
    def show_note(self):
        name = form.List_name.selectedItems()[0].text()
        form.Note_edit.setText(self.notes[name]["Текст"])
        form.List_tag.clear()
        form.List_tag.addItems(self.notes[name]["Теги"])

    def add_note(self):
        note_name, ok = QInputDialog.getText(Notes, "Додати замітку", "Назва замітки: ")
        if ok and note_name != "":
            self.notes[note_name] = {"Текст": "", "Теги": []}
            self.ui.List_name.addItem(note_name)
            self.ui.List_tag.addItems(self.notes[note_name]["Теги"])
            print(self.notes)
        else:
            no_win = QMessageBox()
            no_win.setWindowTitle("Повідомлення")
            no_win.setText("Не вибрано замітки!")
            no_win.exec()

    def del_note(self):
        if self.ui.List_name.selectedItems():
            key = self.ui.List_name.selectedItems()[0].text()
            del self.notes[key]
            self.ui.List_name.clear()
            self.ui.List_tag.clear()
            self.ui.Note_edit.clear()
            self.ui.List_name.addItems(self.notes)
            with open("notes_data.json", "w", encoding = "utf-8") as file:
                json.dump(self.notes, file, sort_keys = True, ensure_ascii = False)
        else:
            no_win = QMessageBox()
            no_win.setWindowTitle("Повідомлення")
            no_win.setText("Не вибрано замітки!")
            no_win.exec()

    def save_note(self):
        if self.ui.List_name.selectedItems():
            key = self.ui.List_name.selectedItems()[0].text()
            self.notes[key]["Текст"] = self.ui.Note_edit.toPlainText()
            with open("notes_data.json", "w", encoding = "utf-8") as file:
                json.dump(self.notes, file, sort_keys = True, ensure_ascii = False)
        else:
            no_win = QMessageBox()
            no_win.setWindowTitle("Повідомлення")
            no_win.setText("Не вибрано замітки!")
            no_win.exec()

    # Дії над тегами
    def add_tag(self):
        if self.ui.List_name.selectedItems():
            key = self.ui.List_name.selectedItems()[0].text()
            tag = self.ui.Tag_ledit.text()
            if not tag in self.notes[key]["Теги"]:
                self.notes[key]["Теги"].append(tag)
                self.ui.List_tag.addItem(tag)
                self.ui.Tag_ledit.clear()
            with open("notes_data.json", "w", encoding = "utf-8") as file:
                json.dump(self.notes, file, sort_keys = True, ensure_ascii = False)
        else:
            no_win = QMessageBox()
            no_win.setWindowTitle("Повідомлення")
            no_win.setText("Не вибрано замітки!")
            no_win.exec()

    def del_tag(self):
        if self.ui.List_name.selectedItems():
            key = self.ui.List_name.selectedItems()[0].text()
            tag = self.ui.List_tag.selectedItems()[0].text()
            self.notes[key]["Теги"].remove(tag)
            self.ui.List_tag.clear()
            self.ui.List_tag.addItems(self.notes[key]["Теги"])
            with open("notes_data.json", "w", encoding = "utf-8") as file:
                json.dump(self.notes, file, sort_keys = True, ensure_ascii = False)
        else:
            no_win = QMessageBox()
            no_win.setWindowTitle("Повідомлення")
            no_win.setText("Не вибрано замітки!")
            no_win.exec()

    def find_tag(self):
        tag = self.ui.Tag_ledit.text()
        if self.ui.Searchtag_pb.text() == "Шукати замітку по тегу" and tag:
            notes_filtered = {}
            for note in self.notes:
                if tag in self.notes[note]["Теги"]:
                    notes_filtered[note] = self.notes[note]
            self.ui.Searchtag_pb.setText("Скинути пошук")
            self.ui.List_name.clear()
            self.ui.List_tag.clear()
            self.ui.List_name.addItems(notes_filtered)
        elif self.ui.Searchtag_pb.text() == "Скинути пошук":
            self.ui.Tag_ledit.clear()
            self.ui.List_name.clear()
            self.ui.List_tag.clear()
            self.ui.List_name.addItems(self.notes)
            self.ui.Searchtag_pb.setText("Шукати замітку по тегу")
        else:
            no_win = QMessageBox()
            no_win.setWindowTitle("Повідомлення")
            no_win.setText("Не вибрано тегу!")
            no_win.exec()



Notes = Widget()


Notes.show()
app.exec()