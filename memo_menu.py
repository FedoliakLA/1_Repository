from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QHBoxLayout

menu_wind = QWidget()
menu_wind.move(0, 0)
menu_wind.setWindowTitle("Меню")

#Leybl
lb_quest = QLabel("Введіть питальне слово:")
lb_right_ans = QLabel("Введіть правильну відповідь:")
lb_wrong_ans1 = QLabel("Введіть першу хибну відповідь:")
lb_wrong_ans2 = QLabel("Введіть другу хибну відповідь:")
lb_wrong_ans3 = QLabel("Введіть третю хибну відповідь:")

#Ledit
led_question = QLineEdit()
led_right_ans = QLineEdit()
led_wrong_ans1 = QLineEdit()
led_wrong_ans2 = QLineEdit()
led_wrong_ans3 = QLineEdit()

#BTRPack
btn_back = QPushButton("Повернутися")
btn_add_qst = QPushButton("Додати питання")
btn_clear = QPushButton("Очистити бланк")

#Leybl, but cooler
lb_head_stat = QLabel("Статистика")
lb_head_stat.setStyleSheet('font-size: 19px; font-weight: bold;')
lb_stats = QLabel()

#Vertical leybl
vl_labels = QVBoxLayout()
vl_labels.addWidget(lb_quest)
vl_labels.addWidget(lb_right_ans)
vl_labels.addWidget(lb_wrong_ans1)
vl_labels.addWidget(lb_wrong_ans2)
vl_labels.addWidget(lb_wrong_ans3)

#VerticalLedit
vl_ledit = QVBoxLayout()
vl_ledit.addWidget(led_question)
vl_ledit.addWidget(led_right_ans)
vl_ledit.addWidget(led_wrong_ans1)
vl_ledit.addWidget(led_wrong_ans2)
vl_ledit.addWidget(led_wrong_ans3)

#Damm, a horizontal
hl_question = QHBoxLayout()
hl_question.addLayout(vl_labels)
hl_question.addLayout(vl_ledit)

#Horizontal, but buttons
hl_buttons = QHBoxLayout()
hl_buttons.addWidget(btn_add_qst)
hl_buttons.addWidget(btn_clear)

#The Boss vertical
vl_res = QVBoxLayout()
vl_res.addLayout(hl_question)
vl_res.addLayout(hl_buttons)
vl_res.addWidget(lb_head_stat)
vl_res.addWidget(lb_stats)
vl_res.addWidget(btn_back)


menu_wind.setLayout(vl_res)

