import tkinter as tk

def get_values():
    # вытаскиваем введенные данные в первом поле:
    num1 = int(number1_entry.get())
    # вытаскиваем введенные данные во втором поле:
    num2 = int(number2_entry.get())
    # возвращаем взятые значения:
    return num1, num2

def insert_values(value):
    # добавляем метод для удаления старых ответов/обновления поля:
    answer_entry.delete(0, 'end')
    # добавляем результат в поле answer:
    answer_entry.insert(0, value)

def add():
    # создаем функцию сложения
    # берем значения из функции get_values:
    num1, num2 = get_values()
    # записываем результат функции сложения в переменную:
    res = num1 + num2
    # вызываем функцию insert_values, которая очищает поле и показывает новый результат:
    insert_values(res)


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def multi():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)

window = tk.Tk() #создаем графическое окно - всегда первая строчка
window.title('Калькулятор') #название окна
window.geometry('350x350') #размер
window.resizable(False, False) #ограничение изменений размера

#создаем кнопку, tk.Button = команда button из библиотеки tk, window - принадлежность
button_add = tk.Button(window, text = "+", width = 2, height = 2, command = add)
#размещаем кнопку с помощью метода place и задаем координаты
button_add.place(x = 100, y = 200)

button_sub = tk.Button(window, text = "-", width = 2, height = 2, command = sub)
button_sub.place(x = 150, y = 200)

button_multi = tk.Button(window, text = "x", width = 2, height = 2, command = multi)
button_multi.place(x = 200, y = 200)

button_div = tk.Button(window, text = "/", width = 2, height = 2, command = div)
button_div.place(x = 250, y = 200)

#tk.Entry - для создания полей, куда человек вводит информацию
number1_entry = tk.Entry(window, width = 21)
number1_entry.place(x = 100, y = 75)
number1 = tk.Label(window, text = "Введите первое число:")
number1.place(x = 100, y = 50)

number2_entry = tk.Entry(window, width = 21)
number2_entry.place(x = 100, y = 125)
number2 = tk.Label(window, text = "Введите второе число:")
number2.place(x = 100, y = 125)

answer_entry = tk.Entry(window, width = 21)
answer_entry.place(x = 100, y = 300)
answer = tk.Label(window, text = "Ответ:")
number2.place(x = 100, y = 275)

window.mainloop() #цикл обновления событий - всегда последняя строчка

