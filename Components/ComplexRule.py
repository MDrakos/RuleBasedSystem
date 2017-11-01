"""Provides a class to store complex rules.

Complex rules contain a complex antecedent which is a dictionary
of consequences from previous rules.

Each rule is tied to a topic, so the topics serve as keys in the
complex_antecedent dict and the consequent is the value.
"""

__author__ = 'Mike'
__version__ = '1.0'


class ComplexRule:
    def __init__(self, complex_antecedent={}, consequent="", topic=""):
        self.complex_antecedent = complex_antecedent
        self.consequent = consequent
        self.topic = topic

    def set_antecedent(self, complex_antecedent):
        self.complex_antecedent = complex_antecedent

    def set_consequent(self, consequent):
        self.consequent = consequent

    def get_antecedent(self):
        return self.complex_antecedent

    def get_consequent(self):
        return self.consequent

    def get_topic(self):
        return self.topic
