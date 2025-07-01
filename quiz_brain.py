class QuizBrain:
    def __init__(self,questionlist):
        self.questionno=0
        self.questionlist=questionlist
        self.score=0

    def still_has_qstns(self):
        if self.questionno < len(self.questionlist):
            return True
        else:
            return False

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            print("You got it right!!")
            self.score+=1
        else:
            print("Oopss,You lose it..")
        print("The correct answer is",correct_answer)
        print(f"Your Current Score is {self.score}/{self.questionno}")
        print("\n")



    def next_question(self):
        current_qstn = self.questionlist[self.questionno]
        self.questionno += 1
        user_ans = input(f"Q{self.questionno} {current_qstn.text}[True/False]:\n")
        self.check_answer(user_ans, current_qstn.answer)
