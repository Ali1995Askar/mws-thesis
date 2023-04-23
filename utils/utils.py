def camel_case_to_readable(camel_case_string):
    result = camel_case_string[0].lower()
    for char in camel_case_string[1:]:
        if char.isupper():
            result += ' ' + char.lower()
        else:
            result += char
    return result.title()
