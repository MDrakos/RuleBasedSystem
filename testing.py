# This file is for testing while in development!
from FileIO import FileIO
from Components.User import User
from Components.Answer import Answer
from Components.WorkingMemory import WorkingMemory
from Components.InferenceEngine import InferenceEngine
from Components.KnowledgeBase import KnowledgeBase
from Components.ComplexRule import ComplexRule

def test_file_io():
    FileIO.load_rules('JSON/rules.json')
    FileIO.load_phones('JSON/phones.json')
    FileIO.load_questions('JSON/questions.json')

# test_file_io()


def test_process():
    # create blank user, working memory, and knowledge base
    user = User()
    wm = WorkingMemory()
    kb = KnowledgeBase()

    # Import rules, phones, and questions
    rules = FileIO.load_rules('JSON/rules.json')
    phones = FileIO.load_phones('JSON/phones.json')
    questions = FileIO.load_questions('JSON/questions.json')

    # Store rules in Knowledge Base
    kb.set_rules(rules)

    # set known user values so far
    user.set_user_first_name("Mike")
    user.set_user_last_name("Drakos")

    # set known components for working memory
    wm.set_user(user)
    wm.set_rules(kb.get_rules())
    wm.set_phones(phones)
    wm.set_questions(questions)

    # main process for asking questions
    for question in wm.get_questions():
        print(question.get_question())
        for answer in question.get_possible_answers():
            print(answer)
        user_answer_topic = question.get_topic()
        user_answer_content = input()
        user_answer = Answer(user_answer_topic, user_answer_content)
        user.set_answer(user_answer)

    # infer answer
    infer = InferenceEngine(wm)
    infer.infer()

    # print answer
    print(wm.get_user().get_phone().get_model())
    print(wm.get_user().get_phone().get_cpu())

    # ask if it's right
    print("Is this the phone you wanted? y or n")
    correct_phone = input()
    last_fired_rule = infer.get_fired_rules()[-1]
    if correct_phone == 'y':
        last_fired_rule.set_salience(last_fired_rule.get_salience()+1)
    else:
        print("What phone do you think is a better choice?")
        potential_phones = infer.find_new_rule()
        print(potential_phones)

        # correct_model = input()
        # new_antecedents = last_fired_rule.get_antecedent()
        # new_topic = last_fired_rule.get_topic()
        # new_salience = last_fired_rule.get_salience()+1
        # new_rule = ComplexRule(new_antecedents, correct_model, new_topic, new_salience)
        # wm.add_rule(new_rule)
        # print(new_rule.get_topic(), new_rule.get_antecedent(), new_rule.get_consequent())


    # user.set_answer("Samsung")
    # user.set_answer(">1000")
    # print(user.get_answers())

test_process()
