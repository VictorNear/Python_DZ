
def user_input():
   
   ask = int(input("Выбери ниже: \n 1-записать пользователя \n 2-поиск по имени \n" 
                   " 3-отсортировать справочник по имени \n 4-сортировка по дате рождения \n"
                   " 5-вывод имен абонентов \n 6-вывод справочника \n 7-удалить абонента из списка \n"
                   " 8-изменить данные абонента \n 9-выйти \n"))
   return ask

def man():
   name = input("Введите имя: ")
   famaly = input("Введите фамилию: ")
   father = input("Введите отчество: ")
   date = input("Введите дату рождения: ")
   telephone = input("Введите телефон: ")
   data = name + "; " + famaly + "; " + father + "; " + date +"; " + telephone + "; " + "\n"
   return data.lower()

def search():
   str_search = input("Введите данные для поиска: ").lower()
   return str_search

def select_num():
   num = int(input("Выберите аббонента: "))
   return num