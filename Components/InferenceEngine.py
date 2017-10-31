from Components.WorkingMemory import WorkingMemory


class InferenceEngine:
    def __init__(self, working_memory=WorkingMemory()):
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
        phones = self.working_memory.get_phones()
        consequents = []
        for answer in user.get_answers():
            for rule in rules:
                if answer.get_topic() == rule.get_topic():
                    if answer.get_content() in rule.get_antecedent():
                        consequents.append(rule.consequent)
                        user.add_attribute(rule.get_topic(), rule.get_antecedent())

        for rule in rules:
            if isinstance(rule.get_antecedent(), dict):
                for antecedents in rule.get_antecedent():
                    for attributes in user.get_attributes():
                        if antecedents == attributes:
                            for phone in phones:
                                if rule.get_consequent() in phone.get_model():
                                    user.set_phone(phone)

        # print(user.get_phone())