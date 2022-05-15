import json


def load_candidate():
    '''Загружает кандидатов из файла в СПИСОК'''
    with open('candidates.json') as file:
        file = json.load(file)
        return tuple(file)


def get_candidates():
    """ Выведите полный список кандидатов """
    candidate = ""
    for candidates in load_candidate():
        candidate += "Имя кандидата: " + candidates["name"] + "\n" \
                     "Позиция кандидата: " + candidates["position"] + "\n" \
                     "Навыки через запятую: " + candidates["skills"] + "\n""\n"
    return "<h2>" + "<pre>" + candidate + "</pre>" + "<h2>"


def get_id(id):
    """ Выводит кандидатов по их ID"""
    id_list = ''
    for candidates in load_candidate():
        if candidates["id"] == id:
            id_list += "<img src=https://picsum.photos/200>" + "\n" \
                       "Имя кандидата: " + candidates["name"] + "\n" \
                       "Позиция кандидата: " + candidates["position"] + "\n" \
                       "Навыки через запятую: " + candidates["skills"] + "\n"
            return "<h2>" + "<pre>" + id_list + "</pre>" + "<h2>"
    return "<h1>" + "Нет такого кандидата" + "<h1>" + "<img src=https://picsum.photos/500>"


def get_skil(skill):
    """ Выводит кандидатов по их навыкам"""
    skill_list = ""
    for candidates in load_candidate():
        skills = candidates["skills"].lower().split(', ')
        if skill in skills:
            skill_list += "Имя кандидата: " + candidates["name"] + " \n" \
                          "Позиция кандидата: " + candidates["position"] + "\n" \
                          "Навыки через запятую: " + candidates["skills"] + "\n""\n"
    return "<h2>" + "<pre>" + skill_list + "</pre>" + "<h2>"