import math


TASK = 1 # сюда пишіть номер завдання


def task_one():
    try:
        num = int(input("Введіть ціле число: "))
    except ValueError:
        raise ValueError("Введене значення має бути цілим числом") from None
    else:
        if num % 2 == 0:
            print(f"Число '{num}' - парне")
        else:
            print(f"Число '{num}' - непарне")

    print("===========================")

    try:
        age = int(input("Введіть Ваш вік: "))
    except ValueError:
        raise ValueError("Введене значення має бути цілим числом") from None
    else:
        if age >= 18:
           print("Ви повнолітній")
        elif age < 0:
            raise ValueError("Вік повинен бути не від'ємним")
        else:
            print("Ви не повнолітній")

    print("===========================")

    try:
        r = float(input("Введіть радіус кола: "))
    except ValueError:
        raise ValueError("Введене значення має бути цілим або дробовим числом") from None
    else:
        if r < 0:
            raise ValueError("Радіус повинен бути додатнім")

        l = 2 * r * math.pi
        s = r**2 * math.pi

        print(f"Довжина кола: {l:.2f}", f"Площа круга: {s:.2f}", sep=" | ")

    print("===========================")

    num = input("Введіть 2 числа через пробіл: ")

    num_splitted = num.split()

    if len(num_splitted) != 2:
        raise ValueError("Ви ввели некоректну кількість чисел")
    else:
        try:
            formatted_num = list(map(float, num.split()))
        except ValueError:
            raise ValueError("Введені значення мають бути числами") from None
        else:
            print("Найбільше число: ", max(formatted_num))


def task_two():
    parts = input("Введіть координати точки (x y) через пробіл: ").split()

    if len(parts) != 2:
        raise ValueError("Ви ввели некоректну кількість чисел")

    try:
        x, y = float(parts[0]), float(parts[1])
    except ValueError:
        raise ValueError("Введені значення мають бути числами") from None

    if x == 0 and y == 0:
        print("Точка знаходиться на початку координат")
    elif x == 0:
        print("Точка лежить на осі OY")
    elif y == 0:
        print("Точка лежить на осі OX")
    elif x > 0 and y > 0:
        print("Точка належить I чверті")
    elif x < 0 and y > 0:
        print("Точка належить II чверті")
    elif x < 0 and y < 0:
        print("Точка належить III чверті")
    else:
        print("Точка належить IV чверті")


def task_three():
    try:
        age = int(input("Введіть вік: "))
    except ValueError:
        raise ValueError("Введене значення має бути цілим числом") from None

    if age < 0 or age > 120:
        raise ValueError("Вік має бути в межах від 0 до 120")

    if 11 <= age % 100 <= 14:
        word = "років"
    elif age % 10 == 1:
        word = "рік"
    elif 2 <= age % 10 <= 4:
        word = "роки"
    else:
        word = "років"

    print(f"{age} {word}")


def task_four():
    try:
        n = int(input("Введіть N (кількість поїздок): "))
        k = int(input("Введіть k (кількість квитків у пачці): "))
        p1 = int(input("Введіть p1 (ціна одного квитка): "))
        p2 = int(input("Введіть p2 (ціна пачки): "))
    except ValueError:
        raise ValueError("Введені значення мають бути цілими числами") from None

    for value in (n, k, p1, p2):
        if value <= 0 or value > 10000:
            raise ValueError("Усі величини мають бути в межах від 1 до 10000")

    packs, rest = divmod(n, k)

    only_single = n * p1
    packs_and_singles = packs * p2 + rest * p1
    only_packs = (packs + 1) * p2 if rest else packs * p2

    print(min(only_single, packs_and_singles, only_packs))


if __name__ == '__main__':
    if TASK == 1:
        task_one()
    elif TASK == 2:
        task_two()
    elif TASK == 3:
        task_three()
    elif TASK == 4:
        task_four()
    else:
        raise TypeError("Введено неправильний номер завдання")


