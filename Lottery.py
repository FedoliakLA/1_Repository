from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint
app = QApplication([])
main_win = QWidget()
main_win.resize(400, 200)
main_win.setWindowTitle("Лото-забава!")
button = QPushButton("Спробувати вдачу")
text = QLabel("Виграєш чи ні? Зараз побачимо! Натискай кнопку!")
num_1_t = QLabel("?")
num_2_t = QLabel("?")

line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignmentFlag.AlignCenter)
line.addWidget(num_1_t, alignment = Qt.AlignmentFlag.AlignCenter)
line.addWidget(num_2_t, alignment = Qt.AlignmentFlag.AlignCenter)
line.addWidget(button, alignment = Qt.AlignmentFlag.AlignCenter)
main_win.setLayout(line)
def show_peremoga():
    number_1 = randint(1, 10)
    number_2 = randint(1, 10)
    if number_1 == number_2:
        text.setText("Ви виграли")
        num_1_t.setText(str(number_1))
        num_2_t.setText(str(number_2))
        button.setText("Грати знову")
    else:
        text.setText("Ви програли")
        num_1_t.setText(str(number_1))
        num_2_t.setText(str(number_2))
        button.setText("Спробувати ще раз")
button.clicked.connect(show_peremoga)

main_win.show()
app.exec()