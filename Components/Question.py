class Question:
    def __init__(self, question=None, topic=None, possible_answers=None, user_answer=None):
        self.question = question
        self.topic = topic
        self.possible_answers = possible_answers
        self.user_answer = user_answer

    def set_question(self, question):
        self.question = question

    def set_topic(self, topic):
        self.topic = topic

    def set_possible_answers(self, possible_answers):
        self.possible_answers = possible_answers

    def add_possible_answer(self, answer):
        self.possible_answers.append(answer)

    def get_question(self):
        return self.question

    def get_topic(self):
        return self.topic

    def get_possible_answers(self):
        return self.possible_answers

    def get_user_answer(self):
        return self.user_answer
