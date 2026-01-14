class QuizzBrain:
    def __init__(self, question_list):
        print("New QuizzBrain is being created")
        self.question_number = 0
        self.question_list = question_list
        
    def next_question(self):
        curr_question = self.question_list[self.question_number]
        user_answer = input(curr_question.text)
        self.question_number += 1
        return user_answer
    
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False    
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            return True
        else:
            return False 