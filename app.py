#import library
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

#Inisiasi object flask
app = Flask(__name__)

#Inisiasi object flask_restful
api = Api(app)

#Inisiasi object flask_cors
CORS(app)

# variabel kososng
identitas = {}

#membuat class resource
class ContohResource(Resource):
    #method get dan post
    def get(self):
        #response = {"msg":"Halo dunia, COBA RESTFUL DONG"}
        return identitas
    
    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        identitas["nama"] = nama
        identitas["umur"] = umur
        response = {"msg":"sukses Dong"}
        return response


#setup resourcenya
api.add_resource(ContohResource, "/api", methods = ["GET","POST"])

if __name__ == "__main__":
    app.run(debug=True,port=5005)





