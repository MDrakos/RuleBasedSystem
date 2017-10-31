import json

from Components.Rule import Rule
from Components.ComplexRule import ComplexRule
from Components.Question import Question
from Components.Phone import Phone
from Components.KnowledgeBase import KnowledgeBase


def load_rules(filepath):
    rules = []
    with open(filepath) as json_data:
        data = json.load(json_data)
        for rule in data:
            if isinstance(rule['antecedent'], dict):
                add = ComplexRule(rule['antecedent'], rule['consequent'], rule['topic'])
                rules.append(add)
            else:
                add = Rule(rule['antecedent'], rule['consequent'], rule['topic'])
                rules.append(add)

    # kb = KnowledgeBase(rules)
    #
    # for rul in kb.get_rules():
    #     print(rul.get_antecedent(), rul.get_consequent())

    return rules


def load_phones(filepath):
    phones = []
    attributes = {}
    with open(filepath) as json_data:
        data = json.load(json_data)
        for phone in data:
            # print(phone)
            for attribute in phone:
                attributes[attribute] = phone.get(attribute)
                # print(attribute, phone.get(attribute))
            phones.append(Phone(attributes))
            attributes = {}

    return phones

    # print(phones[0].get_attributes())


def load_questions(filepath):
    questions = []
    with open(filepath) as json_data:
        data = json.load(json_data)
        for question in data:
            quest = Question()
            answers = []
            for attribute in question:
                if attribute == 'question':
                    quest.set_question(question.get(attribute))
                if attribute == 'topic':
                    quest.set_topic(question.get(attribute))
                if 'answer' in attribute:
                    answers.append(question.get(attribute))
            quest.set_possible_answers(answers)
            questions.append(quest)

    return questions

    # print(questions[1].get_topic())