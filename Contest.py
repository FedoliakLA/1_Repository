from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton

app = QApplication([])
main_win = QWidget()
main_win.resize(400, 200)
main_win.setWindowTitle("Конкурс від Crazy People")

question = QLabel("В якому році канал отримав золоту кнопку YouTube?")

button_1 = QRadioButton('2005')
button_2 = QRadioButton('2010')
button_3 = QRadioButton('2015')
button_4 = QRadioButton('2020')


main_layout = QVBoxLayout()
line_h_1 = QHBoxLayout()
line_h_2 = QHBoxLayout()
line_h_3 = QHBoxLayout()

line_h_1.addWidget(question, alignment = Qt.AlignmentFlag.AlignCenter)
line_h_2.addWidget(button_1, alignment = Qt.AlignmentFlag.AlignCenter)
line_h_2.addWidget(button_2, alignment = Qt.AlignmentFlag.AlignCenter)
line_h_3.addWidget(button_3, alignment = Qt.AlignmentFlag.AlignCenter)
line_h_3.addWidget(button_4, alignment = Qt.AlignmentFlag.AlignCenter)

main_layout.addLayout(line_h_1)
main_layout.addLayout(line_h_2)
main_layout.addLayout(line_h_3)

def show_victory():
    victory_win = QMessageBox()
    victory_win.setText("Правильно! Ви виграли гіроскутер!")
    victory_win.exec()
def show_lose():
    lose_win = QMessageBox()
    lose_win.setText("Ні, в 2015 році Crazy People виграли золоту кнопку!")
    lose_win.exec()

button_1.clicked.connect(show_lose)
button_2.clicked.connect(show_lose)
button_3.clicked.connect(show_victory)
button_4.clicked.connect(show_lose)

main_win.setLayout(main_layout)
main_win.show()
app.exec()