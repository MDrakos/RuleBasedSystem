import json

from Components.Rule import Rule
from Components.KnowledgeBase import KnowledgeBase


def load_rules(filepath):
    rules = []
    with open(filepath) as json_data:
        data = json.load(json_data)
        for rule in data:
            add = Rule(rule['antecedent'], rule['consequent'])
            rules.append(add)

    kb = KnowledgeBase(rules)

    for rul in kb.get_rules():
        print(rul.get_antecedent(), rul.get_consequent())

