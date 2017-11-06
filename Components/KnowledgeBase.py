"""Provides an object to store rules
Used by the working memory
"""

__author__ = 'Mike'
__version__ = '1.0'


class KnowledgeBase:
    def __init__(self, rules=[]):
        """
        Creates new knowledge base

        :param rules: list of rules
        """
        self.rules = rules

    def set_rules(self, rules):
        """
        Sets rules of knowledge base

        :param rules: list of rules
        """
        self.rules = rules

    def add_rule(self, rule):
        """
        Adds rule to knowledge base

        :param rule: Rule object
        """
        self.rules.append(rule)

    def get_rules(self):
        """
        Gets list of rules from the knowledge base

        :return: list of rules
        """
        return self.rules
