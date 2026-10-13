from datetime import date
from tkinter import messagebox
import tkinter as tk
import student_utils
import math
import random
import statistics


def task_one():
    radius = float(input("Радіус: "))
    legs = input("Катети: ").split(',')
    items = int(input("Предметів: "))
    n = int(input("В упаковці: "))

    print(f"Площа круга: {round(math.pi * radius**2, 2)}")
    print(f"Гіпотенуза: {round(math.sqrt(float(legs[0])**2 + float(legs[1])**2), 2)}")
    print(f"Потрібно упаковок: {math.ceil(items / n)}")


def task_two():
    n = int(input("Введіть кількість оцінок: "))

    if n < 0:
        print("N повинно бути додатнім")
        return

    marks = []

    for _ in range(n):
        marks.append(random.randint(1, 12))

    print(f"Оцінки: {marks}")
    print(f"Min: {min(marks)}")
    print(f"Max: {max(marks)}")
    print(f"Середнє: {statistics.mean(marks)}")
    print(f"Медіана: {statistics.median(marks)}")
    print(f"Оцінок 10–12: {marks.count(10) + marks.count(11) + marks.count(12)}")


def task_three():
    user_date = input("Дата події: ").split('-')

    current_date = date.today()
    event_date = date(int(user_date[0]), int(user_date[1]), int(user_date[2]))

    if event_date > current_date:
        delta = event_date - current_date
        print(f"До події залишилося: {delta.days} днів")
    elif event_date < current_date:
        delta = current_date - event_date
        print(f"З моменту події минуло: {delta.days} днів")
    else:
        print("Ця подія відбувається сьогодні")


def task_four():
    STUDENTS = ["Anna", "Ivan", "Olha"]

    def generate_report():
        input_value = entry_count.get().strip()

        if not input_value.isdecimal():
            messagebox.showerror("Помилка", "Введіть ціле додатне число")
            return

        count = int(input_value)
        if not (1 <= count <= 20):
            messagebox.showerror("Помилка", "Кількість оцінок повинна бути в діапазоні від 1 до 20")
            return

        report_lines = []

        for student in STUDENTS:
            grades = student_utils.generate_grades(count)
            avg = student_utils.average_grade(grades)
            level = student_utils.get_level(avg)

            line = f"{student}: {grades} - {avg:.1f} - {level}"
            report_lines.append(line)
        full_report = "\n".join(report_lines)

        print("\nНовий звіт:")
        print(full_report)

        text_result.delete("1.0", tk.END)
        text_result.insert(tk.END, full_report)

    root = tk.Tk()
    root.title("Статистика учнів")
    root.geometry("450x350")

    label_info = tk.Label(root, text="Введіть кількість оцінок для кожного учня (1–20):", font=("Arial", 10))
    label_info.pack(pady=5)

    entry_count = tk.Entry(root, font=("Arial", 10), width=10)
    entry_count.pack(pady=5)
    entry_count.insert(0, "1")

    btn_generate = tk.Button(root, text="Сформувати звіт", command=generate_report, font=("Arial", 10, "bold"))
    btn_generate.pack(pady=10)

    text_result = tk.Text(root, font=("Consolas", 10), width=50, height=10)
    text_result.pack(pady=5, padx=10)

    root.mainloop()


# task_one()
# task_two()
# task_three()
# task_four()