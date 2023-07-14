from flask import Flask, jsonify, json
from flask_restful import Api, Resource,reqparse

app = Flask(__name__)
api = Api(app)

class myApi(Resource):
 
    @app.route("/data/<int:id>", methods=["GET"])
    def getData(id): 
        with open("data.json", "r") as jsonFile:
            data = json.load(jsonFile)

        for item in data:
            if (item["id"] == id):
                return jsonify(item)

    @app.route("/data/<int:id>", methods=["PUT"])
    def putData(id):
        with open("data.json", "r") as jsonFile:
            data = json.load(jsonFile)

        parser = reqparse.RequestParser()
        parser.add_argument("name", required=True)
        parser.add_argument("number", default="")
        params = parser.parse_args()

        for item in data:
            if (id == item["id"]):
                item["name"] = params["name"]
                item["number"] = params["number"]

        item = {
            "id": id,
            "name": params["name"],
            "number": params["number"]
        } 
        
        with open("data.json", "w") as writeJson:
            json.dump(data, writeJson)

        return ("Success")

    @app.route("/data/<int:id>", methods=["POST"])
    def postData(id):
        with open("data.json", "r") as jsonFile:
            data = json.load(jsonFile)

        parser = reqparse.RequestParser()
        parser.add_argument("name", required=True)
        parser.add_argument("number" defautl=" ")
        param = parser.parse_args()

        for item in data:
            if (id == item["id"]):
                return("Record already exist!")
        item = {
            "id": id,
            "name": param["name"],
            "number": param["number"]
        }

        with open("data.json", "w") as writeJson:
            json.dump(writeJson)

        return("Success")

    @app.route("/data/<int:id>", methods=["DELETE"])
    def deleteData(id):
        with open("data.json", "r") as jsonFile:
            data = json.load(jsonFile) 

        for item in data:
            if (item["id"] == id):
                data.remove(item)
                
        with open("data.json", "w") as writeFile:
            json.dump(data, writeFile)

        return("Success")

if __name__ == "__main__":
    app.run(debug=True)
