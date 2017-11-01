from tkinter import *
from FileIO import FileIO
from Components.User import User
from Components.Answer import Answer
from Components.WorkingMemory import WorkingMemory
from Components.InferenceEngine import InferenceEngine

class App:


    def __init__(self, master):
        #default size of the frame
        master.minsize(width=666, height=666)
        master.maxsize(width=666, height=666)
        frame = Frame(master)
        frame.pack()

        user = User()
        wm = WorkingMemory()
        rules = FileIO.load_rules('JSON/test_rules.json')
        phones = FileIO.load_phones('JSON/phones.json')
        questions = FileIO.load_questions('JSON/test_questions.json')

        FileIO.load_rules('JSON/test_rules.json')
        FileIO.load_phones('JSON/phones.json')
        FileIO.load_questions('JSON/test_questions.json')

        user.set_user_first_name("Mike")
        user.set_user_last_name("Drakos")

        wm.set_user(user)
        wm.set_rules(rules)
        wm.set_phones(phones)
        wm.set_questions(questions)

        for question in questions:
            get_q = question.get_question()
            w = Label(master, text=get_q)
            w.pack()
            possible_ans = question.get_possible_answers()

            for answer in possible_ans:
                self.var = BooleanVar()
                self.ans = answer
                self.check = Checkbutton(master, text=self.ans, var=self.var, onvalue = True, offvalue = False,command=self.cb)
                self.check.pack()
                print(self.var)
                print(self.var.get())

        submit_button = Button(None, text='Submit')
        submit_button.pack()

    def cb(self):
        print (self.var ,"variable is", self.var.get())

root = Tk()
app = App(root)
root.title("Smartphone Selector")
root.mainloop()
