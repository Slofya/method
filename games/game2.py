import random

GAME_DESCRIPTION = "What number is missing in the progression?"


def generate_progression(start, step, length):
    """
    Генерирует геометрическую прогрессию.
    """
    return [start * (step ** i) for i in range(length)]


def generate_round():
    """
    Генерирует вопрос и правильный ответ для игры "Геометрическая прогрессия".
    """
    start = random.randint(1, 10)
    step = random.randint(2, 5)
    length = random.randint(5, 10)
    progression = generate_progression(start, step, length)
    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."
    question = " ".join(map(str, progression))
    return question, correct_answer