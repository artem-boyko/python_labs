import tkinter as tk


# print(math.sqrt(81))
#
# a = [10, 15, 3, 5, 8, 9]
#
# print(f'Mean mark: {stat.mean(a):.2f}')
#
# r = int(input("r = "))
#
# print(round(math.pi * math.pow(r, 2), 2))

# balls = 25
# n = 6
# print(f'Повністю заповнених коробок: {math.floor(balls / n)}')
# print(f'Всього коробок: {math.ceil(balls / n)}')

# numbers = []
#
# for i in range(10):
#     numbers.append(random.randint(1, 100))
#
# print(numbers)

# print(f"Сьогодні: {date.today()}")

# print(demo.square(3))
# print(demo.is_even(8))


def text():
    text = "Tysm!"
    lbl_text['text'] = text


def text2():
    text = "I'll punish u!"
    lbl_text['text'] = text


def clear(event):
    lbl_text['text'] = ''


window = tk.Tk()
window.title("My Window")
window.geometry('200x200')
window.resizable(False, False)
window["bg"] = "#F19CBB"

label = tk.Label(window, text="The best program in the world", bg="#F19CBB", font=("Arial, 18"), pady=20)
label.pack()

frame = tk.Frame(window, bg="#F19CBB")
frame.pack()

btn1 = tk.Button(frame, text="Tip", width=7, activebackground="lightgreen", command=text)
btn1.grid(row=0, column=0, padx=10)

btn2 = tk.Button(frame, text="No Tip", width=7, activebackground="lightgreen", command=text2)
btn2.grid(row=0, column=1, padx=10)
btn2.bind("<Button-3>", clear)

lbl_text = tk.Label(frame, text="", bg="#F19CBB", font=("Arial, 18"), pady=20)
lbl_text.grid(column=0, row=1, columnspan=2)

window.mainloop()