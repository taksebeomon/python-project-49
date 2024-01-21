import random
import prompt
from brain_games.games.games_logic import start_game

def generate_round():
    number1 = random.randint(1, 20)
    number2 = random.randint(1, 20)
    operation = random.choice(['+', '-', '*'])
    
    question = f"{number1} {operation} {number2}"
    if operation == '+':
        correct_answer = str(number1 + number2)
    elif operation == '-':
        correct_answer = str(number1 - number2)
    elif operation == '*':
        correct_answer = str(number1 * number2)

    return question, correct_answer

def main():
    start_game(generate_round)

if __name__ == "__main__":
    main()
