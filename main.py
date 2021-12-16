from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
  question_text = item['question']
  question_answer =  item['correct_answer']
  new_question = Question(question_text, question_answer)
  question_bank.append(new_question)

  query = QuizBrain(question_bank)

while query.still_has_querries():
  query.next_question()


print("You have come to the end of the quiz")
print(f"Your final score is {query.score}/{len(question_bank)}")