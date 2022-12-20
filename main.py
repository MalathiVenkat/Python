name = input("What is your name?")
name = name.title()
print("""Hello {}, welcome to  Quiz! 
Good luck!""".format(name))
from PyPDF2 import PdfFileReader, PdfFileWriter

file_path = 'C:/Users/2081139/Downloads/quizq.pdf'
pdf = PdfFileReader(file_path)

with open('questions.txt', 'w' ) as f:
    for page_num in range(pdf.numPages):

        pageObj = pdf.getPage(page_num)

        try:
            txt = pageObj.extractText()
            print(''.center(100, '-'))
        except:
            pass
        else:

            f.write(txt)
    f.close()
with open('questions.txt', 'r') as quesfile, open ('options.txt') as optfile, open('answers.txt', 'r')as ansfile:
    questions = [question.strip() for question in quesfile.readlines()]
    options = [option.strip() for option in optfile.readlines()]
    answers = [answer.strip() for answer in ansfile.readlines()]

    score = 0

    for question, option, answer in zip(questions, options, answers):
        print(question)
        print(option)
        user_ans = input()
        if user_ans.lower() == answer.lower():
            print("correct!")
            score += 1
        else:
            print("incorrect")

    print(f"Final Score: {score} / {len(questions)}".center(100))

    print("You answered", score, "correct!")
    if score < 4:
        print("aww have a better luck next time")
    elif 4 <= score <= 6:
        print("Good job!", name, 'you done well')
    elif 6 < score <= 8:
        print("Wow you done very good", name, "!")
    elif 8 < score <= 9:
        print("That so crazy, are you a genius?", name)
    elif score <= 10:
        print("Wow", name, " you are a genius!")

    summary_score = (str(("Name:", name, "gets", score, "out of 10 marks")))
    Report = open("Report.txt", 'a')
    Report.write(summary_score + '\n')
    Report.close()