import csv


def create_notes(title, body, created_date, modified_date):
    with open('notes.csv', 'a') as data:
        writer = csv.DictWriter(data,  ['id', 'Title', 'Body', 'Created_date', 'Modified_date'])
        row = {'id': generate_index(), 'Title': title, 'Body': body, 'Created_date': created_date, 'Modified_date': modified_date}
        writer.writerow(row)


def read_notes():
    with open('notes.csv', 'r') as data:
        reader = csv.DictReader(data)
        return list(reader)


def generate_index():
    with open('notes.csv', 'r') as data:
        reader = csv.DictReader(data)
        row_count = sum(1 for row in data)
        return row_count


def rewrite(data_list):
    with open('notes.csv', 'w') as data:
        writer = csv.DictWriter(data, ['id', 'Title', 'Body', 'Created_data', 'Modified_data'])
        writer.writeheader()
        for row in data_list:
            writer.writerow(row)



