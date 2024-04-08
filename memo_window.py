from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup, QSpinBox
from random import shuffle, randint
main_win = QWidget()
main_win.resize(500, 400)
main_win.setWindowTitle("Флеш-картки")
main_win.move(0, 0)

# Kvadrat_knopky
btn_menu = QPushButton("Меню")
btn_answer = QPushButton("Щира відповідь")

# SpinBox
btn_vidpochynok = QPushButton("Відпочілити")
sp_vidpochynok = QSpinBox()
sp_vidpochynok.setValue(30)

# Radio_knopky
rb_ans_1 = QRadioButton("1")
rb_ans_2 = QRadioButton("2")
rb_ans_3 = QRadioButton("3")
rb_ans_4 = QRadioButton("4")

# RadioBanda
RadioBand = QButtonGroup()
RadioBand.addButton(rb_ans_1)
RadioBand.addButton(rb_ans_2)
RadioBand.addButton(rb_ans_3)
RadioBand.addButton(rb_ans_4)

RadioBand.setExclusive(False)
# Leybl
lb_question = QLabel("Питання")

lb_vidpochynok = QLabel("хвилин")
lb_result = QLabel("Правильно")
lb_answer = QLabel("відповідь")

# Група-боксів
gb_question = QGroupBox("Варіанти відповідей:")

# Layout
line_main = QVBoxLayout()

# Перша лінія
rb_h_a = QHBoxLayout()

rb_h_a.addWidget(btn_menu, alignment = Qt.AlignmentFlag.AlignLeft)
rb_h_a.addStretch(1)
rb_h_a.addWidget(btn_vidpochynok, alignment = Qt.AlignmentFlag.AlignRight)
rb_h_a.addWidget(sp_vidpochynok, alignment = Qt.AlignmentFlag.AlignRight)
rb_h_a.addWidget(lb_vidpochynok, alignment = Qt.AlignmentFlag.AlignRight)

# Друга лінія
rb_h_b = QHBoxLayout()
rb_h_b.addWidget(lb_question, alignment = Qt.AlignmentFlag.AlignCenter)

# Третя лінія
rb_v1 = QVBoxLayout()
rb_v2 = QVBoxLayout()
rb_h1 = QHBoxLayout()


rb_v1.addWidget(rb_ans_1)
rb_v1.addWidget(rb_ans_2)

rb_v2.addWidget(rb_ans_3)
rb_v2.addWidget(rb_ans_4)

rb_h1.addLayout(rb_v1)
rb_h1.addLayout(rb_v2)

gb_question.setLayout(rb_h1)

# Четверта лінія
rb_h_ans = QHBoxLayout()
btn_answer = QPushButton("Починаємо!")
rb_h_ans.addWidget(btn_answer, stretch = 2, alignment = Qt.AlignmentFlag.AlignCenter)
# Група "відповідь"
gb_answer = QGroupBox()

ans_v1 = QVBoxLayout()

ans_v1.addWidget(lb_result)
ans_v1.addWidget(lb_answer)
gb_answer.setLayout(ans_v1)

# Основна лінія
line_main = QVBoxLayout()
line_main.addLayout(rb_h_a)
line_main.addLayout(rb_h_b)
line_main.addWidget(gb_question)
line_main.addWidget(gb_answer)
gb_answer.hide()
line_main.addLayout(rb_h_ans)


main_win.setLayout(line_main)

