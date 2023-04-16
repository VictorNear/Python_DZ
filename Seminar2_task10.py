# Задача 10: На столе лежат n монеток. Некоторые из нихлежат вверх решкой, а некоторые – гербом. Определите
# минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той 
# же стороной. Выведите минимальное количество монет, которые нужно перевернуть.

n = int(input())
count_tails = 0
count_eagle = 0
for i in range(n):
   x = int(input())
   if x == 0:
      count_eagle += 1
   else:
      count_tails += 1
if count_tails > count_eagle:
   print(count_eagle)
else:
   print(count_tails)