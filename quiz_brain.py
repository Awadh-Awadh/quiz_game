class QuizBrain:

  def __init__(self, q_list):
    self.question_number = 0
    self.question_list = q_list
    self.score = 0


  def still_has_querries(self):
    return self.question_number < len(self.question_list)
    
  def check_answer(self, user_answer, correct_answer):
      if correct_answer.lower() == user_answer.lower():
        self.score += 1
        print("You got it right")
        print(f"score {self.score}/{self.question_number}")
      else:
        print("that was wrong")
      print(f"The correct anser is {correct_answer}")

  def next_question(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    user_input = input(f"Q. {self.question_number}: {current_question.question} (True/False) ")
    self.check_answer(user_input, current_question.answer)


    