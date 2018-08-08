from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_pymongo import PyMongo

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

#database config
app.config['MONGO_URI'] = 'mongodb://localhost:27017/violdb'

mongo = PyMongo(app)
violations = mongo.db.violations
# enable CORS
CORS(app)


@app.route('/violations', methods=['GET'])
def all_violations():

    output = []
    for q in violations.find():
        output.append({"index": q["index"], "date": q["date"], "whoFound": q["whoFound"], "network": q["network"],
                       "ipAdress" : q["ipAdress"], "department" : q["department"], "militaryUnit" : q["militaryUnit"],
                       "deslocation" : q["deslocation"], "subordinate" : q["subordinate"], "normDoc" : q["normDoc"],
                       "violCont" : q["violCont"], "volumeInf" : q["volumeInf"], "sourceDoc" : q["sourceDoc"],
                       "incomeDoc" : q["incomeDoc"]})
    return jsonify({ 'data': output})

#@app.route('/violation_edit/<int:viol_id>', methods=['PUT'])
#def update_violation(viol_id):

@app.route('/violation_delete/<int:data_index>', methods=['DELETE'])
def delete_violation(data_index):
    print(data_index)
    return jsonify({'Deleted', True})

    #mycollection.update_one({'_id':mongo_id}, {"$set": post}, upsert=False)

@app.route('/violation_new', methods=['POST'])
def add_violation():
    index = mongo.db.violations.count() + 1
    date = request.json['date']
    whoFound = request.json['whoFound']
    network = request.json['network']
    ipAdress = request.json['ipAdress']
    department = request.json['department']
    militaryUnit = request.json['militaryUnit']
    deslocation = request.json['deslocation']
    subordinate = request.json['subordinate']
    normDoc = request.json['normDoc']
    violCont = request.json['violCont']
    volumeInf = request.json['volumeInf']
    sourceDoc = request.json['sourceDoc']
    incomeDoc = request.json['incomeDoc']

    violations_id = violations.insert_one({"index": index, "date": date, "whoFound": whoFound, "network": network,
                                       "ipAdress" : ipAdress, "department" : department, "militaryUnit" : militaryUnit,
                                        "deslocation" : deslocation, "subordinate" : subordinate, "normDoc" : normDoc,
                                        "violCont" : violCont, "volumeInf" : volumeInf, "sourceDoc" : sourceDoc,
                                        "incomeDoc" : incomeDoc})
    new_violations = violations.find_one({'_id' : violations_id})

    output = {"index": index, "date": new_violations["date"], "whoFound": new_violations["whoFound"],
              "network": new_violations["network"], "ipAdress" : new_violations["ipAdress"], "department" : new_violations["department"],
              "militaryUnit" : new_violations["militaryUnit"], "deslocation" : new_violations["deslocation"], "subordinate" : new_violations["subordinate"],
              "normDoc" : new_violations["normDoc"], "violCont" : new_violations["violCont"], "volumeInf" : new_violations["volumeInf"],
              "sourceDoc" : new_violations["sourceDoc"], "incomeDoc" : new_violations["incomeDoc"]}

    return jsonify({'result' : output})
if __name__ == '__main__':
    app.run()