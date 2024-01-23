import random
import prompt


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name, dorogusha? ')
    print(f"Hello, {name}!")
    print(
        'Answer "yes" if the number is even '
        '(i mean, if it divides by 2 without tails, dorogusha), '
        'otherwise answer "no"'
    )

    for _ in range(3):
        rand_numb = random.randint(1, 100)
        print(f'Question: {rand_numb}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = 'yes'if rand_numb % 2 == 0 else 'no'

        if user_answer != correct_answer:
            print(
                f"Sorry, but '{user_answer}' is wrong answer, dorogusha. "
                f"Correct answer was '{correct_answer}'"
            )
            print(
                f"Don't be upset, dorogusha! "
                f"Start the game and let's try again, {name}!"
            )
            return
        else:
            print('Correct, dorogusha!')

    print(f"Congratulations, {name}")


if __name__ == "__main__":
    main()
