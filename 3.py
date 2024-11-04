import random
import csv


def generate_references(dataset_path, num_references=20):
    references = []
    with open(dataset_path, 'r', encoding='latin-1') as dataset:
        reader = csv.DictReader(dataset, delimiter=';')
        all_records = list(reader)

        for _ in range(num_references):
            record = random.choice(all_records)
            reference = f"{record['Book-Author']}. {record['Book-Title']} - {record['Year-Of-Publication']}"
            references.append(reference)

    return references


def save_references_to_file(references, output_path):
    with open(output_path, 'w', encoding='utf-8') as output_file:
        for i, reference in enumerate(references, start=1):
            output_file.write(f"{i}. {reference}\n")


if __name__ == "__main__":
    dataset_path = 'books-en.csv'
    output_path = 'references.txt'

    references = generate_references(dataset_path)
    save_references_to_file(references, output_path)

    print(f"Список библиографических ссылок сохранен в файл {output_path}")