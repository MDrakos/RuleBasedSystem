import json

from Components.Rule import Rule


def load_rules(filepath):
    rules = []
    with open(filepath) as json_data:
        data = json.load(json_data)
        for rule in data:
            add = Rule(rule['antecedent'], rule['consequent'])
            rules.append(add)

    print(rules[0].antecedent, rules[0].consequent)

