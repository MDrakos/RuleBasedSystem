class InferenceEngine:
    def __init__(self, working_memory):
        self.working_memory = working_memory

    def set_working_memory(self, working_memory):
        self.working_memory = working_memory

    def get_user(self):
        return self.working_memory.get_user()

    def get_rules(self):
        return self.working_memory.get_rules()

    def infer(self):
        user = self.working_memory.get_user()
        rules = self.working_memory.get_rules()
        consequents = []
        for answer in user.get_answers():
            for rule in rules:
                if answer.get_topic() == rule.get_topic():
                    if answer.get_content() in rule.get_antecedent():
                        consequents.append(rule.consequent)

        for rule in rules:
            if consequents == rule.get_antecedent():
                consequents = [rule.get_consequent()]

        print(consequents)