from notes_service import create_new_notes, search, get_all_notes, delete_notes, correction_notes, search_date
from notes_repository import read_notes, rewrite

def redactor():
    while True:
        print('\n\t\t*****Главное Меню*****')
        print('''
              1 - Создать заметку
              2 - Прочитать
              3 - Редактировать
              4 - Удалить 
              5 - Вывести список
              6 - Поиск по дате
              7 - Выход
     
             ''')
        str_in = input()
        if str_in == "1":
            print('')
            create_new_notes()
            return redactor()
        elif str_in == "2":
            search()
        elif str_in == "3":
            rewrite(correction_notes())
        elif str_in == "4":
            rewrite(delete_notes())
        elif str_in == "5":
            get_all_notes()
        elif str_in == "6":
            search_date()
        elif str_in == "7":
            break