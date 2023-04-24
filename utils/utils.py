import csv


def create_csv(filename, columns, data):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(columns)
        for row in data:
            writer.writerow(row)

    print(f"CSV file '{filename}' created successfully")


def camel_case_to_readable(camel_case_string):
    result = camel_case_string[0].lower()
    for char in camel_case_string[1:]:
        if char.isupper():
            result += ' ' + char.lower()
        else:
            result += char
    return result.title()
