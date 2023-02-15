quiz = {
    "question1": {
        "question": "what is the capital of France?",
        "answer": "Paris"
    },
     "question2": {
        "question": "what is the capital of England?",
        "answer": "London"
    },
    "question3": {
        "question": "what is the capital of Germany?",
        "answer": "Berlin"
    },
    "question4": {
        "question": "what is the capital of Spain?",
        "answer": "Madrid"
    },
    "question5": {
        "question": "what is the capital of India?",
        "answer": "Delhi"
    },
    "question6": {
        "question": "what is the capital of Turkey?",
        "answer": "Ankara"
    },
    "question7": {
        "question": "what is the capital of Nigeria?",
        "answer": "Lagos"
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input('Answer? ')

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score += 1
        print('Your score is ' + str(score))
        print('')

    else:
        print('Wrong!')
        print('The answer is: ' + value['answer'])
        print('Your score is ' + str(score))
        print('')

print('Your total score is ' + str(score) + ' out of 7')