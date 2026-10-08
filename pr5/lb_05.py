def task_one():
    def circle_area(radius):
        return 3.14159 * radius ** 2

    def rectangle_area(width, height):
        return width * height

    def triangle_area(base, height):
        return 0.5 * base * height

    def main():
        print("Оберіть фігуру: круг, прямокутник, трикутник")
        figure = input("Фігура: ").strip().lower()

        if figure == "круг":
            r = float(input("Радіус: "))
            print("Площа круга:", circle_area(r))
        elif figure == "прямокутник":
            w = float(input("Ширина: "))
            h = float(input("Висота: "))
            print("Площа прямокутника:", rectangle_area(w, h))
        elif figure == "трикутник":
            b = float(input("Основа: "))
            h = float(input("Висота: "))
            print("Площа трикутника:", triangle_area(b, h))
        else:
            print("Невідома фігур.")

    main()


def task_two():
    def is_prime(n):
        if n < 2:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    def divisors(n):
        result = []
        for i in range(1, n + 1):
            if n % i == 0:
                result.append(i)
        return result

    def digit_sum(n):
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        return total

    def main():
        n = int(input("N = "))
        print("Просте число:", "так" if is_prime(n) else "ні")
        print("Дільники:", divisors(n))
        print("Сума цифр:", digit_sum(n))

    main()


def task_three():
    def average(grades):
        return sum(grades) / len(grades)

    def minimum(grades):
        result = grades[0]
        for g in grades:
            if g < result:
                result = g
        return result

    def maximum(grades):
        result = grades[0]
        for g in grades:
            if g > result:
                result = g
        return result

    def count_above(grades, value):
        count = 0
        for g in grades:
            if g > value:
                count += 1
        return count

    def main():
        grades = [int(x) for x in input("Оцінки (через пробіл): ").split()]
        threshold = int(input("Поріг: "))

        print("Середній бал:", average(grades))
        print("Мінімальна:", minimum(grades))
        print("Максимальна:", maximum(grades))
        print(f"Вище {threshold}:", count_above(grades, threshold))

    main()


def task_four():
    def has_min_length(password, min_len=8):
        return len(password) >= min_len

    def has_digit(password):
        for ch in password:
            if ch.isdigit():
                return True
        return False

    def has_upper(password):
        for ch in password:
            if ch.isupper():
                return True
        return False

    def has_lower(password):
        for ch in password:
            if ch.islower():
                return True
        return False

    def has_special(password):
        for ch in password:
            if not ch.isalnum():
                return True
        return False

    def validate_password(password):
        errors = []
        if not has_min_length(password):
            errors.append("довжина менше 8 символів")
        if not has_digit(password):
            errors.append("немає цифри")
        if not has_upper(password):
            errors.append("немає великої літери")
        if not has_lower(password):
            errors.append("немає малої літери")
        if not has_special(password):
            errors.append("немає спеціального символу")
        return len(errors) == 0, errors

    def main():
        password = input("Password: ")
        is_valid, errors = validate_password(password)

        if is_valid:
            print("Пароль надійний")
        else:
            print("Пароль не відповідає вимогам")
            print("Не виконано:", "; ".join(errors))

    main()


# task_one()
# task_two()
# task_three()
# task_four()