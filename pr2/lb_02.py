def task_1():
    num = int(input("Введіть натуральне число: "))

    count = 0
    sum = 0
    for i in range(1, num):
        if i % 3 == 0 or i % 5 == 0:
            count += 1
            sum += i

    print(f"Кількість: {count}")
    print(f"Сума: {sum}")
    print(f"Середнє: {(sum / count):.2f}")


def task_2():
    num = int(input("Введіть натуральне число: "))

    sum = 0
    count = 0
    digit = 0
    max_digit = num % 10
    min_digit = num & 10
    while True:
        count += 1
        digit = num % 10
        sum += digit

        if digit >  max_digit:
            max_digit = digit
        elif digit < min_digit:
            min_digit = digit

        num //= 10

        if num < 1:
            break;

    print(f"Кількість: {count}")
    print(f"Сума: {sum}")
    print(f"Найбільше: {max_digit}")
    print(f"Найменше: {min_digit}")



def task_3():
    num = int(input("Введіть натуральне число: "))

    for i in range(1, num + 1):
        temp = i
        is_correct = True

        while temp > 0:
            digit = temp % 10

            if digit != 0 and i % digit != 0:
                is_correct = False
                break

            temp //= 10

        if is_correct:
            print(i, end=' ')


def task_4():
    width = int(input("Введіть ширину: "))
    height = int(input("Введіть висоту: "))
    border = input("Введіть символ контуру: ")
    inner = input("Введіть символ внутрішньої частини: ")

    if width < 3 or height < 3:
        raise ValueError("Мінімальний розмір рамки - 3 × 3") from None

    for row in range(height):
        for col in range(width):
            if row == 0 or row == height - 1 or col == 0 or col == width - 1:
                print(border, end='')
            else:
                print(inner, end='')
        print()


# task_1()
# task_2()
# task_3()
# task_4()