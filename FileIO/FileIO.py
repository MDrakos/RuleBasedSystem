import json

from Components.Rule import Rule
from Components.KnowledgeBase import KnowledgeBase
from Components.Phone import Phone


def load_rules(filepath):
    rules = []
    with open(filepath) as json_data:
        data = json.load(json_data)
        for rule in data:
            add = Rule(rule['antecedent'], rule['consequent'])
            rules.append(add)

    # kb = KnowledgeBase(rules)
    #
    # for rul in kb.get_rules():
    #     print(rul.get_antecedent(), rul.get_consequent())


def load_phones(filepath):
    phones = []
    attributes = {}
    with open(filepath) as json_data:
        data = json.load(json_data)
        for phone in data:
            for attribute in phone:
                attributes[attribute] = phone.get(attribute)
                # print(attribute, phone.get(attribute))
            phones.append(Phone(attributes))

    print(phones[0].get_attributes())