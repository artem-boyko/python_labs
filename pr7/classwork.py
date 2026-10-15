# with open("text.txt", 'r', encoding="utf-8") as f:
#     for n, l in enumerate(f, start=1):
#         print(n, l, end="")

# w, r, a, x

# line = "Komarov Ivan;2\n"
# clean_line = line.strip()
# name, grade = clean_line.split(';')
# print(name, grade)

# students = []
# botanics = []
#
# with open("students.txt", 'r', encoding="utf-8") as f:
#     for i in f:
#         name, grade = i.strip().split(';')
#         students.append([name, grade])
#
#         if int(grade) >= 90:
#             botanics.append([name, grade])
#
# print(students)
# print(botanics)
#
# with open("botanics.txt", 'w', encoding="utf-8") as f:
#     for name, grade in botanics:
#         f.write(name + ';' + grade + '\n')

# with open("grades.csv", 'r', encoding="utf-8") as f:
#     for l in f:
#         name, subject, grade = l.strip().split(';')
#         print(name, subject, grade)

