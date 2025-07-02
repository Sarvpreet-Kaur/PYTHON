class QuizBrain:
    def __init__(self,qlist):
        self.score = 0
        self.quesNo = 0
        self.questionList = qlist

    def next_question(self):
        curr = self.questionList[self.quesNo]
        questext = curr.question
        userAns = input(f"Q.{self.quesNo+1}. {questext} (True/False)? ")
        self.checkAns(userAns, str(curr.answer))
        self.quesNo += 1

    def checkAns(self,userAns,correctAns):
        if userAns==correctAns:
            print("You got it right!")
            self.score +=1
        else:
            print("That's wrong")
        print(f"Correct answer is {correctAns}")
        print(f"Your current score is: {self.score}/{self.quesNo+1}")

    def still_has_questions(self):
        return self.quesNo< len(self.questionList)-1

