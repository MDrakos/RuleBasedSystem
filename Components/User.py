"""Provides a class to store user information
Attributes are connected to Topics and compared in the inference engine
"""

__author__ = 'Mike'
__version__ = '1.0'


class User:
    def __init__(self, first_name="", last_name="", answers=[], attributes={}, phone=[]):
        """
        Creates new user object

        :param first_name: string
        :param last_name: string
        :param answers: list
        :param attributes: dictionary
        :param phone: list
        """
        self.first_name = first_name
        self.last_name = last_name
        self.answers = answers
        self.attributes = attributes
        self.phone = phone

    def set_user_first_name(self, first_name):
        """
        Sets first name of user

        :param first_name: string
        """
        self.first_name = first_name

    def set_user_last_name(self, last_name):
        """
        Sets last name of user

        :param last_name: string
        """
        self.last_name = last_name

    def set_answers(self, answers):
        """
        Sets users answers

        :param answers: list
        """
        self.answers = answers

    def set_answer(self, answer):
        """
        Adds answer to users answers

        :param answer: string
        """
        self.answers.append(answer)

    def set_phone(self, phone):
        """
        Sets phone for user

        :param phone: Phone object
        """
        self.phone = phone

    def set_attributes(self, attributes):
        """
        Sets attributes for user

        :param attributes: dictionary
        """
        self.attributes = attributes

    def add_attribute(self, topic, value):
        """
        Adds attribute for user

        :param topic: string
        :param value: string
        """
        self.attributes[topic] = value

    def get_first_name(self):
        """
        Returns user's first name

        :return: string
        """
        return self.first_name

    def get_last_name(self):
        """
        Returns user's last name

        :return: string
        """
        return self.last_name

    def get_answers(self):
        """
        Returns user's answers

        :return: list
        """
        return self.answers

    def get_attributes(self):
        """
        Returns user's attributes

        :return: dictionary
        """
        return self.attributes

    def get_phone(self):
        """
        Returns users phones

        :return: list
        """
        return self.phone

    def __str__(self):
        """
        To string method

        :return: string of users first name and last name
        """
        return self.get_first_name() + " " + self.get_last_name()
