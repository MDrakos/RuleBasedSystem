from tkinter import *
import tkinter as tk
from tkinter import messagebox
from FileIO import FileIO
from Components.User import User
from Components.Answer import Answer
from Components.WorkingMemory import WorkingMemory
from Components.InferenceEngine import InferenceEngine
from Components.KnowledgeBase import KnowledgeBase


class Window:
    def __init__(self, master):
        self.user = User()
        self.wm = WorkingMemory()
        self.rules = FileIO.load_rules('JSON/test_rules.json')
        self.phones = FileIO.load_phones('JSON/phones.json')
        self.questions = FileIO.load_questions('JSON/test_questions.json')

        self.wm.set_user(self.user)
        self.wm.set_rules(self.rules)
        self.wm.set_phones(self.phones)
        self.wm.set_questions(self.questions)

        Label(master, text="Type your First Name").grid(row=1,column=0)
        Label(master, text="Type your Last Name").grid(row=2,column=0)

        self.e1 = Entry(master)
        self.e2 = Entry(master)

        self.e1.grid(row=1, column=2)
        self.e2.grid(row=2, column=2)

        self.bbutton = Button(root, text="Display Questions", command=self.display_questions)
        self.bbutton.grid(row=3, column=1)

    def display_questions(self):
        self.user.set_user_first_name(self.e1.get())
        self.user.set_user_last_name(self.e2.get())
        print(self.user)
        window = tk.Toplevel(root)
        window.minsize(width=666, height=666)
        window.maxsize(width=666, height=666)
        if self.wm.get_questions():
            self.vars = {}
            for question in self.wm.get_questions():
                question_label = Label(window, text=question.get_question())
                question_label.pack()
                answers = question.get_possible_answers()

                for answer in answers:
                    # print(answer)
                    var = IntVar()
                    self.vars[(question.get_topic(), answer)] = var
                    check = Checkbutton(window, text=answer, variable=var)
                    check.pack()

        submit = Button(window, text='Submit', command=self.set_answer)
        submit.pack()

    def check_states(self):
        for var in self.vars:
            print(self.vars.get(var).get())

    def set_answer(self):
        for var in self.vars:
            if self.vars.get(var).get():
                user = self.wm.get_user()
                user_topic = var[0]
                user_answer = var[1]
                ans = Answer(user_topic, user_answer)
                user.set_answer(ans)
                print(user_topic, user_answer)
        messagebox.showinfo('Result', user.get_answers())
        #print(user.get_answers())

root = Tk()
root.title("Cellphone selector")
window = Window(root)
root.mainloop()
