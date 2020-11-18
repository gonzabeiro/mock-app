from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"



@app.route('/predictions/fraudml/test/execution/<id>', methods=['GET'])
def get_prediction(id):
    # JSON file 
    path = "execution_" + id + ".json"
    f = open(path, "r") 
    # Reading from file 
    data = json.loads(f.read()) 
    return jsonify(data)

@app.route('/predictions/fraudml/test/<prediction_id>/execute', methods=['POST'])
def execute_prediction(prediction_id):
    # JSON file 
    path = "prediction_" + prediction_id + ".json"
    print(path)
    f = open(path, "r") 
    
    # Reading from file 
    data = json.loads(f.read()) 
    
    return jsonify(data)
