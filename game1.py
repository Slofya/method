import math
import random


def compute_lcm(x, y):
    """Вычисляет НОК двух чисел."""
    return x * y // math.gcd(x, y)


def compute_lcm_three(a, b, c):
    """Вычисляет НОК трех чисел."""
    return compute_lcm(compute_lcm(a, b), c)


def generate_numbers():
    """Генерирует три случайных числа."""
    return random.randint(1, 20), random.randint(1, 20), random.randint(1, 20)


def play_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the smallest common multiple of given numbers.")

    correct_answers_needed = 3
    correct_answers = 0

    while correct_answers < correct_answers_needed:
        num1, num2, num3 = generate_numbers()
        correct_lcm = compute_lcm_three(num1, num2, num3)

        print(f"Question: {num1} {num2} {num3}")
        user_answer = int(input("Your answer: "))

        if user_answer == correct_lcm:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_lcm}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_game()