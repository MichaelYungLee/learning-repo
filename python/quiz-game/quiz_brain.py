class QuizBrain():
    def __init__(self, question_bank) -> None:
        self.question_bank = question_bank
        self.question_num = 0
        self.score = 0

    def next_question(self):
        question = self.question_bank[self.question_num]
        self.question_num += 1
        answer = input(f'Q.{self.question_num}: {question.text} (True/False)?: ')
        self.check_answer(answer, question.answer)

    def still_has_questions(self):
        return len(self.question_bank) > self.question_num

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            self.score += 1
            print('You got it right!')
        else:
            print("That's wrong.")
        print(f'The correct answer was: {question_answer}.')
        print(f"Your current score is: {self.score}/{self.question_num}\n")
        