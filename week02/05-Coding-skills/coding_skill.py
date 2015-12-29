import sys
import json


def list_with_languages(data):
    languages = {}
    for person in range(0, len(data['people'])):
        for i in range(0, len(data['people'][person]['skills'])):
            current_lang = data['people'][person]['skills'][i]['name']
            languages[current_lang] = ''
    return languages


def list_with_names(data):
    dictionary = list_with_languages(data)
    for person in range(0, len(data['people'])):
        for i in range(0, len(data['people'][person]['skills'])):
            if dictionary[data['people'][person]['skills'][i]['name']] != '':
                current_level = data['people'][person]['skills'][i]['level']
                if dictionary[data['people'][person]['skills'][i]['name']] \
                   < current_level:
                    dictionary[data['people'][person]['skills'][i]['name']] \
                     = current_level
            else:
                dictionary[data['people'][person]['skills'][i]['name']] \
                 = data['people'][person]['skills'][i]['level']

    for i in range(0, len(data['people'])):
        for j in range(0, len(data['people'][i]['skills'])):
            lang = data['people'][i]['skills'][j]['name']
            person = data['people'][i]['first_name'] + ' ' \
                        + data['people'][i]['last_name']
            if lang in dictionary:
                if data['people'][i]['skills'][j]['level'] \
                   in dictionary.values():
                    dictionary[lang] = person

    return dictionary


def main():
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        data = json.load(f)

    list_with_names(data)


if __name__ == '__main__':
    print(main())
