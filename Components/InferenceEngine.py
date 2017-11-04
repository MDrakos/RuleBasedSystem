from Components.WorkingMemory import WorkingMemory


class InferenceEngine:
    def __init__(self, working_memory=WorkingMemory(), fired_rules=[]):
        self.working_memory = working_memory
        self.fired_rules = fired_rules

    def set_working_memory(self, working_memory):
        self.working_memory = working_memory

    def get_user(self):
        return self.working_memory.get_user()

    def get_rules(self):
        return self.working_memory.get_rules()

    def get_fired_rules(self):
        return self.fired_rules

    def infer(self):
        user = self.working_memory.get_user()
        rules = self.working_memory.get_rules()
        phones = self.working_memory.get_phones()
        consequents = []
        potential_complex_rules = []

        # First, for basic rules add their consequences as user attributes
        for answer in user.get_answers():
            for rule in rules:
                if answer.get_topic() == rule.get_topic():
                    if answer.get_content() in rule.get_antecedent():
                        self.fired_rules.append(rule)
                        consequents.append(rule.consequent)
                        user.add_attribute(rule.get_topic(), rule.get_consequent())

        # For rules with a complex antecedent compare the antecedent with the user attributes
        # and fire the correct rule
        for rule in rules:
            # Isolate rules with complex antecedents
            if isinstance(rule.get_antecedent(), dict):
                rule_antecedents = rule.get_antecedent()
                user_attributes = user.get_attributes()
                if rule_antecedents.items() == user_attributes.items():
                    potential_complex_rules.append(rule)

        our_rule = self.get_max_salience(potential_complex_rules)
        self.fired_rules.append(our_rule)
        for phone in phones:
            if our_rule.get_consequent() in phone.get_model():
                user.set_phone(phone)

    @staticmethod
    def get_max_salience(potential_complex_rules):
        max_salience = 0
        for complex_rule in potential_complex_rules:
            if complex_rule.get_salience() > max_salience:
                max_salience = complex_rule.get_salience()

        for complex_rule in potential_complex_rules:
            if complex_rule.get_salience() == max_salience:
                return complex_rule
