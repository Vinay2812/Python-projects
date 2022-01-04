class QuizBrain:
    def __init__(self, question_bank):
        self.question_num = 0
        self.question_bank = question_bank
        self.score = 0

    def still_has_question(self):
        return self.question_num < len(self.question_bank)

    def next_question(self):
        self.user_answer = input(
            f"Q.{self.question_num +1} {self.question_bank[self.question_num].text} (True\False): "
        ).lower()
        self.question_answer = self.question_bank[self.question_num].answer
        if self.check_answer():
            self.score += 1
            print("You got it right!!.")
        else:
            print("That's the wrong answer.")
            print(f"The correct answer was : {self.question_answer}")
        print(f"Your current score : {self.score}/{self.question_num+1}\n")

        self.question_num += 1

    def check_answer(self):
        return self.user_answer[0] == self.question_answer.lower()[0]
