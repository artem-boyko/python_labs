import random
import statistics


def generate_grades(count):
    marks = []

    for _ in range(count):
        marks.append(random.randint(1, 12))

    return marks


def average_grade(grades):
    return statistics.mean(grades)


def get_level(average):
    if average >= 10:
        text = "високий"
    elif average >= 7:
        text = "достатній"
    elif average >= 4:
        text = "середній"
    else:
        text = "початковий"

    return text