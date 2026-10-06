def task_one():
    lst = [12, 3, 4, 14, -12, 5, 10, 16, -4]

    positive = []
    negative = []
    even = []
    multiples = []

    for i in lst:
        if i > 0:
            positive.append(i)
        elif i < 0:
            negative.append(i)

        if i % 2 == 0:
            even.append(i)

        if i % 3 == 0:
            multiples.append(i)

    print(f"Додатні: {positive}")
    print(f"Від'ємні {negative}")
    print(f"Парні: {even}")
    print(f"Кратні 3: {multiples}")

    print(f"Min: {min(lst)}; Max: {max(lst)}; Sum: {sum(lst)}; Avg: {(sum(lst) / len(lst)):.2f}")


def task_two():
    group1 = {'Anna', 'Ivan', 'Olha'}
    group2 = {'Ivan', 'Maksym', 'Olha'}

    print(f"Спільні:", ", ".join(group1 & group2))
    print(f"Тільки group1:", ", ".join(group1 - group2))
    print(f"Тільки group2:", ", ".join(group2 - group1))
    print(f"Усі:", ", ".join(group1 | group2))


def task_three():
    goods = {"apple": 25, "milk": 48, "tea": 75}

    while True:
        dec = input("1 - Додати товар\n2 - Змінити ціну існуючого\n3 - Пошук товару за назвою\n4 - Виведення всіх товарів в заданому діапазоні\n5 - Вийти\n")

        if dec == "1":
            parts = input("Введіть назву товару та його ціну, приклад: banana 15 грн\n").split()

            if len(parts) != 3 or not parts[0].isalpha() or not parts[1].isdigit():
                print("Ви ввели некоректний формат данних")
                continue

            if parts[0] in goods:
                print("Цей товар вже існує")
                continue

            goods[parts[0]] = int(parts[1])
            print("Товар успішно добавлено!")

        elif dec == "2":
            parts = input("Введіть назву товару та його ціну, приклад: banana 15 грн\n").split()

            if len(parts) != 3 or not parts[0].isalpha() or not parts[1].isdigit():
                print("Ви ввели некоректний формат данних")
                continue

            if parts[0] not in goods:
                print("Цього товару не існує")
                continue

            goods[parts[0]] = int(parts[1])
            print("Ціну товару успішно змінено!")

        elif dec == "3":
            name = input("Введіть назву товару: ").strip()

            if not name.isalpha():
                print("Ви ввели некоректний формат данних")
                continue

            if name not in goods:
                print("Цього товару не існує")
                continue

            print(f"{name}: {goods[name]} грн")

        elif dec == "4":
            parts = input("Ціновий діапазон (приклад: 10-100 грн): ").split()

            if not parts:
                print("Ви ввели некоректний формат данних")
                continue

            bounds = parts[0].split("-")

            if len(bounds) != 2 or not (bounds[0].isdigit() and bounds[1].isdigit()):
                print("Ви ввели некоректний формат данних")
                continue

            start, stop = int(bounds[0]), int(bounds[1])

            for key, value in goods.items():
                if start <= value <= stop:
                    print(f"{key}: {value} грн")

        elif dec == "5":
            break

        else:
            print("Невірний пункт меню")


def task_four():
    group_info = ("10-IT", "2025/2026")
    journal = {
        "Іваненко Іван Іванович": [10, 11, 9, 12, 10],
        "Петренко Марія Олегівна": [12, 12, 11, 12, 10],
        "Бурмалда Андрій Петрович": [7, 8, 6, 9, 8],
    }

    while True:
        choice = input(
            "\n1 - Додати учня\n"
            "2 - Показати весь журнал\n"
            "3 - Середній бал кожного учня\n"
            "4 - Рейтинг учнів\n"
            "5 - Учень з найвищим середнім балом\n"
            "6 - Вийти\n"
        ).strip()

        if choice == "1":
            name = " ".join(input("Введіть ПІБ учня: ").split())

            if not name:
                print("ПІБ не може бути порожнім")
                continue

            if name in journal:
                print("Такий учень уже є в журналі")
                continue

            parts = input("Введіть 5 оцінок (1-12) через пробіл: ").replace(",", " ").split()

            if len(parts) != 5:
                print("Потрібно рівно 5 оцінок")
                continue

            if not all(p.isdigit() and 1 <= int(p) <= 12 for p in parts):
                print("Кожна оцінка має бути цілим числом від 1 до 12")
                continue

            journal[name] = [int(p) for p in parts]
            print("Учня успішно додано")

        elif choice in ("2", "3", "4", "5"):
            if not journal:
                print("Журнал порожній")
                continue

            if choice == "2":
                print(f"\nГрупа: {group_info[0]}, навчальний рік: {group_info[1]}")
                print("-" * 50)
                for name, grades in journal.items():
                    print(f"{name} {grades}")

            elif choice == "3":
                print("\nСередній бал учнів:")
                for name, grades in journal.items():
                    print(f"{name} {sum(grades) / len(grades):.2f}")

            elif choice == "4":
                ranking = sorted(
                    journal.items(),
                    key=lambda item: sum(item[1]) / len(item[1]),
                    reverse=True,
                )
                print("\nРейтинг учнів за середнім балом:")
                for place, (name, grades) in enumerate(ranking, start=1):
                    print(f"{place}. {name} {sum(grades) / len(grades):.2f}")

            else:
                best_avg = max(sum(g) / len(g) for g in journal.values())
                print(f"\nНайвищий середній бал: {best_avg:.2f}")
                for name, grades in journal.items():
                    if sum(grades) / len(grades) == best_avg:
                        print(f" - {name}")

        elif choice == "6":
            break

        else:
            print("Невірний пункт меню")

# task_one()
# task_two()
# task_three()
# task_four()