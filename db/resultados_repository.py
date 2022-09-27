from models.resultados_model import ResultadosModel
from db.repository import Repository
from bson import ObjectId
from pymongo import MongoClient 

class ResultadosRepository(Repository[ResultadosModel]):
    def __init__(self):
        super().__init__()

    def get_all_table(self):
        theQuery = {}
        data = self.query(theQuery)
        result = {}
        all_results = []
        for d in data:
            result = {}
            result["_id_table"] = d["_id"]
            result["name"] =  d["user"]["name"]
            result["lastname"] =  d["user"]["lastname"]
            result["match"] = d["user"]["match"]["name"]
            result["votes"] = d["votes"]
            all_results.append(result)
        
        return sorted(all_results, key=lambda x: x['votes'], reverse=True)
    
    def get_mesas_id(self, mesas_id):
        theQuery = {"table.$id": ObjectId(mesas_id)}
        data = self.query(theQuery)
        result = {}
        all_results = []
        for d in data:
            result = {}
            result["_id_result"] = d["_id"]
            result["name"] =  d["user"]["name"]
            result["lastname"] =  d["user"]["lastname"]
            result["match"] = d["user"]["match"]["name"]
            result["votes"] = d["votes"]
            all_results.append(result)
        return all_results
        

        

    