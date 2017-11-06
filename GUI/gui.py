from tkinter import *
import tkinter as tk
from tkinter import messagebox

import FileIO.FileIO as fileIO
from Components.User import User
from Components.Answer import Answer
from Components.WorkingMemory import WorkingMemory
from Components.InferenceEngine import InferenceEngine
from Components.KnowledgeBase import KnowledgeBase
from Components.ComplexRule import ComplexRule
from Components.Phone import Phone
from PIL import ImageTk, Image

"""GUI to provide user interaction with the Knowledge Based System.
"""


__author__ = "Won"
__version__ = "1.0"


class Window:
    def __init__(self, master):
        # create blank user, working memory, and knowledge base
        self.user = User()
        self.wm = WorkingMemory()
        self.kb = KnowledgeBase()
        self.inference_engine = InferenceEngine()
        self.user_result = Phone()
        self.vars = {}
        self.phone_vars = {}
        self.new_rule = ComplexRule()
        self.questions_window = None
        self.results_window = None
        self.update_rule_window = None
        self.rule_addition_window = None
        self.find_rule_window = None
        self.update_salience_window = None
        self.display_specs_window = None

        #puts an image to the GUI
        image = Image.open("my_logo.png")
        photo = ImageTk.PhotoImage(image)
        label = Label(image=photo)
        label.image = photo  # keep a reference!
        label.grid(row=0, column=2)

        #Asking questions to enter the user's name
        first_name_label = Label(master, text="Enter first name").grid(row=1, column=1)
        self.first_name = Entry(master).grid(row=1, column=2)
        last_name_label = Label(master, text="Enter last name").grid(row=2, column=1)
        self.last_name = Entry(master).grid(row=2, column=2)

        #Makes a label for the Rules JSON
        self.rules = []
        self.rules_file = " "
        rules_json = Label(master, text="Rules JSON").grid(row=3, column=0)
        bar_placeholder1 = Entry(master, textvariable=self.rules_file).grid(row=3, column=2)

        #Makes a label for the Questions JSON
        self.questions = []
        self.questions_file = " "
        questions_json = Label(master, text="Questions JSON").grid(row=4, column=0)
        bar_placeholder2 = Entry(master, textvariable=self.questions_file).grid(row=4, column=2)

        # Makes a label for the Phones JSON
        self.phones = []
        self.phones_file = " "
        phones_json = Label(master, text="Phones JSON").grid(row=5, column=0)
        bar_placeholder2 = Entry(master, textvariable=self.phones_file).grid(row=5, column=2)

        #Makes the button for the Load rules json file from the browsed file
        self.rules_button = Button(master, text="Load Rules", command=self.load_rules)
        self.rules_button.grid(row=3, column=4)
        self.browse_rules = Button(master, text="Browse", command=self.browse_rules_file)
        self.browse_rules.grid(row=3, column=1)

        #Makes the button for the Load questions json file from the browsed file
        self.questions_button = Button(master, text="Load Questions", command=self.load_questions)
        self.questions_button.grid(row=4, column=4, sticky=W + E)
        self.browse_questions = Button(master, text="Browse", command=self.browse_questions_file)
        self.browse_questions.grid(row=4, column=1)

        #Makes the button for the Load phones json file from the browsed file
        self.phones_button = Button(master, text="Load Phones", command=self.load_phones)
        self.phones_button.grid(row=5, column=4, sticky=W + E)
        self.browse_phones = Button(master, text="Browse", command=self.browse_phones_file)
        self.browse_phones.grid(row=5, column=1)

        #A button that loads all of rules, questions and phones at the same time
        self.load_all_button = Button(master, text="Load all", command=self.load_all)
        self.load_all_button.grid(row=4, column=5, sticky=W + E)

        #A button that calls the display questions that needs to be answered by the user
        self.next_button = Button(master, text="Next", command=self.display_questions)
        self.next_button.grid(row=6, column=2)

    #Function to browse the rule files for the GUI
    def browse_rules_file(self):
        from tkinter.filedialog import askopenfilename
        first_file_path = StringVar()
        first_bar = Entry(root, textvariable=first_file_path)
        first_bar.grid(row=3, column=2)

        Tk().withdraw()
        self.rules_file = askopenfilename()
        first_file_path.set(self.rules_file)

    # Function to browse the question files for the GUI
    def browse_questions_file(self):
        from tkinter.filedialog import askopenfilename
        second_file_path = StringVar()
        second_bar = Entry(root, textvariable=second_file_path)
        second_bar.grid(row=4, column=2)

        Tk().withdraw()
        self.questions_file = askopenfilename()
        second_file_path.set(self.questions_file)

    #Function to browse the phone files
    def browse_phones_file(self):
        from tkinter.filedialog import askopenfilename
        third_file_path = StringVar()
        third_bar = Entry(root, textvariable=third_file_path)
        third_bar.grid(row=5, column=2)

        Tk().withdraw()
        self.phones_file = askopenfilename()
        third_file_path.set(self.phones_file)

    #Function that loads rules to the working memory and knowledge based
    def load_rules(self):
        if self.rules_file:
            self.rules = fileIO.load_rules(self.rules_file)

            # Store rules in Knowledge Base
            self.kb.set_rules(self.rules)
            self.wm.set_rules(self.kb.get_rules())

            # if self.wm.get_rules():
            #     messagebox.showinfo("Load Successful", "Rules file loaded successfully")

    #Function that loads questions to the working memory
    def load_questions(self):
        if self.questions_file:
            self.questions = fileIO.load_questions(self.questions_file)

            # Store questions in Working Memory
            self.wm.set_questions(self.questions)

            # if self.wm.get_rules():
            #     messagebox.showinfo("Load Successful", "Questions file loaded successfully")

    #Function that loads phones to the working memory
    def load_phones(self):
        if self.phones_file:
            self.phones = fileIO.load_phones(self.phones_file)

            # Store phones in Working Memory
            self.wm.set_phones(self.phones)

            # if self.wm.get_rules():
            #     messagebox.showinfo("Load Successful", "Phones file loaded successfully")

    #Fuction that can be use to load all rules, questions and phones at the same time.
    def load_all(self):
        self.load_rules()
        self.load_questions()
        self.load_phones()

        if self.questions_file and self.phones_file and self.rules_file:
            messagebox.showinfo("Success", "All files loaded successfully")

    #A fuction that displays all the questions that needs to be answered from the user
    def display_questions(self):
        if self.user.first_name and self.user.last_name:
            self.user.set_user_first_name(self.first_name.get())
            self.user.set_user_last_name(self.last_name.get())

        #This set the question_window that can be called
        self.questions_window = tk.Toplevel(root)

        #Sets the size of the frame size
        self.questions_window.minsize(width=666, height=666)
        self.questions_window.maxsize(width=666, height=666)

        #From working memory's questions, it will get the possible answer from the user
        if self.wm.get_questions():
            self.vars = {}
            for question in self.wm.get_questions():
                question_label = Label(self.questions_window, text=question.get_question())
                question_label.pack()
                answers = question.get_possible_answers()
                for answer in answers:
                    var = IntVar()
                    self.vars[(question.get_topic(), answer)] = var
                    check = Checkbutton(self.questions_window, text=answer, variable=var)
                    check.pack()

        # A button that calls the function set_answer that get the perfect phone from the user
        submit = Button(self.questions_window, text='Submit', command=self.set_answer)
        submit.pack()

    # This function is to check the function of the
    def check_states(self):
        for var in self.vars:
            print(self.vars.get(var).get())

    # This fucnction sets the answer from the user's selected answer
    def set_answer(self):
        self.questions_window.destroy()
        for var in self.vars:
            if self.vars.get(var).get():
                self.user = self.wm.get_user()
                user_topic = var[0]
                user_answer = var[1]
                ans = Answer(user_topic, user_answer)
                self.user.set_answer(ans)

        # inference engine takes in to work with the working memeory
        self.inference_engine = InferenceEngine(self.wm)
        self.inference_engine.infer()
        self.user_result = self.wm.get_user().get_phone()

        # calls fucntion display result that will be show the perfect smartphone to the user
        self.display_results()

    def display_results(self):
        self.results_window = tk.Toplevel(root)

        # Explanations
        if self.user_result:
            # This will trigger if the selected rules had a perfect matching for the user and shows the phone specification if user wants and ability to add self learning
            phone = self.wm.get_user().get_phone()
            attributes = phone.get_attributes()
            Label(self.results_window, text="Best matched phone: ").pack()
            Label(self.results_window, text=self.user_result.get_model()).pack()
            Label(self.results_window, text="This phone was selected for the following reasons:").pack()
            for answer in self.wm.get_user().get_answers():
                topic = answer.get_topic()
                content = answer.get_content()
                Label(self.results_window, text="For: " + topic).pack()
                Label(self.results_window, text="Your answer was " + content).pack()
                Label(self.results_window, text="For this phone: " + topic + " is " + attributes[topic]).pack()

            Label(self.results_window, text="Is this the phone you expected?").pack()
            self.bbutton = Button(self.results_window, text="Yes", command=self.update_salience)
            self.bbutton.pack()
            self.bbutton = Button(self.results_window, text="No", command=self.rule_addition_query)
            self.bbutton.pack()
            self.bbutton = Button(self.results_window, text="See phone specifications", command=self.display_specs)
            self.bbutton.pack()
        else:
            # This will be triggerd if the selected rules didn't have the resulting phone that will lead to self learning
            Label(self.results_window, text="Uh oh. I couldn't find a phone").pack()
            self.bbutton = Button(self.results_window, text="Let me try to find a rule?", command=self.find_rule)
            self.bbutton.pack()
            self.bbutton = Button(self.results_window, text="Add rule manually?", command=self.update_rule)
            self.bbutton.pack()
            self.bbutton = Button(self.results_window, text="Quit", command=exit)
            self.bbutton.pack()
            self.bbutton = Button(self.results_window, text="Retry", command=self.try_again)
            self.bbutton.pack()

    # This function that will update the salience
    def update_salience(self):
        last_fired_rule = self.inference_engine.get_fired_rules()[-1]
        last_fired_rule.set_salience(last_fired_rule.get_salience()+1)
        messagebox.showinfo("Thanks", "Great! Thank you :)")

        self.try_again_messagebox()

    # A function that can be used to display all the phone specification
    def display_specs(self):
        self.results_window.destroy()
        self.display_specs_window = tk.Toplevel(root)
        phone = self.wm.get_user().get_phone()
        print(phone)
        phone_attributes = phone.get_attributes()
        for attribute in phone_attributes:
            Label(self.display_specs_window, text=attribute + ": " + phone_attributes[attribute]).pack()

        Button(self.display_specs_window, text="Done", command=self.try_again_messagebox).pack()

    # This function will add rule to the query using the button. Program can add rules by itself too.
    def rule_addition_query(self):
        self.results_window.destroy()
        self.rule_addition_window = tk.Toplevel(root)
        question = Label(self.rule_addition_window, text="Let me try to add a rule?")
        question.pack()

        self.bbutton = Button(self.rule_addition_window, text="Yes", command=self.find_rule)
        self.bbutton.pack()
        self.bbutton = Button(self.rule_addition_window, text="No", command=self.update_rule)
        self.bbutton.pack()
        self.bbutton = Button(self.rule_addition_window, text="Quit", command=exit)
        self.bbutton.pack()

    # This function will find the rules
    def find_rule(self):
        if self.rule_addition_window:
            self.rule_addition_window.destroy()
        if self.results_window:
            self.results_window.destroy()
        self.find_rule_window = tk.Toplevel(root)
        self.new_rule = self.inference_engine.find_new_rule()

        if self.new_rule:
            Label(self.find_rule_window, text="How about this rule?").pack()
            new_rule_antecedents_text = self.new_rule.get_antecedent()
            Label(self.find_rule_window, text="Antecedents: ").pack()
            for antecedent in new_rule_antecedents_text:
                Label(self.find_rule_window, text="topic: " + antecedent + ", content: " +
                                                  new_rule_antecedents_text[antecedent]).pack()

            Label(self.find_rule_window, text="Consequent: ").pack()
            new_rule_consequents_text = self.new_rule.get_consequent()
            Label(self.find_rule_window, text=new_rule_consequents_text).pack()

            #Buttons that will add new set of rules or not
            self.bbutton = Button(self.find_rule_window, text="Add", command=self.add_new_rule)
            self.bbutton.pack()
            self.bbutton = Button(self.find_rule_window, text="Don't Add", command=self.update_rule)
            self.bbutton.pack()
        else:
            #Buttons that will add rules manurally or not
            Label(self.find_rule_window, text="Couldn't find new rule").pack()
            self.bbutton = Button(self.find_rule_window, text="Add rule manually?", command=self.update_rule)
            self.bbutton.pack()
            self.bbutton = Button(self.find_rule_window, text="Quit", command=exit)
            self.bbutton.pack()

    # This function updates the rules if the user wants to change the resulting answer
    def update_rule(self):
        if self.rule_addition_window:
            self.rule_addition_window.destroy()
        if self.results_window:
            self.results_window.destroy()
        if self.find_rule_window:
            self.find_rule_window.destroy()
        self.update_rule_window = tk.Toplevel(root)
        question = Label(self.update_rule_window, text="What phone do you think is a good choice?")
        question.pack()
        self.phone_vars = {}
        for phone in self.phones:
            var = IntVar()
            phone_model = phone.get_model()
            self.phone_vars[phone.get_model()] = var
            check = Checkbutton(self.update_rule_window, text=phone_model, variable=var)
            check.pack()

        submit = Button(self.update_rule_window, text='Submit', command=self.set_new_rule)
        submit.pack()

    # This function sets the new rules to the program that is part of self learning
    def set_new_rule(self):
        # If a complex rule fired and was wrong, need to correct it.
        last_fired_rule = self.inference_engine.get_fired_rules()[-1]
        if last_fired_rule:
            new_rule = ComplexRule()
            for var in self.phone_vars:
                if self.phone_vars.get(var).get():
                    new_antecedents = last_fired_rule.get_antecedent()
                    new_topic = last_fired_rule.get_topic()
                    new_salience = last_fired_rule.get_salience() + 1
                    new_rule = ComplexRule(new_antecedents, var, new_topic, new_salience)
                    for rule in self.wm.get_rules():
                        if isinstance(rule.get_antecedent(), dict):
                            if new_rule.get_antecedent().items() == rule.get_antecedent().items() and \
                                    new_rule.get_consequent() == rule.get_consequent() and \
                                    new_rule.get_topic() == rule.get_topic():
                                messagebox.showinfo("Already Exists", "This rule already exists")
                                self.try_again_messagebox()
                                return 0

            self.wm.add_rule(new_rule)
            self.rules = self.wm.get_rules()
            self.inference_engine.set_working_memory(self.wm)
            messagebox.showinfo("New Rule", "New rule created for " + new_rule.get_consequent())
            self.try_again_messagebox()
        else:
            # No complex rule fired, need to create a new one
            new_rule = ComplexRule()
            for phone_var in self.phone_vars:
                new_antecedents = {}
                if self.phone_vars.get(phone_var).get():
                    for var in self.vars:
                        if self.vars.get(var).get():
                            for rule in self.rules:
                                if var[1] in rule.get_antecedent():
                                    new_antecedents[var[0]] = rule.get_consequent()
                    new_topic = "phone"
                    new_salience = 1
                    new_rule = ComplexRule(new_antecedents, phone_var, new_topic, new_salience)
                    self.wm.add_rule(new_rule)
                    self.rules = self.wm.get_rules()
                    self.inference_engine.set_working_memory(self.wm)

            messagebox.showinfo("New Rule", "New rule created for " + new_rule.get_consequent())
            self.try_again_messagebox()

    # This funcgtion adds new rules to the program
    def add_new_rule(self):
        self.wm.add_rule(self.new_rule)
        self.rules = self.wm.get_rules()
        self.inference_engine.set_working_memory(self.wm)
        messagebox.showinfo("New Rule", "Added new rule")
        self.try_again_messagebox()

    def try_again_messagebox(self):
        try_again = messagebox.askretrycancel("Retry", "Try again?")
        if try_again:
            self.try_again()
        else:
            quit(0)

    # A function that is for trying again to do the GUI starting from the beginning
    def try_again(self):
        if self.update_salience_window:
            self.update_salience_window.destroy()
        if self.rule_addition_window:
            self.rule_addition_window.destroy()
        if self.results_window:
            self.results_window.destroy()
        if self.find_rule_window:
            self.find_rule_window.destroy()
        if self.questions_window:
            self.questions_window.destroy()
        if self.update_rule_window:
            self.update_rule_window.destroy()

        # Reset User attributes
        self.user.set_answers([])
        self.user.set_attributes({})
        self.inference_engine.set_working_memory(self.wm)
        self.display_questions()


root = Tk()
# Makes title to be cellphone selector
root.title("Cellphone selector")
window = Window(root)
name_start = Window(root)
self_start = Window(root)
self_learn = Window(root)
root.mainloop()
