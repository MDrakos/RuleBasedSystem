class User:
    def __init__(self, first_name, last_name, answers=None, phone=None):
        if answers is None:
            self.answers = []
        if phone is None:
            self.phone = ""
        else:
            self.first_name = first_name
            self.last_name = last_name
            self.answers = answers
            self.phone = phone

    def set_answers(self, answers):
        self.answers = answers

    def set_answer(self, answer):
        self.answers.append(answer)

    def set_phone(self, phone):
        self.phone = phone

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
