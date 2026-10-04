def task_1():
    text = input("Введіть текст: ")

    vowels = "aeiou"

    lenght = 0
    letters = 0
    digits = 0
    spaces = 0
    vowels_count = 0

    for i in text.lower():
        lenght += 1

        if i.isalpha():
            letters += 1
        elif i.isdigit():
            digits += 1
        elif i == " ":
            spaces += 1

        if i in vowels:
            vowels_count += 1

    print(f"Символів: {lenght}")
    print(f"Літер: {letters}")
    print(f"Цифр: {digits}")
    print(f"Пробілів: {spaces}")
    print(f"Голосних: {vowels_count}")
    print(f"Слів: {len(text.split(' '))}")


def task_2():
    text = input("Введіть ПІБ: ")

    text = text.lower().title().split()

    if len(text) == 3:
        print(f"{text[0]} {text[1][0]}.{text[2][0]}")
    else:
        raise ValueError("Неправильні данні") from None


def task_3():
    text1 = sorted(input("Введіть текст1: ").lower().replace(' ', ''))
    text2 = sorted(input("Введіть текст2: ").lower().replace(' ', ''))

    if text1 == text2:
        print("Рядки є анаграмами")
    else:
        print("Рядки не є анаграмами")


def task_4():
    text = input("Введіть текст: ").lower().split()

    unique_words = []
    for w in text:
        if w not in unique_words:
            unique_words.append(w)

    word = input("Введіть слово для заміни малим регістром: ")

    if word in text:
        new_word = input("Введить нове слово: ")

        for i in range(len(text)):
            if text[i] == word:
                text[i] = new_word

        print("Найдовші:", max(text, key=len))
        print("Накоротші:", min(text, key=len))
        print("Унікальних слів:", len(unique_words))
        print("Після заміни:", ' '.join(text))
    else:
        print("Такого слова немає")


# task_1()
# task_2()
# task_3()
# task_4()