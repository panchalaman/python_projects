class QuizBrain:
    def __init__(self, q_bank):
        self.question_number = 0
        self.q_bank = q_bank
        self.score = 0
    def still_has_questions(self):
        if self.question_number < len(self.q_bank):
            return True
        else:
            print("You have completed the quiz")
            print(f"You final score is: {self.score}/{self.question_number} ")

    def next_question(self):
        current_q = self.q_bank[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number}. {current_q.text} (True / False): ").title()
        self.check_answer(user_input, current_q.answer)
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("You got it right!")
        else:
            print(f"Incorrect answer! Correct answer is {correct_answer}")
        print(f"Current score: {self.score}/{self.question_number}")
        print("\n")