class KnowledgeBase:
    rules = []

    def __init__(self, rules=None):
        if rules is None:
            self.rules = []
        else:
            self.rules = rules

    def set_rules(self, rules):
        self.rules = rules

    def get_rules(self):
        return self.rules
