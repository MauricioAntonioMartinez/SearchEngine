
import json
import os

from flask import Flask, Response, request
from flask_cors import CORS

from db.connection import MongoAPI
from manager import SearchEngine
from metadata.get_data import MetadataStractor
from scrape.get_links import Scraper

PORT = os.environ.get("PORT")



app = Flask(__name__)

cors = CORS(app,resources={r"/*":{"origins":"*"}})
app.secret_key ="thisisasupersecretkey"

db = MongoAPI()

@app.route('/', methods=['GET'])
def base():
    return Response(
        response={"success":True},
        status=200,
        mimetype='application/json')


@app.route('/page_index',methods=['POST'])
def page_index():
    url = request.args.get("url")
    if not url:
        return Response({"error":"URL not provided"})
    SearchEngine(url,db).index_page() 
    # links,content,title = Scraper(url).find_links()
    # print(title)
    # metadata = MetadataStractor(content).find_metadata()
    # db.write({"links":list(links),"metadata":metadata,"title":title})
    return Response(response=json.dumps({"url":url,"success":True}),status=200,
        mimetype='application/json')


@app.route('/search',methods=['POST'])
def search():
    query = request.args.get("q")
    if not query:
        return Response(response=json.dumps({"success":False,"message":"Query not provided"}),status=200,mimetype="application/json")

    data = db.read(query)
    # filtered_data = []
    # for item in data:
    #     if (any)
    return Response(response= json.dumps({"query":query,
    "results":data,"success":True}),status=200,mimetype="application/json")

@app.route('/links',methods=["GET"])
def links():

    links = db.read("")

    return {"data":links}

if __name__ == '__main__':
    app.run(debug=True,port=PORT,host="0.0.0.0")
    print("Connection Stablish")
    print(f"Listen traffic through http://localhost:{PORT}")
