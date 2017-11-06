from Components.User import User
from Components.KnowledgeBase import KnowledgeBase

"""Working memory is where all information about the current session is saved.
Working memory is updated and accessed constantly by the GUI and the inference engine.
Get's rules from the Knowledge Base
"""


class WorkingMemory:
    def __init__(self, user=User(), rules=[], phones=[], questions=[], knowledge_base=KnowledgeBase()):
        """
        Creates new working memory object

        :param user: user object
        :param rules: list
        :param phones: list
        :param questions: list
        :param knowledge_base: knowledge base object
        """
        self.user = user
        self.rules = rules
        self.phones = phones
        self.questions = questions
        self.knowledge_base = knowledge_base

    def set_user(self, user):
        """
        Sets user in working memory

        :param user: user object
        """
        self.user = user

    def set_rules(self, rules):
        """
        Sets rules in working memory

        :param rules: list
        """
        self.rules = rules

    def add_rule(self, rule):
        """
        Adds rule to current rules

        :param rule: rule object
        """
        self.rules.append(rule)
        self.knowledge_base.add_rule(rule)

    def set_phones(self, phones):
        """
        Sets phones from FileIO

        :param phones: list
        """
        self.phones = phones

    def set_questions(self, questions):
        """
        Sets questions from FileIO

        :param questions: list
        """
        self.questions = questions

    def add_question(self, question):
        """
        Adds question to current questions

        :param question: question object
        """
        self.questions.append(question)

    def get_user(self):
        """
        Returns user from working memory

        :return: user object
        """
        return self.user

    def get_rules(self):
        """
        Returns rules from working memory

        :return: list
        """
        return self.rules

    def get_phones(self):
        """
        Returns phones from working memory

        :return: list
        """
        return self.phones

    def get_questions(self):
        """
        Returns questions from working memory

        :return: list
        """
        return self.questions

    def __str__(self):
        """
        To string method
        :return: string
        """
        return print(self.user)
