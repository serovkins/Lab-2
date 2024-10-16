import json
import csv

DATASET_PATH = 'memes_dataset.csv'
OUT_PATH = 'out.json'


def get_title(dataset):
    dataset.seek(0)
    title = next(dataset)
    title = title.split(',')
    title = [col.strip() for col in title]
    return title


def get_object_alt(line, title):
    reader = csv.DictReader([line], title, delimiter=',', quotechar='"')
    res = next(reader)
    return res


def filter_year(dataset, title, year):
    filtered = []
    dataset.seek(0)  # Reset the file pointer
    next(dataset)  # Skip the header row

    for line in dataset:
        obj = get_object_alt(line, title)
        year_value = obj['origin_year']
        if year_value == str(year):
            filtered.append(obj)

    dataset.seek(0)  # Reset the file pointer
    return filtered


if __name__ == '__main__':
    with open(DATASET_PATH) as dataset:
        title = get_title(dataset)
        res = filter_year(dataset, title, 2008)
        res = json.dumps(res, indent=4)
        with open(OUT_PATH, 'w') as out:
            out.write(res)