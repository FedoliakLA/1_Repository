class Title():
    def __init__(self, title_text, x_num, y_num):
        self.title = title_text
        self.cor = x_num, y_num
        self.appearance = True
    def hide(self):
        print(self.title, "- приховано")
        self.appearance = False
    def show(self):
        print(self.title, "- відображається")
        self.appearance = True
    def print_status(self):
        print("Кнопка:", self.title)
        print("Розташування:", self.cor)
        print("Видимість:", self.appearance)
title_1 = Title("Дізнатись переможця прямо зараз!", 150, 50)
title_2 = Title("Переможець може бути тільки один", 150, -100)
title_1.print_status()
title_2.print_status()
title_2.hide()



