# Extra task (optional).
# Python "Loops" tasks:
# 1. Найдите сумму всех чисел от 5 до 57, исключив числа 34, 46 и 52.
# Сделайте это при помощи цикла while и for.

numbers = range(5, 58)
sum1 = 0
for num in numbers:
    if num == 34:
        continue
    if num == 46:
        continue
    if num == 52:
        continue
    sum1 += num
print(sum1)

# Найдите сумму чисел от 1 до 100, которые кратны 4.
numbers = range(1, 100)
sum1 = 0
for num in numbers:
    if num % 4 == 0:
        sum1 = sum1 + num
    else:
        continue
print(sum1)

# Выведите в цикле "while" следующую последовательность:
# 13, 12, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1
# Важно чтобы сохранились пробелы и запятые после выполнения цикла.
i = 13
arr = []
while i >= 1:
    arr.append(i)
    i -= 1
print(arr)
# 4. Выведите на экран таблицу умножения числа 5. Сделайте таблицу через цикл for.
# В каждом цикле число 5 должно умножаться от 1 до 10 включительно.
# 5. Выведите столбец чисел от 34 до 67 с выводом только четных чисел.
# Используйте цикл while для этой задачи.
i  = 32
while i < 67:
    i += 1
    if i % 2 == 0:
        print(i)
    else:
        continue


#7. Выведите числа от 1 до 100 с пропуском чисел 50 и 99.
#Создайте вывод при помощи цикла for, а также цикла while.

for num in range(1, 101):
    if num == 50:
        continue
    elif num == 99:
        continue
    print(num)