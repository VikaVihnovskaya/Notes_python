import time

from prettytable import PrettyTable
from datetime import datetime
from notes_repository import create_notes, read_index, rewrite_index
from notes_repository import read_notes


def create_new_notes():
    name_notes = input('Введите заголовок заметки: ')
    body_notes = input('Введите тело заметки: ')
    date = current_date()
    id = generate_id()
    created_date = date
    modified_date = date
    create_notes(id, name_notes, body_notes, created_date, modified_date)


def search():
    data_list = read_notes()
    my_list = []
    find_contact = input('Введите название заметки,которую хотите прочитать: ')
    for i in range(len(data_list)):
        if find_contact.lower() in data_list[i]['Title'].lower():
            my_list.append(data_list[i])
    print_table(my_list)


def current_date():
    now = datetime.now()
    date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    return date_time_str


def get_all_notes():
    data_list = read_notes()
    print_table(data_list)


def delete_notes():
    notes = input('Введите название заметки,которую хотите удалить:  ')
    data_list = read_notes()
    dict_for_search = {}
    for i in range(len(data_list)):
        if notes in data_list[i]['Title']:
            dict_for_search[i] = data_list[i]
    if not dict_for_search:
        print("Такой заметки не существует!")
        return data_list

    print_table(list(dict_for_search.values()))
    while len(dict_for_search) != 1:
        id = input('Введите id заметки, которую хотите удалить: ')
        dict_for_search = dict(filter(lambda value: value[1]["id"] == id, dict_for_search.items()))

    key = list(dict_for_search.keys())[0]
    data_list.remove(dict(dict_for_search[key]))
    return data_list


def correction_notes():
    notes = input('Введите название заметки,которую хотите редактировать:  ')
    data_list = read_notes()
    dict_for_search = {}
    for i in range(len(data_list)):
        if notes in data_list[i]['Title']:
            dict_for_search[i] = data_list[i]
    if not dict_for_search:
        print("Такой заметки не существует!")
        return data_list

    print_table(list(dict_for_search.values()))
    while len(dict_for_search) != 1:
        id = input('Введите id заметки, которую хотите редактировать: ')
        dict_for_search = dict(filter(lambda value: value[1]["id"] == id, dict_for_search.items()))

    print('Что вы хотите редактировать?')
    list_of_command = ['Название заметки', 'Тело заметки', 'Название', 'Тело']
    while (command := input('Название заметки или Тело заметки: ')) not in list_of_command:
        print('Ошибка ввода!!!')
    else:
        mapping ={
            'Название заметки': 'Title',
            'Тело заметки': 'Body',
            'Название': 'Title',
            'Тело': 'Body'
        }
        data_list[list(dict_for_search.keys())[0]][mapping[command]] = input('Введите корректные данные: ')
        data_list[list(dict_for_search.keys())[0]]['Modified_data'] = current_date()
    return data_list


def search_date():
    data_list = read_notes()
    my_list = []
    dt_string = input('Введите дату в формате YYYYY-MM-DD ,чтобы сделать выборку: ')
    dt_object = datetime.strptime(dt_string, "%Y-%m-%d")
    for i in range(len(data_list)):
        note_creation_date_str = data_list[i]['Created_data']
        note_creation_date = datetime.strptime(note_creation_date_str, "%Y-%m-%d %H:%M:%S").date()
        if dt_object.year == note_creation_date.year and dt_object.month == note_creation_date.month and dt_object.day == note_creation_date.day:
            my_list.append(data_list[i])
    print_table(my_list)

def print_table(list_of_notes):
    my_table = PrettyTable(['id', 'Title', 'Body', 'Created_date', 'Modified_date'])
    for i in range(len(list_of_notes)):
        my_table.add_row(list_of_notes[i].values())
    print(my_table)


def generate_id():
    index_list = read_index()
    current_id = index_list[0]["id"]
    index_list[0]["id"] = str(int(current_id) + 1)
    rewrite_index(index_list)
    return current_id
