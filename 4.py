import xml.etree.ElementTree as ET

def parse_currency_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    char_codes = []
    values = []

    for valute in root.findall('Valute'):
        char_codes.append(valute.find('CharCode').text)
        values.append(float(valute.find('Value').text.replace(',', '.')))

    return char_codes, values

if __name__ == "__main__":
    file_path = 'currency.xml'
    char_codes, values = parse_currency_xml(file_path)

    print("CharCode:", char_codes)
    print("Value:", values)