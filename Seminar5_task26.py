# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А 
# в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

number = int(input("Введите число: "))
degree = int(input("Введите степень: "))
res = number
def degree_of(number, degree, res):
   if degree == 1:
      return res
   else:
      res = res * number
      return degree_of(number, degree - 1, res)
print(f"{number} в степени {degree} равно {degree_of(number, degree, res)}")
