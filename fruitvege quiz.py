Questions = ["What is an apple?", "What is a Cabbage?", "What is a mango?", "What is a cucumber?", "What is a tomato?"]
Answer = ["a", "b", "c"]
Choices = ["a. Fruit", "b. Vegetable", "c. Both"]
question_answers = ["a", "b", "a", "c", "c"]
keep_going = "y"

# runs the introduction of the quiz
def introduction():
    name = input("What is your name? ") # takes input to use for answer feedback
    print()
    print("Welcome, {}. In this multi choice quiz, you will have to answer five questions by typing in either a, b or c as the answer. Enjoy the quiz!".format(name))
    print()
    print()
    input("Press enter to start.")
    print("--------------------------------------------------------------------------------")
    print()
    return name

# prints the questions and choices    
def questionoutput(number):
    print("***********************************Question {}***********************************".format(number+1))
    print()
    print(Questions[number])
    for i in range(len(Choices)):
        print(Choices[i])
    print()

# checks if the user has entered a valid answer
def answer_is_valid(answer):
    while answer != "a" and answer != "b" and answer != "c": # makes the user re-enter an answer if not valid
            print("Not a valid answer! Please input a, b, or c.")
            answer = input("Your Answer: ")
    return answer

# checks if the user's answer is correct
def check_answer(answer, number):
    if answer == question_answers[number]:
        return True
    else:
        return False

# calculates the user's final score and gives feedback
def calculate_total_score(score):
    if score == 5:
        print("Amazing, {}! You got a perfect 5 out of 5!".format(name))

    elif score >= 2:
        print("Well done, {}. You got {} out of 5.".format(name, score))

    else:
        print("Oh dear, {}. You got {} out of 5. Maybe try again?".format(name, score))

# main quiz loop
while keep_going == 'y':
    score = 0
    question_num = 0
    name = introduction()
    for i in range(len(Questions)):
        questionoutput(question_num)
        user_answer = input("Your Answer: ")
        user_answer = answer_is_valid(user_answer)
        print()
        if check_answer(user_answer, question_num) == True:
            print("That is correct {}! :D".format(name))
            score += 1
        else:
            print("That was incorrect {} :(".format(name))
        question_num += 1
        print()
    print()
    print("--------------------------------------------------------------------------------")
    print()
    calculate_total_score(score)
    print()
    keep_going = input("Please type in 'y' to replay the quiz or type in anything else and enter to quit. ") # if the user enters 'y' then cut the quiz loop and end the program
    print()
print("Thank you for Playing.")
