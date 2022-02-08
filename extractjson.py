import json

def validator(text):
    try:
        json.loads(text)
        valid = True
        
    except Exception as e:
        valid = False

    return valid


def find_json_strings(text):
    items = []

    opening_brackets = 0
    closing_brackets = 0
    first_bracket_found = False
    first_bracket_position = 0
    close_bracket_position = 0

    for i, character in enumerate(text):
        if character == "{":
            opening_brackets += 1
            if not first_bracket_found:
                first_bracket_found = True
                first_bracket_position = i

        if character == "}":
            closing_brackets += 1

        if opening_brackets == closing_brackets and (opening_brackets != 0):
            block = text[first_bracket_position:(i + 1)]
            items.append(block)

            opening_brackets = 0
            closing_brackets = 0
            first_bracket_found = False

    return items


def extract(content):
    valid_json = []

    json_str_objects = find_json_strings(content)
    for json_str_obj in json_str_objects:

        if not validator(json_str_obj):
            items = find_json_strings(json_str_obj[1:-1])
            for item in items:
                json_str_objects.append(item)
        else:
            valid_json.append(json_str_obj)

    return [json.loads(x) for x in valid_json if x != "{}"]
