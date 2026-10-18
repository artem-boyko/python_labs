def task_one():
    try:
        a = float(input("A: "))
        b = float(input("B: "))
    except ValueError:
        print("Потрібно ввести числа")
    else:
        operation = input("Операція: ").strip()

        if operation == "+":
            print("Результат:", a + b)
        elif operation == "-":
            print("Результат:", a - b)
        elif operation == "*":
            print("Результат:", a * b)
        elif operation == "/":
            try:
                print("Результат:", a / b)
            except ZeroDivisionError:
                print("На нуль ділити не можна")
        else:
            print("Невідома операція")


def task_two():
    def input_grade():
        while True:
            text = input("Оцінка: ")

            try:
                grade = int(text)
            except ValueError:
                print("Потрібно ввести ціле число")
                continue

            try:
                if grade < 1 or grade > 12:
                    raise ValueError("Оцінка повинна бути від 1 до 12")
            except ValueError as error:
                print(f"Помилка: {error}")
                continue

            return grade

    grade = input_grade()
    print(f"Прийнято: {grade}")


def task_three():
    students = ["Іваненко Іван", "Петренко Петро", "Коваль Альберт", "Шевченко Тарас"]
    grades = {"математика": 12, "фізика": 10, "історія": 9, "інформатика": 11}

    choice = input("1 - учень, 2 - предмет: ").strip()

    if choice == "1":
        text = input("Індекс: ")
        try:
            index = int(text)
        except ValueError:
            print("Індекс повинен бути цілим числом")
        else:
            try:
                print("Учень:", students[index])
            except IndexError:
                print("Учня з таким індексом немає")
    elif choice == "2":
        subject = input("Предмет: ").strip().lower()
        try:
            print(f"Оцінка з предмета {subject}:", grades[subject])
        except KeyError:
            print("Такого предмета немає")
    else:
        print("Невідомий пункт меню")


def task_four():
    valid = []
    skipped = 0

    try:
        with open("students.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Файл students.txt не знайдено")
    else:
        for number, line in enumerate(lines, start=1):
            line = line.strip()
            if not line:
                continue

            if ";" not in line:
                print(f"Рядок {number} пропущено: немає роздільника ;")
                skipped += 1
                continue

            parts = line.split(";")
            if len(parts) != 2 or not parts[0].strip():
                print(f"Рядок {number} пропущено: неправильна кількість полів")
                skipped += 1
                continue

            name = parts[0].strip()

            try:
                score = int(parts[1].strip())
            except ValueError:
                print(f"Рядок {number} пропущено: бал не є цілим числом")
                skipped += 1
                continue

            try:
                if score < 0 or score > 100:
                    raise ValueError("бал поза діапазоном 0..100")
            except ValueError as error:
                print(f"Рядок {number} пропущено: {error}")
                skipped += 1
                continue

            valid.append((name, score))

        valid.sort(key=lambda record: record[1], reverse=True)

        with open("report.txt", "w", encoding="utf-8") as report:
            for name, score in valid:
                report.write(f"{name};{score}\n")

        print(f"Правильних записів: {len(valid)}")
        print(f"Пропущених записів: {skipped}")


# task_one()
# task_two()
# task_three()
# task_four()