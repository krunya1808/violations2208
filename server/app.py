from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_pymongo import PyMongo
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

#jwt = JWTManager(app)

#database config
app.config['MONGO_URI'] = 'mongodb://localhost:27017/violdb'

mongo = PyMongo(app)
violations = mongo.db.violations
users = mongo.db.users
# enable CORS
CORS(app)

'''@app.route('/auth', methods=['POST'])
def login():
    if not request_is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    if username != 'test' or password != 'test':
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200'''

@app.route('/users', methods=['GET'])
def get_all_users():
    output = []
    for q in users.find():
        output.append({"public_id": q["public_id"], "name": q["name"], "login": q["login"],
                      "password": q["password"], "admin": q["admin"]})
    return jsonify({'users': output})

@app.route('/user/<public_id>', methods=['GET'])
def get_one_user(public_id):
    user = users.find_one({'public_id' : public_id})
    if not user:
        return jsonify({'message': 'No user found!'})
    user_data = {"public_id" : user["public_id"], "name" : user["name"], "login" : user["login"],
                 "password" : user["password"], "admin" : user["admin"]}
    return jsonify({'user' : user_data})

@app.route('/user/<public_id>', methods=['DELETE'])
def get_one_user(public_id):
    user = users.delete_one({'public_id' : public_id})
    if not user:
        return jsonify({'message': 'No user found!'})

    return jsonify({'message' : 'User has been deleted'})

@app.route('/user/<public_id>', methods=['PUT'])
def get_one_user(public_id):
    data = request.get_json()

    hashed_pass = generate_password_hash(data['password'], method='sha256')

    user = users.update_one({'public_id' : public_id}, {'$set': {'name': data['name'],
        'login': data['login'], 'password' : hashed_pass, 'admin' : data['admin']}})
    if not user:
        return jsonify({'message' : 'No user found!'})

    return jsonify({'message' : 'User was updated'})

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()

    hashed_pass = generate_password_hash(data['password'], method='sha256')

    users.insert_one({"public_id": str(uuid.uuid4()), "name": data['name'], "password": hashed_pass,
                      "login": data['login'], "admin": False})
    return jsonify({'message' : 'New user created'})

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
    app.run(host='0.0.0.0')