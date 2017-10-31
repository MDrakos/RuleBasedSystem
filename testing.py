# This file is for testing while in development!
from FileIO import FileIO
from Components.User import User
from Components.Answer import Answer
from Components.WorkingMemory import WorkingMemory
from Components.InferenceEngine import InferenceEngine


def test_file_io():
    FileIO.load_rules('JSON/test_rules.json')
    FileIO.load_phones('JSON/phones.json')
    FileIO.load_questions('JSON/test_questions.json')

# test_file_io()


def test_process():
    user = User()
    wm = WorkingMemory()
    rules = FileIO.load_rules('JSON/test_rules.json')
    phones = FileIO.load_phones('JSON/phones.json')
    questions = FileIO.load_questions('JSON/test_questions.json')

    user.set_user_first_name("Mike")
    user.set_user_last_name("Drakos")

    wm.set_user(user)
    wm.set_rules(rules)
    wm.set_phones(phones)
    wm.set_questions(questions)

    for question in wm.get_questions():
        print(question.get_question())
        for answer in question.get_possible_answers():
            print(answer)
        user_answer_topic = question.get_topic()
        user_answer_content = input()
        user_answer = Answer(user_answer_topic, user_answer_content)
        user.set_answer(user_answer)

    infer = InferenceEngine(wm)
    infer.infer()

    # user.set_answer("Samsung")
    # user.set_answer(">1000")
    # print(user.get_answers())

test_process()
