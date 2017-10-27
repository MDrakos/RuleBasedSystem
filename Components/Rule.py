class Rule:
    def __init__(self, antecedent, consequent):
        self.antecedent = antecedent
        self.consequent = consequent

    def get_antecedent(self):
        return self.antecedent

    def get_consequent(self):
        return self.consequent
