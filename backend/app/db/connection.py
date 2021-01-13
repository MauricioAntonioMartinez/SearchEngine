import logging as logging
import os

from pymongo import MongoClient


class MongoAPI:
    MONGO_URI = os.environ.get("MONGO_URI")

    def __init__(self):
        self.instance = MongoClient(self.MONGO_URI)
        db = self.instance["pages"]
        self.collection = db["pages"]
     
    def read(self,metadata):
        print(metadata.split(" "))
        documents = self.collection.find({ "metadata": { "$in": metadata.split(" ")} })
        jobs = [{job: data[job] for job in data if job != '_id'}
                  for data in documents]
        return jobs 

    def write(self, data):
        response = self.collection.insert_one(data)
        output = {'Status': 'Successfully Inserted',
                  'Document_ID': str(response.inserted_id)}
        return output

    def update(self):
        updated_data = {}
        response = self.collection.update_one({}, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output

    def delete(self, job_id):
        response = self.collection.delete_one({"_id":job_id})
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0
         else "Document not found."}
        return output


