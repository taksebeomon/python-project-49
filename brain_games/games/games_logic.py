import prompt


def start_game(generate_round):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    _, _, instruction = generate_round()
    print(instruction)

    for _ in range(3):
        question, correct_answer, _ = generate_round()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'"
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
