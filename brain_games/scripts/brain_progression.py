import random
from brain_games.games.games_logic import start_game


def generate_progression(start, length, step):
    return [str(start + i * step) for i in range(length)]


def generate_round():
    progression_length = random.randint(5, 10)
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    progression = generate_progression(start, progression_length, step)

    hidden_element_index = random.randint(0, progression_length - 1)
    correct_answer = progression[hidden_element_index]
    progression[hidden_element_index] = '..'

    question = ' '.join(progression)
    instruction = "What number is missing in the progression?"
    return question, correct_answer, instruction


def main():
    start_game(generate_round)


if __name__ == "__main__":
    main()
