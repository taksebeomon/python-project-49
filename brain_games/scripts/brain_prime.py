import random
from brain_games.games.games_logic import start_game


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_round():
    number = random.randint(1, 100)

    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    instruction = (
        "Answer 'yes' if given number is prime. "
        "Otherwise answer 'no'."
    )

    return question, correct_answer, instruction


def main():
    start_game(generate_round)


if __name__ == "__main__":
    main()
