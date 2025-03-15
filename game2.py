import random


def generate_progression(start, step, length):
    """Генерирует геометрическую прогрессию."""
    return [start * (step ** i) for i in range(length)]


def hide_element(progression):
    """Скрывает случайный элемент прогрессии."""
    hidden_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    return progression, correct_answer


def play_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    correct_answers_needed = 3
    correct_answers = 0

    while correct_answers < correct_answers_needed:
        start = random.randint(1, 10)
        step = random.randint(2, 5)
        length = random.randint(5, 10)
        progression = generate_progression(start, step, length)
        progression, correct_answer = hide_element(progression)

        print("Question:", " ".join(map(str, progression)))
        user_answer = int(input("Your answer: "))

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_game()