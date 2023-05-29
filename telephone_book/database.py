# основные функции:
# основные модули:
# view.py - функции для работы с пользователем
# database.py - функции для работы с текстовым файлом
# controller.py - связь этих функций между собой
# main.py - модуль для запсука скрипта(необязательно)
# 0)менюшка с функциями ниже, чтобы в терминале писать цифру - означающую номер функции, в бесконечном цикле
# 1)ввод данных пользователем(имя, телефон, дата рождения)
# 2)добавление записи в txt документ
# 3)поиск по полю - либо телефон, либо имя
# 4)сортировка файла по имени,или по дате рождения и его перезапись
# 5) вывод только имен сотрудников
# 6)вывод всего файлика txt

def add_dat(data):
   with open("db.txt", "a" ) as file:
      file.write(data)
   print("Телефонная книга обновлена.\n")

def search_name(name):
   with open("db.txt", "r" ) as file:
      data = file.readlines()
      flag = False
      for i in data:
         if name in i:
            print(i)
            flag = True      
      if flag == False:      
         print("Абоннент не найден \n")

def sort_db_name():
   with open("db.txt", "r") as file:
      data = file.readlines()
      data.sort()
   with open("db.txt", "w") as file:
       file.writelines(data)
       
def sort_db_data():
   with open("db.txt", "r") as file:
      data = file.readlines()
      data.sort(key = lambda x: x[4])
   with open("db.txt", "w") as file:
       file.writelines(data)
       
def print_name():
   with open("db.txt", "r") as file:
      data = file.readlines()
      for i in data:
         print(i.split(";")[0])

def print_db():
   with open("db.txt", "r") as file:
      print(file.read())

def select_db(name):
   lst_db = []
   count = 1
   with open("db.txt", "r") as file:
      db = file.readlines()
      for i in db:
         if name in i:
            print(count, i.strip()) 
            count += 1
            lst_db.append(i)
   return lst_db

def del_abonnent(number):
   with open("db.txt", "r") as file:
      db = file.readlines()
      with open("db.txt", "w") as file:
         for i in db:
            if number == i:
               continue
            file.write(i)
      print("абоннент удален")    
   
def change_abonnent(dat, data):
   with open("db.txt", "r") as file:
      db = file.readlines()
      with open("db.txt", "w") as file:
         for i in db:
            if i == dat:
               file.write(data)
               continue
            file.write(i)
      print("абоннент изменен")  