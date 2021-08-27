def check_guess(guess, answer):
    global score
    # initialize still_guessing, and attempt
    still_guessing_the_same_question = True
    attempt = 1
    # while loop
    while still_guessing_the_same_question and attempt < 3:
        # correct answer
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score += 1
            still_guessing_the_same_question = False
        # wrong answer for first and second times
        else:
            if attempt < 3:
                guess = input("Sorry, wrong answer! Please try again!")
                attempt += 1
    # return correct answer if attempt reaches 3
    if attempt == 3:
        print("The correct answer is ", answer)

# initialize score
score = 0
print("Guess the Animal")
guess1 = input("Which bear lives at the North Pole? ")
check_guess(guess1, "Polar bear")
guess2 = input("Which is the fastest land animal? ")
check_guess(guess2, "Cheetah")
guess3 = input("Which is the largest animal? ")
check_guess(guess3, "Blue whale")
print("Your score is " + str(score))
