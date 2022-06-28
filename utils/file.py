import csv
from datetime import datetime


def generate_filename(search_term):
    timestamp = datetime.now().strftime("%d%m%Y")
    stem = path = '_'.join(search_term.split(' '))
    filename = stem + '_' + timestamp + '.csv'
    return filename


def save_data_to_csv(record, filename, new_file=False):
    header = ['Store_name', 'Product_name', 'Weight', 'Price', 'Price_kilo','Image']
    if new_file:
        with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(header)
    else:
        with open(filename, 'a+', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(record)