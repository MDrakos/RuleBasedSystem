"""Provides an object to store 'simple' rules.
A simple rule only has one antecedent.
"""

__author__ = 'Mike'
__version__ = '1.0'


class Rule:
    def __init__(self, antecedent, consequent, topic="", salience=0):
        self.antecedent = antecedent
        self.consequent = consequent
        self.topic = topic
        self.salience = salience

    def set_antecedent(self, antecedent):
        self.antecedent = antecedent

    def set_consequent(self, consequent):
        self.consequent = consequent

    def set_topic(self, topic):
        self.topic = topic

    def set_salience(self, salience):
        self.salience = salience

    def get_antecedent(self):
        return self.antecedent

    def get_consequent(self):
        return self.consequent

    def get_topic(self):
        return self.topic

    def get_salience(self):
        return self.salience

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
