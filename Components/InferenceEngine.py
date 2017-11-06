from Components.WorkingMemory import WorkingMemory
from Components.ComplexRule import ComplexRule

"""Provides a class to preform forward chaining inference.
Uses working memory to get necessary rules.
Rules that have already been fired can be passed in later to assist self-learning
"""

__author__ = 'Mike'
__version__ = '1.0'


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

    # The main inference method
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

        # Isolate our rule as the rule with maximum salience
        our_rule = self.get_max_salience(potential_complex_rules)
        self.fired_rules.append(our_rule)
        for phone in phones:
            if our_rule:
                if our_rule.get_consequent() in phone.get_model():
                    user.set_phone(phone)
            else:
                user.set_phone(None)

    def find_new_rule(self):
        phones = self.working_memory.get_phones()
        rules = self.working_memory.get_rules()
        user = self.working_memory.get_user()
        fired_rules = self.get_fired_rules()
        last_fired_rule = fired_rules[-1]
        new_rule = ComplexRule()

        # Check if a complex rule was actually fired
        if last_fired_rule:
            last_fired_rule_antecedents = last_fired_rule.get_antecedent()
            potential_phones = []

            for phone in phones:
                phone_intersect = {}
                phone_attributes = phone.get_attributes()
                intersecting_keys = set(phone_attributes.keys() & last_fired_rule_antecedents.keys())
                for key in intersecting_keys:
                    if key in phone_attributes:
                        phone_intersect[key] = phone_attributes[key]

                if last_fired_rule_antecedents.items() == phone_intersect.items():
                    potential_phones.append(phone)

                    for rule in rules:
                        if rule.get_topic() == 'phone' and rule.get_antecedent().items() == phone_intersect.items() \
                                and rule.get_consequent() == phone.get_model():
                            return 0

            for potential_phone in potential_phones:
                new_rule = ComplexRule(last_fired_rule_antecedents, potential_phone.get_model(),
                                       last_fired_rule.get_topic(), last_fired_rule.get_salience()+1)

            return new_rule

        # If a complex rule wasn't fired, we will have to create a new one
        else:
            potential_phones = []
            for phone in phones:
                phone_intersect = {}
                phone_attributes = phone.get_attributes()
                intersecting_keys = set(phone_attributes.keys() & user.get_attributes().keys())
                for key in intersecting_keys:
                    if key in phone_attributes:
                        phone_intersect[key] = phone_attributes[key]

                if user.get_attributes().items() == phone_intersect.items():
                    potential_phones.append(phone)

                    for rule in rules:
                        if rule.get_topic() == 'phone' and rule.get_antecedent().items() == phone_intersect.items() \
                                and rule.get_consequent() == phone.get_model():
                            return 0

            for potential_phone in potential_phones:
                new_rule = ComplexRule(user.get_attributes(), potential_phone.get_model(),
                                       'phone', 1)

            return new_rule

    @staticmethod
    def get_max_salience(potential_complex_rules):
        max_salience = 0
        for complex_rule in potential_complex_rules:
            if complex_rule.get_salience() >= max_salience:
                max_salience = complex_rule.get_salience()

        for complex_rule in potential_complex_rules:
            if complex_rule.get_salience() == max_salience:
                return complex_rule

