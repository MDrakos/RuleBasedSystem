"""Provides an object to store 'simple' rules.
A simple rule only has one antecedent.
"""

__author__ = 'Mike'
__version__ = '1.0'


class Rule:
    def __init__(self, antecedent, consequent, topic="", salience=0):
        """
        Creates new rule object

        :param antecedent: string antecedent
        :param consequent: string consequent
        :param topic: string topic
        :param salience: int salience
        """
        self.antecedent = antecedent
        self.consequent = consequent
        self.topic = topic
        self.salience = salience

    def set_antecedent(self, antecedent):
        """
        Sets antecedent of rule

        :param antecedent: string antecedent
        """
        self.antecedent = antecedent

    def set_consequent(self, consequent):
        """
        Sets consequent of rule

        :param consequent: string consequent
        """
        self.consequent = consequent

    def set_topic(self, topic):
        """
        Sets topic of question

        :param topic: string of topic
        """
        self.topic = topic

    def set_salience(self, salience):
        """
        Sets salience of question

        :param salience: int salience
        """
        self.salience = salience

    def get_antecedent(self):
        """
        Returns antecedent of question

        :return: string antecedent
        """
        return self.antecedent

    def get_consequent(self):
        """
        Returns consequent of question

        :return: string consequent
        """
        return self.consequent

    def get_topic(self):
        """
        Returns topic of question

        :return: string topic
        """
        return self.topic

    def get_salience(self):
        """
        Returns salience of question

        :return: int salience
        """
        return self.salience

    def __eq__(self, other):
        """
        Used to compare dict attributes of objects

        :param other: dict
        :return: 0 or 1 depending on equality
        """
        return self.__dict__ == other.__dict__
