from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
q_bank = []
for item in question_data:
    text = item['question']
    answer = item['correct_answer']
    questions = Question(text, answer)
    q_bank.append(questions)

brain = QuizBrain(q_bank,)
while brain.still_has_questions():
    brain.next_question()


