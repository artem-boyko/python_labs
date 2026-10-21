def task_one():
    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

        def perimeter(self):
            return 2 * (self.width + self.height)

        def info(self):
            print(f"{self.width} * {self.height}: площа = {self.area()}, периметр = {self.perimeter()}")


    rectangles = [Rectangle(5, 3), Rectangle(10, 4), Rectangle(7, 7)]
    for rect in rectangles:
        rect.info()


class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 1 <= grade <= 12:
            self.grades.append(grade)
        else:
            print(f"Некоректна оцінка {grade}: має бути від 1 до 12")

    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"{self.name}: {self.grades}, середній = {self.average():.2f}"


def task_two():
    ivan = Student("Артем Артеменко")
    for g in (10, 12, 15, 9):
        ivan.add_grade(g)
    print(ivan)

    empty = Student("Бурмалда Бурмалдатович")
    print(empty)


def task_three():
    students = [
        Student("Анна"),
        Student("Адольф"),
        Student("Артем"),
        Student("Хтось"),
        Student("Газ"),
    ]

    grades_data = [
        [10, 11, 11],
        [9, 10],
        [12, 11, 11],
        [8, 9, 10],
        [11, 12, 11],
    ]

    for student, grades in zip(students, grades_data):
        for grade in grades:
            student.add_grade(grade)

    for student in students:
        print(f"{student.name} - {student.average():.2f}")

    best_average = max(student.average() for student in students)
    best_students = [s for s in students if s.average() == best_average]

    if len(best_students) == 1:
        print(f"Найкращий результат: {best_students[0].name} - {best_average:.2f}")
    else:
        print(f"Найкращий результат ({best_average:.2f}) у кількох учнів:")
        for student in best_students:
            print(f"{student.name} - {student.average():.2f}")


def task_four():
    class BankAccount:
        def __init__(self, owner, balance=0):
            self.owner = owner
            self.balance = balance

        def deposit(self, amount):
            if amount <= 0:
                print("Сума поповнення має бути більшою за 0")
                return False
            self.balance += amount
            print(f"Рахунок поповнено на {amount}")
            return True

        def withdraw(self, amount):
            if amount <= 0:
                print("Сума списання має бути більшою за 0")
                return False
            if amount > self.balance:
                print("Недостатньо коштів на рахунку")
                return False
            self.balance -= amount
            print(f"З рахунку знято {amount}")
            return True

        def info(self):
            print(f"Власник: {self.owner}, баланс: {self.balance}")


    account1 = BankAccount("Анна", 1000)
    account2 = BankAccount("Іван")

    account1.info()
    account1.deposit(500)
    account1.deposit(0)
    account1.deposit(-100)
    account1.withdraw(300)
    account1.withdraw(5000)
    account1.withdraw(-50)
    account1.info()

    account2.info()
    account2.deposit(200)
    account2.withdraw(250)
    account2.withdraw(200)
    account2.info()


# task_one()
# task_two()
# task_three()
# task_four()
