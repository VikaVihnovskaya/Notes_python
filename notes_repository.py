import csv


def create_notes(id, title, body, created_date, modified_date):
    with open('notes.csv', 'a') as data:
        writer = csv.DictWriter(data,  ['id', 'Title', 'Body', 'Created_date', 'Modified_date'])
        row = {'id': id, 'Title': title, 'Body': body, 'Created_date': created_date, 'Modified_date': modified_date}
        writer.writerow(row)


def read_notes():
    with open('notes.csv', 'r') as data:
        reader = csv.DictReader(data)
        return list(reader)

def read_index():
    with open('curent_id.csv', 'r') as data:
        reader = csv.DictReader(data)
        return list(reader)


def rewrite(data_list):
    with open('notes.csv', 'w') as data:
        writer = csv.DictWriter(data, ['id', 'Title', 'Body', 'Created_data', 'Modified_data'])
        writer.writeheader()
        for row in data_list:
            writer.writerow(row)


def rewrite_index(data_list):
    with open('curent_id.csv', 'w') as data:
        writer = csv.DictWriter(data, ['id'])
        writer.writeheader()
        for row in data_list:
            writer.writerow(row)
