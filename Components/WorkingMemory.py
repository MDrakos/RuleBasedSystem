class WorkingMemory:
    def __init__(self, user, rules=[], phones=[]):
        self.user = user
        self.rules = rules
        self.phones = phones

    def set_user(self, user):
        self.user = user

    def set_rules(self, rules):
        self.rules = rules

    def set_phones(self, phones):
        self.phones = phones

    def add_rules(self, rule):
        self.rules.append(rule)

    def get_user(self):
        return self.user

    def get_rules(self):
        return self.rules

    def get_phones(self):
        return self.phones

    def __str__(self):
        return print(self.user)
