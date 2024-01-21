import prompt

def start_game(generate_round):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name, dorogusha? ')
    print(f"Hello, {name}!")
    
    for _ in range(3):
        question, correct_answer = generate_round()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer == correct_answer:
            print("Correct, dorogusha!")
        else:
            print(f"Sorry, but '{user_answer}' is wrong answer, dorogusha. Correct answer was '{correct_answer}'")
            print(f"Don't be upset, dorogusha! Start the game and let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")