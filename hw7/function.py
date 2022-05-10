import json


def load_students():
    '''Загружает студентов из файла в СПИСОК'''
    with open('students.json') as file:
        file = json.load(file)
        return file


def load_professions():
    '''Загружает навыки из файла в СПИСОК'''
    with open('professions.json') as file:
        file = json.load(file)
    return file


def get_student_by_pk(pk):
    '''Получает СЛОВАРЬ с данными студента по его 'pk' '''
    for students in load_students():
        if students['pk'] == pk:
            return f'Студент: {students["full_name"]}\nЗнает: {" ".join(students["skills"])}'
    print('У нас нет такого студента')
    quit()


def get_profession_by_title(title):
    '''Получает СЛОВАРЬ с инфо о профе по названию'''
    for professions in load_professions():
        if professions['title'] == title.capitalize():
            return set(professions['skills'])
    print('У нас нет такой специальности')
    quit()


def student_load_professions(student):
    """Выводит навыки выбранного студента отдельно"""
    with open("students.json") as file:
        file = json.load(file)
        return set(file[student - 1]["skills"])


def check_fitness(pk, profession):
    ''' Проверка на профпригодность'''
    students = student_load_professions(pk)
    professions = get_profession_by_title(profession)
    intersections = professions.intersection(students)
    differences = professions.difference(students)
    fitness = round((len(intersections) * 100) / len(professions))
    if fitness == 100:
        return f"Пригодность: {fitness}%\nСтудент знает {' '.join(intersections)}\nСтудент знает всё"
    elif 1 <= fitness <= 99:
        return f"Пригодность: {fitness}%\nСтудент знает {' '.join(intersections)}\nСтудент не знает {' '.join(differences)}"
    else:
        return f"Пригодность: {fitness}%\nСтудент ничего не знает"
