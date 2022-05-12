from flask import Flask
from function import *


app = Flask(__name__)


@app.route("/")
def candidate():
    return get_candidates()


@app.route("/candidates/<int:id>/")
def id_candidate(id):
    return get_id(id)

@app.route("/skills/<skill>/")
def candidate_skill(skill):
    return get_skil(skill)

if __name__ == "__main__":
    app.run(debug=True)
