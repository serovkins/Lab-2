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


def find_books_by_author(dataset, author):
    title = get_title(dataset)
    found_books = []
    
    for line in dataset:
        obj = get_object(line, title)
        if obj['Book-Author'] == author:
            found_books.append(obj)
    return found_books


if __name__ == '__main__':
    with open(DATASET_PATH, 'r') as dataset:
        author_to_search = input("Enter the author's name: ")
        found_books = find_books_by_author(dataset, author_to_search)

        if found_books:
            print("Books by", author_to_search + ":")
            
            for book in found_books:
                print(book)
        
        else:
            print("No books found by", author_to_search)