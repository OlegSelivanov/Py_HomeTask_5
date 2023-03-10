"""
Задача 26: 
Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B 
с помощью рекурсии.

A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
"""

A = int(input('Введите основание степени (A): '))
B = int(input('Введите показатель степени (b): '))

def power(A, B):
    if B < 0:
        return (1/A)*power(A, B+1)
    if B > 0:
        return A*power(A, B-1)
    else:
        return 1

print(f'Число {A} в степени {B} равно: {power(A, B)}')


"""
Задача 28: 
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

2 2
4
"""

def sum(a, b):
    if a == 0:
        return b
    return sum(a-1, b+1)  

print(sum(int(input('Введите число (а): ')), int(input('Введите число (b): '))))