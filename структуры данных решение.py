print("Задача 1.", "✣" * 50)

# импортируем модуль math.
import math

# Запрашиваем у пользователя на ввод значения радиуса окружности.
definition_radius = int(input("Введите размер радиуса: "))

# Определяем функцию circle_area(), которая принимает один аргумент, в теле функции мы вычисляем площадь круга
# с помощью функции math.pi и оператора возведения в степень **.
# Выводим результат f-строки и округляем до двух знаков после запятой.
def circle_area(radius):
    area = math.pi * radius ** 2
    print(f"Площадь круга радиуса: {radius}, равна - {round(area, 2)} кв.ед.")

# Вызываем функцию.
circle_area(definition_radius)

print()
print("Задача 2.", "✣" * 50)

# Создаём функцию с двумя аргументами. В теле функции происхоит поверка условия: если n равно None,
# то с помощью функции sum() вычисляется сумма всех элементов списка lst и сохраняется в переменную sum_lst.
# Затем выводится сообщение и вычисленное значение sum_lst.
# Если значение n не равно None, то с помощью функции sum() вычисляется сумма первых n элементов списка lst (срез списка lst[:n])
# и сохраняется в переменную sum_lst. Затем выводится сообщение , перечисление первых n элементов списка lst,
# и вычисленное значение sum_lst.
def sum_elements(lst, n=None):
    if n == None:
        sum_lst = sum(lst)
        print(f"Сумма всех элементов списка равна {sum_lst}.")
    else:
        sum_lst = sum(lst[:n])
        print(f"Сумма элементов {', '.join(map(str, lst[:n]))} равна {sum_lst}.")

list_example = range(-10, 10)
n = 2
sum_elements(list_example, 2)
sum_elements(list_example)

print()
print("Задача 3.", "✣" * 50)

print("Далее позволю себе не расписывать подробно алгоритм решения задач, так как будет занимать время,\nкоторое хотелось бы уделить на изучение Pandas 🙏😊")
print()

def mean(lst):
    sum_lst = 0
    for i in lst:
        sum_lst += i
    mean_value = sum_lst / len(lst)
    print(f"Выборочное среднее: {mean_value}.")

def median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 0:
        median_value = (sorted_lst[n//2-1] + sorted_lst[n//2]) / 2
    else:
        median_value = sorted_lst[n//2]
    print(f"Медиана: {median_value}.")

def mode(lst):
    count_dict = {}
    for i in lst:
        if i not in count_dict:
            count_dict[i] = 1
        else:
            count_dict[i] += 1
    max_count = max(count_dict.values())
    mode_value = [k for k, v in count_dict.items() if v == max_count]
    print(f"Наиболее распространенный элемент: {', '.join(map(str, mode_value))}.")


value = [12, 13, 2, 4, 13, 5, 6, 7, 8, 8, 8, 8, 8, 10]
mean(value)
median(value)
mode(value)


print()
print("Задача 4.", "✣" * 50)

print("Решение задания с использованием кортежа.")

def income(*args):
    total_income = sum(args)
    print(f"Общий доход: {total_income}.")

income(100)
income(100, 10)
income(200, 300, 400)

print("Решение задания с использованием словаря.")

def income(**kwargs):
    total_income = sum(kwargs.values())
    print(f"Общий доход: {total_income}.")

income(salary=100, deposits=50, dividends=20, benefits=5)
income(salary=200, benefits=10)
income(deposits=500)
