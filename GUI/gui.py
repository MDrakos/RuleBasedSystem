from tkinter import *
import tkinter as tk

import FileIO.FileIO as fileIO
from Components.User import User
from Components.Answer import Answer
from Components.WorkingMemory import WorkingMemory
from Components.InferenceEngine import InferenceEngine
from Components.KnowledgeBase import KnowledgeBase


class Window:
    def __init__(self, master):
        # create blank user, working memory, and knowledge base
        self.user = User()
        self.wm = WorkingMemory()
        self.kb = KnowledgeBase()

        self.rules = []
        self.rules_file = " "
        rules_json = Label(root, text="Rules JSON").grid(row=1, column=0)
        bar_placeholder1 = Entry(master, textvariable=self.rules_file).grid(row=1, column=2)

        self.questions = []
        self.questions_file = " "
        questions_json = Label(root, text="Questions JSON").grid(row=2, column=0)
        bar_placeholder2 = Entry(master, textvariable=self.questions_file).grid(row=2, column=2)

        self.phones = []
        self.phones_file = " "
        phones_json = Label(root, text="Phones JSON").grid(row=3, column=0)
        bar_placeholder2 = Entry(master, textvariable=self.phones_file).grid(row=3, column=2)

        # First file buttons
        self.cbutton = Button(root, text="Load Rules", command=self.load_rules)
        self.cbutton.grid(row=1, column=4, sticky=W + E)
        self.bbutton = Button(root, text="Browse", command=self.browse_rules_file)
        self.bbutton.grid(row=1, column=1)

        self.cbutton = Button(root, text="Load Questions", command=self.load_questions)
        self.cbutton.grid(row=2, column=4, sticky=W + E)
        self.bbutton = Button(root, text="Browse", command=self.browse_questions_file)
        self.bbutton.grid(row=2, column=1)

        self.cbutton = Button(root, text="Load Phones", command=self.load_phones)
        self.cbutton.grid(row=3, column=4, sticky=W + E)
        self.bbutton = Button(root, text="Browse", command=self.browse_phones_file)
        self.bbutton.grid(row=3, column=1)

        Label(master, text="Type your First Name").grid(row=4,column=0)
        Label(master, text="Type your Last Name").grid(row=5,column=0)

        self.e1 = Entry(master)
        self.e2 = Entry(master)

        self.e1.grid(row=4, column=2)
        self.e2.grid(row=5, column=2)

        self.bbutton = Button(root, text="Display Questions", command=self.display_questions)
        self.bbutton.grid(row=2, column=5)

    def browse_rules_file(self):
        from tkinter.filedialog import askopenfilename
        first_file_path = StringVar()
        first_bar = Entry(root, textvariable=first_file_path)
        first_bar.grid(row=1, column=2)

        Tk().withdraw()
        self.rules_file = askopenfilename()
        first_file_path.set(self.rules_file)

    def browse_questions_file(self):
        from tkinter.filedialog import askopenfilename
        second_file_path = StringVar()
        second_bar = Entry(root, textvariable=second_file_path)
        second_bar.grid(row=2, column=2)

        Tk().withdraw()
        self.questions_file = askopenfilename()
        second_file_path.set(self.questions_file)

    def browse_phones_file(self):
        from tkinter.filedialog import askopenfilename
        third_file_path = StringVar()
        third_bar = Entry(root, textvariable=third_file_path)
        third_bar.grid(row=3, column=2)

        Tk().withdraw()
        self.phones_file = askopenfilename()
        third_file_path.set(self.phones_file)

    def load_rules(self):
        if self.rules_file:
            self.rules = fileIO.load_rules(self.rules_file)
            # print(rules)

            # Store rules in Knowledge Base
            self.kb.set_rules(self.rules)
            self.wm.set_rules(self.kb.get_rules())

    def load_questions(self):
        if self.questions_file:
            self.questions = fileIO.load_questions(self.questions_file)
            # print(questions)

            self.wm.set_questions(self.questions)

    def load_phones(self):
        if self.phones_file:
            self.phones = fileIO.load_questions(self.phones_file)
            # print(self.phones)

            self.wm.set_phones(self.phones)

    def display_questions(self):
        self.user.set_user_first_name(self.e1.get())
        self.user.set_user_last_name(self.e2.get())
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

        print(user.get_answers())

root = Tk()
root.title("Cellphone selector")
window = Window(root)
root.mainloop()
