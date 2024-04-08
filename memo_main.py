from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import choice, shuffle
from time import sleep

app = QApplication([])

from memo_window import *
from memo_menu import *

# Fucktions
button_pack = [rb_ans_1, rb_ans_2, rb_ans_3, rb_ans_4]

class Question():
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question
        self.answer = answer
        self.wrong_answer_1 = wrong_ans1
        self.wrong_answer_2 = wrong_ans2
        self.wrong_answer_3 = wrong_ans3
        self.count_asked = 0
        self.count_answered = 0

    def got_right(self):
        self.count_asked += 1
        self.count_answered += 1

    def got_wrong(self):
        self.count_asked += 1

q1 = Question("Торт", "Cake", "Drive", "Pocket", "Boot")
q2 = Question("Горілка", "Vodka", "Anticipation", "Race", "Obese")
q3 = Question("Ніж", "Knife", "Opinion", "Influence", "Large")
q4 = Question("Хороші росіяни", "Dead russians", "Mint", "Count", "Breeze")
q5 = Question("Гранатомет", "Grenade launcher", "Bear", "Upset", "Skate")
q6 = Question("Пуцьвірінок", "A small thing", "Rich", "Biscuit", "Minister")
question_pack = [q1, q2, q3, q4, q5, q6]

curr_q = Question("Питання", "відповідь", "1", "2", "3")
def new_question():
    global curr_q
    curr_q = choice(question_pack)
    lb_question.setText(curr_q.question)
    lb_answer.setText(curr_q.answer)
    shuffle(button_pack)
    button_pack[0].setText(curr_q.answer)
    button_pack[1].setText(curr_q.wrong_answer_1)
    button_pack[2].setText(curr_q.wrong_answer_2)
    button_pack[3].setText(curr_q.wrong_answer_3)

def check_answer():
    global curr_q
    for answer in button_pack:
        if answer.isChecked():
            answer.setChecked(False)
            if answer.text() == lb_answer.text():
                curr_q.got_right()
                lb_result.setText("Правильно!")
                break
    else:
        lb_result.setText("Не правильно!")
        curr_q.got_wrong()

def switch_screen():
    if btn_answer.text() == "Щира відповідь":
        check_answer()
        gb_question.hide()
        gb_answer.show()
        btn_answer.setText("Некст запитання")
    else:
        new_question()
        gb_question.show()
        gb_answer.hide()
        btn_answer.setText("Щира відповідь")




btn_answer.clicked.connect(switch_screen)

#Son

def vidpochynok():
    main_win.hide()
    n = sp_vidpochynok.value() * 60
    sleep(n)
    main_win.show()

btn_vidpochynok.clicked.connect(vidpochynok)

# Clear ledit
def clear():
    led_question.clear()
    led_right_ans.clear()
    led_wrong_ans1.clear()
    led_wrong_ans2.clear()
    led_wrong_ans3.clear()
btn_clear.clicked.connect(clear)


#Dodaty pietannia
def add_question():
    new_q = Question(led_question.text(), led_right_ans.text(), led_wrong_ans1.text(), led_wrong_ans2.text(), led_wrong_ans3.text())
    question_pack.append(new_q)
    clear()
btn_add_qst.clicked.connect(add_question)


#Menu findow
def gen_menu():
    if curr_q.question != "Питання":
        if curr_q.count_asked == 0:
            c = 0
        else:
            c = (curr_q.count_answered / curr_q.count_asked) * 100
        text_st = f'Кількість відповідей: {curr_q.count_asked}\n' \
                f'Правильних відповідей: {curr_q.count_answered}\n' \
               f'Успішність: {round(c, 2)}%'

        lb_stats.setText(text_st)
    menu_wind.show()
    main_win.hide()

btn_menu.clicked.connect(gen_menu)


def degen_menu():
    menu_wind.hide()
    main_win.show()

btn_back.clicked.connect(degen_menu)



main_win.show()
app.exec()