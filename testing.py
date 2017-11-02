# This file is for testing while in development!
from FileIO import FileIO
from Components.User import User
from Components.Answer import Answer
from Components.WorkingMemory import WorkingMemory
from Components.InferenceEngine import InferenceEngine
from Components.KnowledgeBase import KnowledgeBase
from GUI import gui

'''
def test_file_io():
    FileIO.load_rules('JSON/test_rules.json')
    FileIO.load_phones('JSON/phones.json')
    FileIO.load_questions('JSON/test_questions.json')

# test_file_io()


def test_process():
    # create blank user, working memory, and knowledge base
    user = User()
    wm = WorkingMemory()
    kb = KnowledgeBase()

    # Import rules, phones, and questions
    rules = FileIO.load_rules('JSON/test_rules.json')
    phones = FileIO.load_phones('JSON/phones.json')
    questions = FileIO.load_questions('JSON/test_questions.json')

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

    # user.set_answer("Samsung")
    # user.set_answer(">1000")
    # print(user.get_answers())

test_process()
'''

def main():
    gui.Window

main()
