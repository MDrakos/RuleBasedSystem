class Rule:
    def __init__(self, antecedent, consequent, topic=""):
        self.antecedent = antecedent
        self.consequent = consequent
        self.topic = topic

    def get_antecedent(self):
        return self.antecedent

    def get_consequent(self):
        return self.consequent

    def get_topic(self):
        return self.topic
