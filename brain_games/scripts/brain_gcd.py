import random
from brain_games.games.games_logic import start_game


def find_gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


def generate_round():
    number1 = random.randint(1, 50)
    number2 = random.randint(1, 50)

    question = f"{number1} {number2}"
    correct_answer = str(find_gcd(number1, number2))

    return question, correct_answer


def main():
    start_game(generate_round)


if __name__ == "__main__":
    main()
