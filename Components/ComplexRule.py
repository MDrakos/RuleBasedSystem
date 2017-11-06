"""Provides a class to store complex rules.

Complex rules contain a complex antecedent which is a dictionary
of consequences from previous rules.

Each rule is tied to a topic, so the topics serve as keys in the
complex_antecedent dict and the consequent is the value.
"""

__author__ = 'Mike'
__version__ = '1.0'


class ComplexRule:
    def __init__(self, complex_antecedent={}, consequent="", topic="", salience=0):
        """
        Creates a new complex rule

        :param complex_antecedent: dictionary of antecedents
        :param consequent: consequent of the rule
        :param topic: topic of the rule
        :param salience: salience value of the rul
        """
        self.complex_antecedent = complex_antecedent
        self.consequent = consequent
        self.topic = topic
        self.salience = salience

    def set_antecedent(self, complex_antecedent):
        """
        Sets the antecedents of the rul

        :param complex_antecedent: dictionary of antecedents
        """
        self.complex_antecedent = complex_antecedent

    def set_consequent(self, consequent):
        """
        Sets the consequent of the complex rule

        :param consequent: string consequent
        """
        self.consequent = consequent

    def set_salience(self, salience):
        """
        Sets salience value for rule

        :param salience: int
        """
        self.salience = salience

    def get_antecedent(self):
        """
        Returns antecedents

        :return: dictionary of antecedents
        """
        return self.complex_antecedent

    def get_consequent(self):
        """
        Returns consequent of rule

        :return: string consequent
        """
        return self.consequent

    def get_topic(self):
        """
        Returns topic of rule

        :return: string topic
        """
        return self.topic

    def get_salience(self):
        """
        Returns salience of rule

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

