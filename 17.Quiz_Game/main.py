from quiz_brain import QuizBrain
from data import question_bank
from question_model import Question

question_obj_list = []
for item in question_bank:
    ques = item["question"]
    ans = item["answer"]
    obj = Question(ques,ans)
    question_obj_list.append(obj)

quiz = QuizBrain(question_obj_list)
while quiz.still_has_questions()==True:
    quiz.next_question()

# print(question_obj_list)
