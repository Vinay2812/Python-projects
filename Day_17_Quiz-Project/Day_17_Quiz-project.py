from Day_17_data import question_data
from Day_17_question_model import Question
from Day_17_quiz_brain import QuizBrain
import random

question_bank = []
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

random.shuffle(question_bank)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is : {quiz.score}/{quiz.question_num}")
