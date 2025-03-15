import random
from math import gcd


def compute_lcm(x, y):
    
    return x * y // gcd(x, y)


def compute_lcm_three(a, b, c):
    
    return compute_lcm(compute_lcm(a, b), c)


GAME_DESCRIPTION = "Find the smallest common multiple of given numbers."


def generate_round():
    
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    num3 = random.randint(1, 20)
    question = f"{num1} {num2} {num3}"
    correct_answer = str(compute_lcm_three(num1, num2, num3))
    return question, correct_answer