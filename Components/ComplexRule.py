class ComplexRule:
    def __init__(self, complex_antecedent={}, consequent="", topic=""):
        self.complex_antecedent = complex_antecedent
        self.consequent = consequent
        self.topic = topic

    def set_antecedent(self, complex_antecedent):
        self.complex_antecedent = complex_antecedent

    def set_consequent(self, consequent):
        self.consequent = consequent

    def get_antecedent(self):
        return self.complex_antecedent

    def get_consequent(self):
        return self.consequent

    def get_topic(self):
        return self.topic
