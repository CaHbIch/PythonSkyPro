import json
from hw11.main import path



def load_candidate():
    '''Загружает кандидатов из файла в СПИСОК'''
    with open(path, encoding="utf-8") as file:
        file = json.load(file)
        return file

print(load_candidate())