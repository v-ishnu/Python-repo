# Create a quiz application that asks the user multiple-choice questions and keeps track of the score. Provide feedback on each question and display the final score at the end.

# print('Q1. What is the scientific name of Human?')
# Option= "A", "B", "C", "D"
# print("A. Homo sapiens", "\n""B. Canis lupus familiaris", "\n""C. Hominoidea")

# Answer = input('Choose Correct Option:')

# if (Answer == "A"):
#     print("Wow!! You'r right")
# else:
#     print('your answer is wrong')
    
    
    
# Other Method

# Quiz data (replace with your questions, options, and answers)
question1 = "What is the capital of France?"
option1a = "Paris"
option1b = "London"
option1c = "Berlin"
option1d = "Madrid"
answer1 = "A"

question2 = "Which planet is closest to the Sun?"
option2a = "Venus"
option2b = "Mercury"
option2c = "Mars"
option2d = "Earth"
answer2 = "B"

question3 = "What is the largest mammal on Earth?"
option3a = "Elephant"
option3b = "Blue Whale"
option3c = "Giraffe"
option3d = "Tiger"
answer3 = "B"

# Initialize variables
question_number = 1
score = 0

while question_number <= 3:
    print(f"Question {question_number}.{question1 if question_number == 1 else question2 if question_number == 2 else question3}:")
    print(f" A. {option1a if question_number == 1 else option2a if question_number == 2 else option3a}")
    print(f" B. {option1b if question_number == 1 else option2b if question_number == 2 else option3b}")
    print(f" C. {option1c if question_number == 1 else option2c if question_number == 2 else option3c}")
    print(f" D. {option1d if question_number == 1 else option2d if question_number == 2 else option3d}")
    user_answer = input("Enter your answer (A, B, C, or D): ").upper()
    if question_number == 1 and user_answer == answer1:
        print("Correct!")
        score += 1
    elif question_number == 2 and user_answer == answer2:
        print("Correct!")
        score += 1
    elif question_number == 3 and user_answer == answer3:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")
    question_number += 1

print("\nQuiz complete!")
print(f"Your final score is: {score}/{question_number - 1}")