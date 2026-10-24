class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"Ім'я: {self.name}"


class Student(Person):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group
        self.grades = []

    def info(self):
        return f"Учень: {self.name}, група: {self.group}"

    def add_grade(self, grade):
        if grade < 1 or grade > 12:
            return False
        self.grades.append(grade)
        return True

    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def info(self):
        return f"Викладач: {self.name}, предмет: {self.subject}"


class Course:
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        self.students = []

    def find_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None

    def add_student(self, student):
        if self.find_student(student.name) is not None:
            print("Такий студент вже є")
            return False
        self.students.append(student)
        return True

    def remove_student(self, name):
        student = self.find_student(name)
        if student is None:
            return False
        self.students.remove(student)
        return True

    def show_students(self):
        print("Студенти:")
        number = 1
        for student in self.students:
            print(f"{number}. {student.name}")
            number += 1

    def show_course(self):
        print("Курс:", self.title)
        print("Викладач:", self.teacher.name)
        self.show_students()

    def add_grade_to_student(self, name, grade):
        student = self.find_student(name)
        if student is None:
            print("Студента не знайдено")
            return
        if student.add_grade(grade):
            print("Оцінку виставлено")
        else:
            print("Оцінка має бути від 1 до 12")

    def show_rating(self):
        sorted_students = sorted(self.students, key=lambda s: s.average(), reverse=True)
        print("Рейтинг:")
        number = 1
        for student in sorted_students:
            print(f"{number} {student.name} - {student.average():.2f}")
            number += 1


def save_data(course):
    with open("course_data.txt", "w", encoding="utf-8") as file:
        for student in course.students:
            grades = ",".join(str(grade) for grade in student.grades)
            print(f"{student.name};{student.group};{grades}", file=file)


def load_data(course):
    try:
        with open("course_data.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                try:
                    name, group, grades_text = line.split(";")
                    student = Student(name, group)
                    if grades_text != "":
                        for grade in grades_text.split(","):
                            student.add_grade(int(grade))
                    course.add_student(student)
                except ValueError:
                    print("Помилка у файлі, рядок пропущено:", line)
    except FileNotFoundError:
        print("Файлу немає")


def task_one():
    student1 = Student("Майкл Джексон", "IT-17")
    student2 = Student("Анненко Анна", "IT-17")
    print(student1.info())
    print(student2.info())


def task_two():
    people = [
        Person("Хтось Там"),
        Student("Анна Анненко", "IT-17"),
        Student("Петро Петрович", "IT-17"),
        Teacher("Іван Комаров", "Python"),
    ]
    for person in people:
        print(person.info())


def task_three():
    teacher = Teacher("Іван Комаров", "Python")
    course = Course("Python", teacher)
    course.add_student(Student("Анна Анненко", "IT-17"))
    course.add_student(Student("Ольга Бурмалда", "IT-17"))
    course.add_student(Student("Артем Сила", "IT-17"))
    course.add_student(Student("Петро Петренко", "IT-17"))
    course.add_student(Student("Анна Анненко", "IT-17"))
    course.remove_student("Петро Петренко")
    course.show_course()


def task_four():
    teacher = Teacher("Іван Комаров", "Python")
    course = Course("Python", teacher)
    load_data(course)

    while True:
        print()
        print("1 - показати курс")
        print("2 - додати студента")
        print("3 - видалити студента")
        print("4 - знайти студента")
        print("5 - виставити оцінку")
        print("6 - показати рейтинг")
        print("7 - зберегти дані")
        print("0 - вихід")
        choice = input("Ваш вибір: ")

        if choice == "1":
            course.show_course()
        elif choice == "2":
            name = input("ПІБ: ")
            group = input("Група: ")
            if course.add_student(Student(name, group)):
                print("Студента додано")
        elif choice == "3":
            name = input("ПІБ: ")
            if course.remove_student(name):
                print("Студента видалено")
            else:
                print("Студента не знайдено")
        elif choice == "4":
            name = input("ПІБ для пошуку: ")
            student = course.find_student(name)
            if student:
                print(student.info())
                print("Оцінки:", student.grades)
                print(f"Середній бал: {student.average():.2f}")
            else:
                print("Студента не знайдено")
        elif choice == "5":
            name = input("ПІБ: ")
            try:
                grade = int(input("Оцінка (1-12): "))
                course.add_grade_to_student(name, grade)
            except ValueError:
                print("Оцінка має бути числом")
        elif choice == "6":
            course.show_rating()
        elif choice == "7":
            save_data(course)
        elif choice == "0":
            break
        else:
            print("Невідомий пункт меню")


# task_one()
# task_two()
# task_three()
# task_four()