# -*- coding: utf-8 -*-
"""HomeWork1-3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iIpYIE9sS-tJgRsTmqU5pYdG4CqqnJ1n
"""

#Задача 1. Напишите программу, которая находит сумму цифр заданного числа. Например, для числа 123 сумма цифр равна 1 + 2 + 3 = 6

a = int(input())
ostatok = 0
summa = 0
while a >= 1:
    summa += a % 10
    a = a // 10
print (summa)

#Задача 2. Вите очень понравилась идея Фёдора с калькулятором, он захотел создать свой, но чтобы не повторять идею друга полностью, решил сделать калькулятор, который перемножает числа от 1 до n. Тем более, у получившегося произведения есть название - факториал. Обозначается он так: n!. Вводится натуральное число n. Выведи результат умножения чисел от 1 до n.

n = int(input())
factorial = 1
for i in range(n):
    factorial *= (i+1)
print(factorial)

#Задача 3. Миша учит признаки делимости чисел на 7. Чтобы себя проверить, он написал программу, которая выводит все числа, кратные семи до числа n. Есть целое число n. Вывести в столбик все такие числа.

n = int(input())
if n > 0:
    for i in range(n):
        delimoe = i + 1
        if delimoe % 7 == 0:
            print(delimoe)
if n < 0:
    for i in range(0, n, -1):
        delimoe = -1 + i
        if delimoe % 7 == 0:
            print(delimoe)