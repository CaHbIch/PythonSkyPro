import requests
from classes import Question


def get_list():
    load_question = requests.get('https://jsonkeeper.com/b/WA8H')  # получит список вопросов с внешнего ресурса,
    load_question_json = list(load_question.json())
    questions = []
    for load_question in load_question_json:
        questions.append(Question(load_question["question_text"], load_question["difficulty"], load_question["answer"]))
    return questions


def statistician(questions):
    correct_count = 0  # Получает правильные ответы
    points_count = 0  # Получает кол-во очков
    for question in questions:
        if question.is_correct():
            correct_count += 1
            points_count += question.get_points()
    return points_count, correct_count
