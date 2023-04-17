# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input())
lst = []
for i in range(n):
   number = int(input())
   lst.append(number)

x = int(input())
min = 10000

for i in range(len(lst)):
   new_min = abs(x - lst[i])
   if new_min < min:
      min = new_min
      rez = lst[i]
print(rez)