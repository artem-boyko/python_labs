def task_one():
    with open("text.txt", encoding="utf-8") as f:
        lines = f.read().splitlines()

    words = 0
    chars = 0
    longest_no = 0
    longest_len = 0
    longest_text = ""

    for i in range(len(lines)):
        line = lines[i]
        words += len(line.split())
        chars += len(line)
        if len(line) > longest_len:
            longest_len = len(line)
            longest_no = i + 1
            longest_text = line

    print("Рядків:", len(lines))
    print("Слів:", words)
    print("Символів:", chars)
    print("Найдовший рядок: " + str(longest_no) + ",", longest_len, "символів")
    print("Текст:", longest_text)


def task_two():
    fragment = input("Фрагмент: ").lower()

    with open("text.txt", encoding="utf-8") as f:
        lines = f.read().splitlines()

    found = False
    for i in range(len(lines)):
        if fragment in lines[i].lower():
            print(str(i + 1) + ": " + lines[i])
            print()
            found = True

    if not found:
        print("Збігів не знайдено")


def task_three():
    with open("students.txt", encoding="utf-8") as f:
        lines = f.read().splitlines()

    students = []
    for line in lines:
        if line.strip() == "":
            continue
        parts = line.split(";")
        name = parts[0]
        score = int(parts[1])
        if score > 80:
            students.append((name, score))

    students.sort(key=lambda s: s[1], reverse=True)

    with open("result.txt", "w", encoding="utf-8") as f:
        for name, score in students:
            f.write(name + ";" + str(score) + "\n")


def task_four():
    with open("grades.csv", encoding="utf-8") as f:
        lines = f.read().splitlines()

    grades = {}
    for line in lines:
        if line.strip() == "":
            continue
        parts = line.split(";")
        name = parts[0]
        grade = int(parts[2])
        if name not in grades:
            grades[name] = []
        grades[name].append(grade)

    result = []
    for name in grades:
        g = grades[name]
        result.append((name, len(g), sum(g) / len(g)))

    result.sort(key=lambda r: r[2], reverse=True)

    best_avg = round(result[0][2], 2)
    best = []
    for r in result:
        if round(r[2], 2) == best_avg:
            best.append(r[0])

    with open("report.txt", "w", encoding="utf-8") as f:
        for name, count, avg in result:
            f.write(f"{name} - оцінок: {count} - середній: {avg:.2f}\n")
        f.write("Найкращий результат: " + " та ".join(best) + f" - {best_avg:.2f}\n")


# task_one()
# task_two()
# task_three()
task_four()