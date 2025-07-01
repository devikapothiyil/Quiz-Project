from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for question in question_data:
    qstn_text=question["text"]
    qstn_answer=question["answer"]
    new_qstn=Question(qstn_text,qstn_answer)
    question_bank.append(new_qstn)


my_question=QuizBrain(question_bank)
while my_question.still_has_qstns():
    my_question.next_question()

print("You have completed the QUIZ !!")
print(f"Your Final Score is {my_question.score}/{my_question.questionno}")
