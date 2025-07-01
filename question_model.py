class Question:
    def __init__(self,text,answer):
        self.text=text
        self.answer=answer

new_qstn=Question("Are you an adult","True")
print(new_qstn.text)
print(new_qstn.answer)
