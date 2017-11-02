"""Provides an object to store rules
Used by the working memory
"""

__author__ = 'Mike'
__version__ = '1.0'


class KnowledgeBase:
    def __init__(self, rules=[]):
        self.rules = rules

    def set_rules(self, rules):
        self.rules = rules

    def add_rule(self, rule):
        self.rules.append(rule)

    def get_rules(self):
        return self.rules
