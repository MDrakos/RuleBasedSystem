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

        rules = FileIO.load_rules('JSON/test_rules.json')
        phones = FileIO.load_phones('JSON/phones.json')
        questions = FileIO.load_questions('JSON/test_questions.json')

        FileIO.load_rules('JSON/test_rules.json')
        FileIO.load_phones('JSON/phones.json')
        FileIO.load_questions('JSON/test_questions.json')



        user = User("Mike", "Drakos")

        for question in questions:
            get_q = question.get_question()
            w = Label(master, text=get_q)
            w.pack()

            for answer in question.get_possible_answers():
                self.var = IntVar()
                check = Checkbutton(master, text=answer, variable=self.var,command=self.cb)
                check.pack()
                print(answer)
                #print(is_checked.get())

        submit_button = Button(None, text='Submit')
        submit_button.pack()

    def cb(self):
        print ("variable is", self.var.get())

root = Tk()
app = App(root)
root.title("Smartphone Selector")
root.mainloop()
