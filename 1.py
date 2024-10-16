import csv


DATASET_PATH = 'books-en.csv'


def get_title(dataset):
    dataset.seek(0)
    title = next(dataset)
    title = title.split(';')
    title = [col.strip() for col in title]
    return title


def get_object(line, title):
    reader = csv.DictReader([line], title, delimiter=';', quotechar='"')
    res = next(reader)
    return res


def filter_books_by_length(dataset, title, min_length=30):
    count = 0
    
    for line in dataset:
        obj = get_object(line, title)
        book_title = obj.get('Book-Title')
        if book_title and len(book_title) > min_length:
            count+=1
    return count


if __name__ == '__main__':
    with open(DATASET_PATH) as dataset:
        title = get_title(dataset)
        count = filter_books_by_length(dataset, title)
        print(count)