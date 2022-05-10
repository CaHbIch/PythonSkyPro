import json


def load_candidate():
    '''Загружает кандидатов из файла в СПИСОК'''
    with open('candidates.json') as file:
        file = json.load(file)
        return file

