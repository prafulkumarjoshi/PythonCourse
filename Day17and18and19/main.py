import question_model , data, quiz_brain

list_of_questions = []
score = 0

for question in data.question_data:
    print(question["text"])
    print(question["answer"])
    list_of_questions.append(question_model.Question(question["text"], question["answer"]))

quiz = quiz_brain.QuizzBrain(list_of_questions)  

while quiz.still_has_questions():
    user_answer = quiz.next_question()
    correct_answer = (quiz.question_list[quiz.question_number-1]).answer
    if quiz.check_answer(user_answer, correct_answer):
        score += 1

print("Score: ", score)
    