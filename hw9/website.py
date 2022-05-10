from flask import Flask, render_template
from function import load_candidate

app = Flask(__name__)


@app.route("/")
def get_candidates():
    """ Выведите полный список кандидатов """
    candidate = ""
    for candidates in load_candidate():
        candidate += 'Имя кандидата: ' + candidates["name"] + " \n"
        candidate += "Позиция кандидата: " + candidates["position"] + "\n"
        candidate += "Навыки через запятую: " + candidates["skills"] + "\n""\n"
    return "<h2>" + "<pre>" + candidate + "</pre>" + "<h2>"


@app.route("/candidates/<int:id>/")
def get_id(id):
    """ Выводит кандидатов по их ID"""
    id_list = ''
    for candidates in load_candidate():
        if candidates["id"] == id:
            id_list += 'Имя кандидата: ' + candidates["name"] + " \n"
            id_list += "Позиция кандидата: " + candidates["position"] + "\n"
            id_list += "Навыки через запятую: " + candidates["skills"] + "\n""\n"
            return "<h2>" + "<pre>" + id_list + "</pre>" + "<h2>"
    return "<h1>" + "Нет такого кандидата" + "<h1>"


@app.route("/skills/<skill>/")
def get_skil(skill):
    """ Выводит кандидатов по их навыкам"""
    skill_list = ''
    for candidates in load_candidate():
        if skill in candidates["skills"].capitalize():
            skill_list += 'Имя кандидата: ' + candidates["name"] + " \n"
            skill_list += "Позиция кандидата: " + candidates["position"] + "\n"
            skill_list += "Навыки через запятую: " + candidates["skills"] + "\n""\n"
            return "<h2>" + "<pre>" + skill_list + "</pre>" + "<h2>"
    return "<h1>" + "Нет такого кандидата с такими знаниями, предлагаю САМИМ учить!!!!" + "<h1>"


if __name__ == "__main__":
    app.run(debug=True)
