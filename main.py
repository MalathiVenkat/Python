from tkinter import *

Question = ["Which of the following testing is also known as white -box testing ?",
            "Testing Must be Planned is stated in"

            ]
options = [["Structural Testing",
            "Error guessing technique",
            "Design based testing",
            "none of the above"],
           ["Bill hetzel principle",
            "Ed Kit principle",
            "IEEE 829",
            "IEEE 8295"]]
Answer = [1, 1]

Score = 0
Total_No_Question = 2
Question_no = 1


def next():
    global Score, Question_no
    if val1.get() == 1:
        selected_option = 1
    elif val2.get() == 1:
        selected_option = 2
    else:
        selected_option = -1

    if Answer[Question_no - 1] == selected_option:
        Score += 1
    else:
        pass

    Question_no += 1

    if Question_no > Total_No_Question:
        root.pack_forget()
        Score.place(relx=.40, rely=.40)
        Score.config(text="Score:" + str(Score))
    else:
        val1.set(0)
        val2.set(0)
        val3.set(0)
        Question.config(text=Question[Question_no - 1])
        option1.config(text=options[Question_no - 1][0])
        option2.config(text=options[Question_no - 1][1])
        option3.config(text=options[Question_no - 1][2])


def check(option):
    if option == 1:
        val2.set(0)
        val3.set(0)
    elif option == 1:
        val2.set(0)
        val3.set(0)


Win = Tk()
Win.title("Quiz Game")

root = Frame()
root.pack()

Question = Label(root, width=60, font=20, text=Question[0])
Question.pack()

val1 = IntVar()
val2 = IntVar()
val3 = IntVar()

option1 = Checkbutton(root, variable=val1, text=options[0][0], command=lambda: check(1))
option1.pack()

option2 = Checkbutton(root, variable=val2, text=options[0][1], command=lambda: check(2))
option2.pack()

option3 = Checkbutton(root, variable=val3, text=options[0][2], command=lambda: check(3))
option3.pack()

next_b = Button(root, text="Next", command=next)
next_b.pack()

Score = Label(Win)
Score.place_forget()

Win.mainloop()
