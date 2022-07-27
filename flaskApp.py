import email
from flask import Flask,request,jsonify
import mysql.connector
import pandas as pd
from yaml import load
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/feedback",methods=["GET"] )
@cross_origin(supports_credentials=True)
def home():
    args = request.args
    print(args)
    name = args['name']
    email = args['email']
    feedback = args['feedback']
    try:
        conn = mysql.connector.connect(host = "localhost",user = "root",database="xenon" ,password="root")
        query = f"insert into feedback (name,email,feedback) values('{name}','{email}','{feedback}')"
        print(query)
        cursor = conn.cursor()
        resp = cursor.execute(query)
        conn.commit()
        resp
        response.headers.add("Access-Control-Allow-Origin", "*")
        print("-"*20)
        print(resp)
        print("-"*20)
        response = jsonify(message="Inserted")

    # Enable Access-Control-Allow-Origin
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    except Exception as e:
        return "Error"
if __name__ == "__main__":
    app.run()
