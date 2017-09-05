from flask import Flask, request
import json

json_data = ''
app = Flask(__name__)

is_debug = app.config['DEBUG']

def load_json(filename):
    """ load external json file """

    with open(filename) as data_file:
        json_data = json.load(data_file)

    return json_data

if (is_debug is True):
    json_data = load_json("dummy.json")
else:
    #load the real data here
    print("! No Game Data !")
    exit()

# Get the questions
questions = json_data['questions']

# Get the questions
#questions = json_data['questions']

@app.route("/api/", methods=['POST'])
def api():
    """ api request """
    questionid = request.form['qid']

    if (is_debug is True):
        print(json.dumps(questions[int(questionid)]))

    return str(json.dumps(questions[int(questionid)]))

if __name__ == "__main__":
   main(sys.argv[1:])