from flask import Flask
import json

app = Flask(__name__)


@app.route("/")
def get_candidates():
    '''Загружает кандитов из файла в СПИСОК'''
    with open('candidates.json', encoding="UTF-8") as file:
        file = tuple(json.load(file))
        return file


print(get_candidates())
# f'Имя кандидата: {file[0]["name"]}\n Позиция кандидата: {file[0]["position"]}'
# if __name__ == "__main__":
#     app.run(debug=True)
