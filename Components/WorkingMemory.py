from Components.Phone import Phone


class WorkingMemory:
    def __init__(self, user, rules, phone=Phone()):
        self.user = user
        self.rules = rules
        self.phone = phone

    def set_user(self, user):
        self.user = user

    def set_rules(self, rules):
        self.rules = rules

    def set_phone(self, phone):
        self.phone = phone

    def add_rules(self, rule):
        self.rules.append(rule)

    def get_user(self):
        return self.user

    def get_rules(self):
        return self.rules

    def get_phone(self):
        return self.phone

    def __str__(self):
        return print(self.user)
