class Widget():
    def __init__(self, title_text, x_cor, y_cor):
        self.title = title_text
        self.x = x_cor
        self.y = y_cor

    def print_info(self):
        print("Напис:", self.title)
        print("Розташування:", self.x, self.y)


class Button(Widget):
    def __init__(self, title_text, x_cor, y_cor, is_clicked):
        super().__init__(title_text, x_cor, y_cor)
        self.clicked = is_clicked

    def click(self):
        self.clicked = True
        print("Ви зареєстровані")


button_1 = Button("Брати участь", 100, 100, False)
answer = input("Хочете зареєструватися?(так/ні): ")
if answer == "так":
    button_1.click()
elif answer == "ні":
    print("А шкода!")
