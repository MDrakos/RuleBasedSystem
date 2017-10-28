from Components.Phone import Phone


class WorkingMemory:
    def __init__(self, user, rules, phone):
        self.user = user
        self.rules = rules
        self.phone = Phone()