"""A class to store questions.
Each question has content, set a possible answers, and topic.
Topics are used to link questions to rules and further to user attributes
"""

__author__ = 'Mike'
__version__ = '1.0'


class Question:
    def __init__(self, question=None, topic=None, possible_answers=None):
        """
        Creates new question object

        :param question: Sting of question
        :param topic: Sting of topic
        :param possible_answers: list of possible answers
        """
        self.question = question
        self.topic = topic
        self.possible_answers = possible_answers

    def set_question(self, question):
        """
        Sets question text

        :param question: string of question
        """
        self.question = question

    def set_topic(self, topic):
        """
        Sets topic

        :param topic: string of topic
        """
        self.topic = topic

    def set_possible_answers(self, possible_answers):
        """
        Sets possible answers

        :param possible_answers: list of possible answers
        """
        self.possible_answers = possible_answers

    def add_possible_answer(self, answer):
        """
        Adds answer to possible answers

        :param answer: add string to list
        """
        self.possible_answers.append(answer)

    def get_question(self):
        """
        Returns question text

        :return: string of question
        """
        return self.question

    def get_topic(self):
        """
        Returns topic text

        :return: string of topic
        """
        return self.topic

    def get_possible_answers(self):
        """
        Returns possible answers

        :return: list of answers
        """
        return self.possible_answers

