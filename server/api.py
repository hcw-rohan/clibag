from flask import Flask, request
import json

json_data = ''
app = Flask(__name__)

def load_json(filename):
    """ load external json file """

    with open(filename) as data_file:
        json_data = json.load(data_file)

    return json_data

json_data = load_json("dummy.json")

# Get the questions
questions = json_data['questions']

# Get the questions
#questions = json_data['questions']

@app.route("/api/", methods=['POST'])
def api():
    """ api request """
    questionid = request.form['qid']

    print(json.dumps(questions[int(questionid)]))

    return str(json.dumps(questions[int(questionid)]))