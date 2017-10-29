class User:
    def __init__(self, first_name, last_name, answers=[], brand="", price="", phone=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.answers = answers
        self.brand = brand
        self.price = price
        self.phone = phone

    def set_answers(self, answers):
        self.answers = answers

    def set_answer(self, answer):
        self.answers.append(answer)

    def set_phone(self, phone):
        self.phone = phone

    def set_brand(self, brand):
        self.brand = brand

    def set_price(self, price):
        self.price = price

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_answers(self):
        return self.answers

    def get_phone(self):
        return self.phone

    def __str__(self):
        return self.get_first_name() + " " + self.get_last_name()
