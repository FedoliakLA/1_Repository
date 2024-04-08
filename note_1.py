from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from random import randint, choice

Form, Window = uic.loadUiType("Password_gen.ui")


def example():
    signs = ""
    if form.Alphabet.isChecked():
        signs += "abcdefghijklmnopqrstuvwxyz"
    if form.Number.isChecked():
        signs += "0123456789"

    result = ""
    number = randint(5, 10)
    if signs != "":
        for i in range(number):
            result += choice(signs)

    form.Result.setText(result)
    print(1)


app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
form.Generate.clicked.connect(example)

window.show()
app.exec()