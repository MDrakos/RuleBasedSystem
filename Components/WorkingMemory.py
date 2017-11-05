from Components.User import User
from Components.KnowledgeBase import KnowledgeBase


class WorkingMemory:
    def __init__(self, user=User(), rules=[], phones=[], questions=[], knowledge_base=KnowledgeBase()):
        self.user = user
        self.rules = rules
        self.phones = phones
        self.questions = questions
        self.knowledge_base = knowledge_base

    def set_user(self, user):
        self.user = user

    def set_rules(self, rules):
        self.rules = rules

    def add_rule(self, rule):
        self.rules.append(rule)
        self.knowledge_base.add_rule(rule)

    def set_phones(self, phones):
        self.phones = phones

    def set_questions(self, questions):
        self.questions = questions

    def add_question(self, question):
        self.questions.append(question)

    def get_user(self):
        return self.user

    def get_rules(self):
        return self.rules

    def get_phones(self):
        return self.phones

    def get_questions(self):
        return self.questions

    def __str__(self):
        return print(self.user)
